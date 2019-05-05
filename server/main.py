# -*- coding: utf-8 -*-
from datetime import datetime, date
from itertools import groupby
from multiprocessing import Lock
from typing import List, Dict, Iterable

import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from dateutil import parser
from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc, text, and_, func
from sqlalchemy.engine import Engine
from sqlalchemy.testing.schema import Table

from server import app, db, cache
from server.orm.bmn import Run
from server.orm.hdbpp import AttConf, AttConfDataType
from server.typings import ScatterPlots, RunEntry

_min_datetime_lock = Lock()
_max_datetime_lock = Lock()

md_text = '''
#### Test [markdown](http://commonmark.org/help) message

This page reads 
[att_array_devdouble_rw](http://localhost:8080/?server=db&username=bmn&db=hdbpp&table=att_array_devdouble_rw) 
table from database and displays 92, 93 
[atts](http://localhost:8080/?server=db&username=bmn&db=hdbpp&table=att_conf) with idx = 1.

- Indicators are updated every second.
- Pressing power button widget will pause/resume monitoring.


'''

app.layout = html.Div(children=[
    html.H1(children='BM@N slow controls sample'),
    dcc.Markdown(md_text),
    html.Div([
        daq.PowerButton(
            id='my-daq-powerbutton',
            on=True, style={'width': '10%', 'display': 'inline-block'}
        ),
        daq.Indicator(
            id='my-indicator',
            label="Online",
            value=True, style={'width': '10%', 'display': 'inline-block'}
        ),
        html.P("last-updated", id='last-updated', style={'width': '20%', 'display': 'inline-block'}),
    ], style={'display': 'flex'}),


    dcc.Markdown("### Select run"),

    html.Div([
        dcc.DatePickerRange(
            id='runs-date-digital-border',
            clearable=True,
            reopen_calendar_on_clear=True,
            style={'display': 'inline', 'margin-left': '80px', 'margin-right': '80px'}),
        html.Div([dcc.RangeSlider(id="runs-date-range", min=0, max=1000, value=[0, 1000])],
                 style={'width': '80%', 'display': 'inline', 'margin-left': '80px', 'margin-right': '80px'}),
        dcc.Interval(id='runs-date-range-init', interval=0, n_intervals=1, max_intervals=1)
    ], style={'display': 'inline-block', 'width': '100%'}),

    html.Div([
        html.P("undefined date range", id="runs-date-range-info",
               style={'width': '40%', 'display': 'inline'}),
        html.Button('Load Runs', id='runs-date-load-button', style={'display': 'inline'}),
        dcc.Dropdown(id='runs-date-dropdown', style={'display': 'inline', 'float': 'right',  'width': '60vh'}),
    ], style={'display': 'flex', 'width': '100%'}),


    dcc.Markdown("### Select Group"),
    html.Div([
        dcc.Dropdown(id='domain-dropdown', placeholder="domain", style={'width': '150px'}),
        dcc.Dropdown(id='family-dropdown', placeholder="family", style={'width': '150px'}),
        dcc.Dropdown(id='member-dropdown', placeholder="member", style={'width': '150px'}),
        dcc.Dropdown(id='name-dropdown', placeholder="name", style={'width': '150px'}),
        html.Button('show', id='show-button'),
        dcc.Interval(id='group-initial-interval', interval=0, n_intervals=1, max_intervals=1)
    ], style={'display': 'flex'}),


    dcc.Markdown("### Graph"),
    html.Div([
        dcc.Graph(id='live-update-graph', animate=False),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,
            n_intervals=0
        )
    ])
])


def _get_min_datetime() -> datetime:
    with _min_datetime_lock:
        return _get_min_datetime_impl()


@cache.memoize(timeout=60)
def _get_min_datetime_impl() -> datetime:
    return db.session.query(func.min(Run.start_datetime).label('min')).scalar()


def _get_max_datetime() -> datetime:
    with _max_datetime_lock:
        return _get_max_datetime_impl()


@cache.memoize(timeout=60)
def _get_max_datetime_impl() -> datetime:
    return db.session.query(func.max(Run.end_datetime).label('max')).scalar()

@cache.cached()
def _get_run(period_number: int, run_number: int) -> Run:
    return db.session.query(Run)\
        .filter(and_(Run.period_number==period_number, Run.run_number==run_number)).first()

def _get_run_datetime_range(period_number: int, run_number: int) -> List[datetime]:
    run: Run = _get_run(period_number, run_number)
    return [run.start_datetime, run.end_datetime]


@cache.cached()
def _get_run_atts(period_number: int, run_number: int) -> List[int]:

    run = _get_run(period_number, run_number)
    query: Iterable[AttConfDataType] = db.session.query(AttConfDataType)
    engine: Engine = db.get_engine(app.server, 'hdbpp')

    def get_values(query_: Iterable[AttConfDataType], run_: Run) -> Iterable[int]:
        for data_type in query_:
            table_name = 'att_' + data_type.data_type

            sql = """SELECT DISTINCT att_conf_id
            FROM {}
            WHERE data_time > "{}" AND data_time < "{}";
            """.format(table_name, run_.start_datetime, run_.end_datetime)

            values: List[int] = [v[0] for v in engine.execute(sql).fetchall()]

            for value in values:
                yield int(value)

    return list(get_values(query, run))


def _get_run_atts_simple(run_raw: str) -> List[int]:
    period_number, run_number = [int(v) for v in run_raw.split(" ")]
    return _get_run_atts(period_number, run_number)


@app.callback(Output('runs-date-digital-border', 'start_date'),
              [Input('runs-date-range-init', 'n_intervals')])
def initialize_min_date(_) -> date:
    min_time = _get_min_datetime()
    return min_time.date()


@app.callback(Output('runs-date-digital-border', 'min_date_allowed'),
              [Input('runs-date-range-init', 'n_intervals')])
def initialize_min_date_allowed(_) -> date:
    min_time = _get_min_datetime()
    return min_time.date()


@app.callback(Output('runs-date-digital-border', 'end_date'),
              [Input('runs-date-range-init', 'n_intervals')])
def initialize_max_date(_) -> date:
    max_time = _get_max_datetime()
    return max_time.date()


@app.callback(Output('runs-date-digital-border', 'max_date_allowed'),
              [Input('runs-date-range-init', 'n_intervals')])
def initialize_max_date_allowed(_) -> date:
    max_time = _get_max_datetime()
    return max_time.date()


@app.callback(Output('runs-date-range', 'min'),
              [Input('runs-date-digital-border', 'start_date')])
def set_left_border(start_date: datetime) -> int:
    return int(parser.parse(start_date).timestamp())


@app.callback(Output('runs-date-range', 'max'),
              [Input('runs-date-digital-border', 'end_date')])
def set_right_border(end_date: datetime) -> int:
    return int(parser.parse(end_date).timestamp())


@app.callback(Output('runs-date-range', 'marks'),
              [Input('runs-date-digital-border', 'start_date'), Input('runs-date-digital-border', 'end_date')])
def update_marks(start_date_raw: str, end_date_raw: str) -> Dict[int, str]:
    start_date = parser.parse(start_date_raw)
    end_date = parser.parse(end_date_raw)
    return {int(start_date.timestamp()): start_date.isoformat(), int(end_date.timestamp()): end_date.isoformat()}


@app.callback(Output('runs-date-range', 'value'),
              [Input('runs-date-digital-border', 'start_date'), Input('runs-date-digital-border', 'end_date')])
def update_values(start_date_raw: str, end_date_raw: str) -> List[int]:
    start_date = parser.parse(start_date_raw)
    end_date = parser.parse(end_date_raw)
    return [int(start_date.timestamp()), int(end_date.timestamp())]


@app.callback(Output('runs-date-range-info', 'children'),
              [Input('runs-date-range', 'value')])
def update_info(range: List[float]) -> str:
    range_left = datetime.fromtimestamp(float(range[0]))
    range_right = datetime.fromtimestamp(float(range[-1]))

    filtered = db.session.query(Run.start_datetime)\
        .filter(and_(Run.end_datetime >= range_left, Run.start_datetime <= range_right))

    return "{} - {}: found {} runs".format(range_left.isoformat(), range_right.isoformat(), filtered.count())


@app.callback(Output('runs-date-dropdown', 'options'),
              [Input('runs-date-load-button', 'n_clicks')],
              [State('runs-date-range', 'value')])
def load_run(_, range_: List[int]) -> List[RunEntry]:
    range_left = datetime.fromtimestamp(float(range_[0]))
    range_right = datetime.fromtimestamp(float(range_[-1]))

    filtered: Iterable[Run] = db.session.query(Run) \
        .filter(and_(Run.end_datetime >= range_left, Run.start_datetime <= range_right)).order_by(Run.start_datetime)

    return [{
        'label': "{},{} ({} - {})".format(
            it.period_number, it.run_number, it.start_datetime, it.end_datetime),
        'value': "{} {}".format(it.period_number, it.run_number)
    } for it in filtered]


@app.callback(Output("last-updated", "children"), [Input('live-update-graph', 'figure')])
def update_last_time(_):
    return 'last-updated: {}'.format(datetime.now().time().isoformat()[:-7])


@app.callback(Output('my-indicator', 'value'), [Input('my-daq-powerbutton', 'on')])
def update_indicator(state: bool) -> bool:
    return state


# @app.callback(Output('interval-component', 'disabled'), [Input('my-daq-powerbutton', 'on')])
# def update_acquisition(state: bool) -> bool:
#     return not state


@app.callback(Output('domain-dropdown', 'options'),
              [Input('runs-date-dropdown', 'value')])
def initialize_domains(run_raw: str):
    """Get all available domains from database."""
    if run_raw is None:
        return []
    atts = _get_run_atts_simple(run_raw)
    query = db.session.query(AttConf.domain)\
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in atts)))).distinct()
    return [
        {'label': v[0], 'value': v[0]}
        for v in query]


@app.callback(Output('family-dropdown', 'options'),
              [Input('domain-dropdown', 'value')],
              [State('runs-date-dropdown', 'value')])
def update_families(domain: str, run_raw: str):
    if domain is None:
        return []

    query = db.session.query(AttConf.family)\
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_run_atts_simple(run_raw)))))\
        .filter(AttConf.domain == domain)\
        .distinct()
    return [{'label': v[0], 'value': v[0]} for v in query]


@app.callback(Output('member-dropdown', 'options'),
              [Input('family-dropdown', 'value')],
              [State('domain-dropdown', 'value'),
               State('runs-date-dropdown', 'value')])
def update_members(family: str, domain:str, run_raw: str):
    if family is None:
        return []
    return [{'label': v[0], 'value': v[0]} for v in db.session.query(AttConf.member)
            .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_run_atts_simple(run_raw)))))
            .filter(AttConf.family == family)
            .filter(AttConf.domain == domain)
            .distinct()]


@app.callback(Output('name-dropdown', 'options'),
              [Input('member-dropdown', 'value')],
              [State('domain-dropdown', 'value'),
               State('family-dropdown', 'value'),
               State('runs-date-dropdown', 'value')])
def update_names(member: str, domain: str, family: str, run_raw: str):
    if member is None:
        return []

    query = db.session.query(AttConf.name)\
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_run_atts_simple(run_raw)))))\
        .filter(AttConf.member == member) \
        .filter(AttConf.family == family)\
        .filter(AttConf.domain == domain)\
        .distinct()
    return [{'label': v[0], 'value': v[0]} for v in query]


@app.callback(Output('show-button', 'disabled'),[
                  Input('domain-dropdown', 'value'),
                  Input('family-dropdown', 'value'),
                  Input('member-dropdown', 'value'),
                  Input('name-dropdown', 'value'),])
def set_button_enabled(domain: str, family: str, member: str, name: str):
    return not all(v is not None for v in (str, family, member, name))


@app.callback(Output('live-update-graph', 'figure'),
              [Input('show-button', 'n_clicks')],
              [ State('domain-dropdown', 'value'),
                State('family-dropdown', 'value'),
                State('member-dropdown', 'value'),
                State('name-dropdown', 'value'),
                State('runs-date-dropdown', 'value')])
def update_graph_live(n_clicks: int, domain: str, family: str, member: str, name: str, run_raw: str) -> go.Figure:
    if n_clicks is None:
        return go.Figure()

    configs: List[AttConf] = list(db.session.query(AttConf).filter(
        and_(AttConf.domain == domain, AttConf.family == family, AttConf.member == member, AttConf.name == name)))

    if len(configs) == 0:
        return go.Figure()

    data: ScatterPlots = []

    for config in configs:

        data_type: AttConfDataType = AttConfDataType.query.get(config.att_conf_data_type_id)
        table: Table = db.metadata.tables['att_' + data_type.data_type]

        if data_type.data_type.startswith("scalar"):
            values: BaseQuery = db.session.query(table) \
                .filter(text("att_conf_id = {}".format(config.att_conf_id))).order_by(desc("data_time"))
            data += [go.Scatter(
                x=[entry.data_time for entry in values],
                y=[entry.value_r for entry in values],
                name=config.att_conf_id,
                mode='lines + markers',
            )]
        else:
            values: BaseQuery = db.session.query(table)\
                .filter(text("att_conf_id = {}".format(config.att_conf_id))).order_by(desc("data_time"))
            groups = []
            keys = []
            for k, g in groupby(sorted(values, key=lambda v: (v.att_conf_id, v.idx)), lambda v: (v.att_conf_id, v.idx)):
                groups.append(sorted(g, key=lambda v: v.data_time))
                keys.append(k)

            data += [go.Scatter(
                x=[entry.data_time for entry in entries],
                y=[entry.value_r for entry in entries],
                name='{}'.format(key),
                mode='lines + markers',
            ) for key, entries in zip(keys, groups)]

    return go.Figure(
        data=data,
        layout=go.Layout(
            title="Output sample",
            xaxis=go.layout.XAxis(title='Acquisition Time'),
            yaxis=go.layout.YAxis(title='U')
        )
    )


if __name__ == '__main__':
    app.run_server(debug=True)
