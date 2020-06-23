# -*- coding: utf-8 -*-
from typing import List, Union
from dateutil.parser import parse

import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sqlalchemy import text

from server import app, db
from server.config import DEBUG, PORT, HOST
from server.layout import make_layout, make_timerange
from server.orm.bmn import Run
from server.orm.hdbpp import AttConf
from server.typings import DomainEntry, Style, ScatterPlots
from server.utils import _get_run, _get_run_attrs, initialize_domains, _get_attrs_for_params, get_values, _get_attrs

app.layout = make_layout([n[0] for n in sorted(
    db.session.query(Run.period_number).distinct())])


@app.callback(Output('run-number', 'placeholder'),
              [Input('run-period', 'value')])
def set_period_runs_range(period) -> str:
    if period is None:
        return "Run Number"
    runs = [n[0] for n in sorted(db.session.query(Run.run_number).filter(Run.period_number == period).distinct())]
    return "{} ... {}".format(min(runs), max(runs))


@app.callback(Output('run-number', 'disabled'),
              [Input('run-period', 'value')])
def run_number_disabled(period) -> bool:
    if period is None:
        return True
    else:
        return False


@app.callback(Output('run-apply', 'disabled'),
              [Input('run-period', 'value'), Input('run-number', 'value')])
def run_apply_disabled(period, number) -> bool:
    return (period is None) or (number is None)


@app.callback([Output('time-range-formgroup', 'children')],
              [Input('run-apply', 'n_clicks_timestamp')],
              [State('run-period', 'value'),
               State('run-number', 'value')])
def apply_run_time_range(
        apply_click_time: int, period: int, run: int) -> (Union[int, None], Union[int, None]):
    entry = _get_run(period, run)
    if entry:
        return [make_timerange(entry.start_datetime, entry.end_datetime)]
    else:
        return [make_timerange()]


@app.callback([Output('curr-start-datetime', 'value'),
               Output('curr-end-datetime', 'value')],
              [Input('datetime-apply', 'n_clicks_timestamp')],
              [State('start-date', 'value'),
               State('start-time', 'value'),
               State('end-date', 'value'),
               State('end-time', 'value')])
def apply_run_selection(
        apply_click_time: int, start_date, start_time, end_date, end_time):

    if apply_click_time == 0:
        return [None, None]

    return [
        parse("{} {}".format(start_date, start_time)).isoformat(),
        parse("{} {}".format(end_date, end_time)).isoformat()]


# @app.callback([Output('curr-run-period', 'value'),
#                Output('curr-run-number', 'value'),
#                Output('notfound-warning', 'hidden')],
#               [Input('run-apply', 'n_clicks_timestamp')],
#               [State('run-period', 'value'),
#                State('run-number', 'value')])
# def apply_run_selection(
#         apply_click_time: int, period: int, run: int) -> (Union[int, None], Union[int, None]):
#     entry = _get_run(period, run)
#     if entry:
#         return period, run, True
#     else:
#         return None, None, period is None or run is None


@app.callback([Output('selected-run-view', 'style'),
               Output('run_info', 'children'),
               Output('domain-dropdown', 'options')],
              [Input('curr-start-datetime', 'value'),
               Input('curr-end-datetime', 'value')])
def apply_run_view(start: str, end: str) -> (Style, List[DomainEntry]):

    if start is None or end is None:
        return {'display': 'none'}, None, []

    start_dt = parse(start)
    end_dt = parse(end)

    return {'display': 'inherit'}, None, initialize_domains(start_dt, end_dt)


@app.callback(Output('family-dropdown', 'options'),
              [Input('domain-dropdown', 'value')],
              [State('curr-start-datetime', 'value'),
               State('curr-end-datetime', 'value')])
def update_families(domain: str, start: str, end: str) -> List[DomainEntry]:
    if domain is None:
        return []

    start_dt = parse(start)
    end_dt = parse(end)

    query = db.session.query(AttConf.family) \
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_attrs(start_dt, end_dt))))) \
        .filter(AttConf.domain == domain) \
        .distinct()
    return [{'label': v[0], 'value': v[0]} for v in query]


@app.callback(Output('member-dropdown', 'options'),
              [Input('family-dropdown', 'value'),
               Input('domain-dropdown', 'value')],
              [State('curr-start-datetime', 'value'),
               State('curr-end-datetime', 'value')])
def update_members(family: str, domain: str, start: str, end: str):
    if family is None or domain is None:
        return []

    start_dt = parse(start)
    end_dt = parse(end)

    return [{'label': v[0], 'value': v[0]} for v in db.session.query(AttConf.member)
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_attrs(start_dt, end_dt)))))
        .filter(AttConf.family == family)
        .filter(AttConf.domain == domain)
        .distinct()]


@app.callback(Output('name-dropdown', 'value'),
              [Input('member-dropdown', 'value'),
               Input('family-dropdown', 'value'),
               Input('domain-dropdown', 'value')],
              [State('name-dropdown', 'value')])
def update_names(member: str, family: str, domain: str, name: str):
    if member is None or family is None or domain is None:
        return None
    else:
        return name


@app.callback(Output('name-dropdown', 'options'),
              [Input('member-dropdown', 'value'),
               Input('family-dropdown', 'value'),
               Input('domain-dropdown', 'value')],
              [State('curr-start-datetime', 'value'),
               State('curr-end-datetime', 'value')])
def update_names(member: str, family: str, domain: str, start: str, end: str):

    if member is None or family is None or domain is None:
        return []

    start_dt = parse(start)
    end_dt = parse(end)

    query = db.session.query(AttConf.name) \
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_attrs(start_dt, end_dt))))) \
        .filter(AttConf.member == member) \
        .filter(AttConf.family == family) \
        .filter(AttConf.domain == domain) \
        .distinct()
    return [{'label': v[0], 'value': v[0]} for v in query]


@app.callback(Output('data-apply', 'disabled'),
              [Input('name-dropdown', 'value'),
               Input('member-dropdown', 'value'),
               Input('family-dropdown', 'value'),
               Input('domain-dropdown', 'value')])
def data_apply_disabled(name: str, member: str, family: str, domain: str) -> bool:
    return name is None


@app.callback(Output('live-update-graph', 'figure'),
              [Input('data-apply', 'n_clicks')],
              [State('name-dropdown', 'value'),
               State('member-dropdown', 'value'),
               State('family-dropdown', 'value'),
               State('domain-dropdown', 'value'),
               State('curr-start-datetime', 'value'),
               State('curr-end-datetime', 'value')])
def draw_group(
        n_clicks: int, name: str, member: str, family: str, domain: str, start: str, end: str) -> go.Figure:
    if n_clicks is None:
        return go.Figure(layout=go.Layout(
            height=500,
        ))

    attrs = _get_attrs_for_params(domain, family, member, name)

    start_dt = parse(start)
    end_dt = parse(end)

    data: ScatterPlots = []
    for attr in attrs:
        graphs_data = get_values(attr[0], attr[1], start, end)
        for graph_idx in graphs_data:
            graph_data = graphs_data[graph_idx]
            data += [go.Scatter(
                x=[entry[0] for entry in graph_data],
                y=[entry[1] for entry in graph_data],
                name='{}:{}:{}'.format(attr[0], attr[1], graph_idx),
                mode='lines + markers')]

    return go.Figure(
        data=data,
        layout=go.Layout(
            title="{}/{}/{}/{}".format(domain, family, member, name),
            xaxis=go.layout.XAxis(title='Acquisition Time'),
            height=500,
        )
    )


if __name__ == '__main__':
    app.run_server(debug=DEBUG, host=HOST, port=PORT)
