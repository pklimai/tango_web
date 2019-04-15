# -*- coding: utf-8 -*-
from datetime import datetime
from itertools import groupby
from typing import List

import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc, text, and_
from sqlalchemy.testing.schema import Table

from server import app, db
from server.orm import AttConf, AttConfDataType
from server.typings import ScatterPlots

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

    html.Div([
        dcc.Dropdown(id='domain-dropdown', placeholder="domain", style={'width': '150px'}),
        dcc.Dropdown(id='family-dropdown', placeholder="family", style={'width': '150px'}),
        dcc.Dropdown(id='member-dropdown', placeholder="member", style={'width': '150px'}),
        dcc.Dropdown(id='name-dropdown', placeholder="name", style={'width': '150px'}),
        html.Button('show', id='show-button'),
        dcc.Interval(id='group-initial-interval', interval=0, n_intervals=1, max_intervals=1)
    ], style={'display': 'flex'}),

    html.Div([
        dcc.DatePickerRange(id='datepicler', start_date=datetime.now(), end_date=datetime.now())
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Graph(id='live-update-graph', animate=True),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,
            n_intervals=0
        )
    ])
])


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
              [Input('group-initial-interval', 'n_intervals')])
def initialize_domains(_):
    """Get all available domains from database."""
    return [{'label': v[0], 'value': v[0]} for v in db.session.query(AttConf.domain).distinct()]


@app.callback(Output('family-dropdown', 'options'),
              [Input('domain-dropdown', 'value')])
def update_families(domain: str):
    if str is None:
        return
    return [{'label': v[0], 'value': v[0]} for v in db.session.query(
        AttConf.family).filter(AttConf.domain == domain).distinct()]


@app.callback(Output('member-dropdown', 'options'),
              [Input('family-dropdown', 'value')])
def update_members(family: str):
    if str is None:
        return
    return [{'label': v[0], 'value': v[0]} for v in db.session.query(
        AttConf.member).filter(AttConf.family == family).distinct()]


@app.callback(Output('name-dropdown', 'options'),
              [Input('member-dropdown', 'value')])
def update_names(member: str):
    if str is None:
        return
    return [{'label': v[0], 'value': v[0]} for v in db.session.query(
        AttConf.name).filter(AttConf.member == member).distinct()]


@app.callback(Output('show-button', 'disabled'),[
                  Input('domain-dropdown', 'value'),
                  Input('family-dropdown', 'value'),
                  Input('member-dropdown', 'value'),
                  Input('name-dropdown', 'value'),])
def set_button_enabled(domain: str, family: str, member: str, name: str):
    return not all(v is not None for v in (str, family, member, name))


@app.callback(Output('live-update-graph', 'figure'),
              [Input('show-button', 'n_clicks')],
              [
                State('domain-dropdown', 'value'),
                State('family-dropdown', 'value'),
                State('member-dropdown', 'value'),
                State('name-dropdown', 'value')])
def update_graph_live(n_clicks: int, domain: str, family: str, member: str, name: str) -> go.Figure:
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
        last_values: BaseQuery = db.session.query(table).filter(
            text("att_conf_id = {}".format(config.att_conf_id))).order_by(desc("data_time")).limit(100)

        groups = []
        keys = []
        for k, g in groupby(sorted(last_values, key=lambda v: (v.att_conf_id, v.idx)), lambda v: (v.att_conf_id, v.idx)):
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
