# -*- coding: utf-8 -*-
from datetime import datetime
from itertools import groupby

import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sqlalchemy import desc, text

from server import app, db
from server.orm import t_att_array_devdouble_rw
from server.typings import ScatterPlots

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

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
        dcc.Graph(id='live-update-graph', animate=True),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,
            n_intervals=0
        )
    ])
])


@app.callback(Output("last-updated", "children"), [Input('live-update-graph', 'figure')])
def update_lat_time(_):
    return 'last-updated: {}'.format(datetime.now().time().isoformat()[:-7])


@app.callback(Output('my-indicator', 'value'), [Input('my-daq-powerbutton', 'on')])
def update_indicator(state):
    return state


@app.callback(Output('interval-component', 'disabled'), [Input('my-daq-powerbutton', 'on')])
def update_acquisition(state):
    return not state


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n: int) -> go.Figure:
    last_values = db.session.query(t_att_array_devdouble_rw)\
        .filter(text("att_conf_id IN (92,93)")).filter_by(idx=1)\
        .order_by(desc("data_time")).limit(30)

    groups = []
    keys = []
    for k, g in groupby(sorted(last_values, key=lambda v: (v.att_conf_id, v.idx)), lambda v: (v.att_conf_id, v.idx)):
        groups.append(sorted(g, key=lambda v: v.data_time))
        keys.append(k)

    data: ScatterPlots = [go.Scatter(
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