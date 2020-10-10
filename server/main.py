# -*- coding: utf-8 -*-
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import sd_material_ui

import nica_dash_components

from server.utils import _get_available_runs

from server import app
from server.config import DEBUG, PORT, HOST
from server.typings import ScatterPlots
from server.utils import _get_run, _get_attrs_for_params, get_values, _get_available_attrs, prepare_datetime

_container_style = {
    'background': "#e0e0e0",
    "height": "100vh"
}

_toolbar_style = {
    "justify-content": 'center',
    "text-align": 'center',
    "color": "white",
    "width": "100%"
}
_selectors_style = {
    "min-width": "250px",
    "margin": "10px",
    "border-radius": "0.6em"
}
_button_style = {"margin": "5px"}


def make_layout():
    return dbc.Container(
        fluid=1,
        style=_container_style,
        children=[
        dbc.Navbar(color='primary', children=[html.H3(
            "BM@N Slow Control Viewer",
            style=_toolbar_style)]),
        dbc.Row([
            dbc.Col(xs=2, children=[
                dbc.Row(children=dbc.Col(
                    children=nica_dash_components.TangoParameterSelector(
                            id="param-selector",
                            style=_selectors_style,
                            availableParams=_get_available_attrs(),
                            dictionary=[{
                                'name': "test_param",
                                'param': dict(domain="mpd", family="sts", member="hv", name="i")
                            }],
                        )
                    )
                ),
                dbc.Row(children=dbc.Col(
                    children=nica_dash_components.RunSelector(
                        id="run-selector",
                        style=_selectors_style,
                        selectedRun=dict(period=7, number=5158),
                        availableRuns=_get_available_runs())
                )),
                dbc.Row(children=dbc.Col(
                    style={
                        "justify-content": 'center',
                        "text-align": 'center',

                    },
                    children=[
                        dbc.Button(id="button-show", children="SHOW", style=_button_style),
                        ]
                    )
                )
            ]),
            dbc.Col(xs=10, children=[
                sd_material_ui.Card(
                    id="graph-card",
                    style=_selectors_style,
                    headerStyle={
                        "justify-content": 'center',
                        "text-align": 'center'
                    },
                    expanded=True,
                    children=[dcc.Graph(
                        id="live-update-graph",

                    )])
            ]),
        ])
    ])


app.layout = make_layout()


@app.callback(Output('run-selector', 'selectedTimeInterval'),
              [Input('run-selector', 'selectedRun')],
              (State('run-selector', 'selectedTimeInterval'),))
def update_timerange(selected_run, selected_time_interval):
    if selected_run:
        run = _get_run(selected_run['period'], selected_run['number'])
        return dict(start=run.start_datetime, end=run.end_datetime)
    return selected_time_interval


@app.callback(Output('graph-card', 'headerTitle'),
              [Input('button-show', 'n_clicks')],
              (State('param-selector', 'selectedParam'),))
def set_graph_title(n_clicks, selected_param) -> str:
    if n_clicks == 0 or not selected_param:
        return "Graph"

    domain = selected_param["domain"]
    family = selected_param["family"]
    member = selected_param["member"]
    name = selected_param["name"]

    return "{}/{}/{}/{}".format(domain, family, member, name)


@app.callback(Output('live-update-graph', 'figure'),
              [Input('button-show', 'n_clicks')],
              (State('run-selector', 'selectedTimeInterval'),
               State('param-selector', 'selectedParam'),))
def draw_group(n_clicks, selected_time_interval, selected_param) -> go.Figure:
    if n_clicks == 0 or (not selected_param) or (not selected_time_interval):
        return go.Figure(layout=go.Layout(
            margin=dict(l=50, r=50, b=50, t=50, pad=4),
            height=600,
        ))

    start_dt = prepare_datetime(selected_time_interval["start"])
    end_dt = prepare_datetime(selected_time_interval["end"])

    domain = selected_param["domain"]
    family = selected_param["family"]
    member = selected_param["member"]
    name = selected_param["name"]

    attrs = _get_attrs_for_params(domain, family, member, name)

    data: ScatterPlots = []

    for attr in attrs:
        graphs_data = get_values(attr[0], attr[1], start_dt, end_dt)
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
            xaxis=go.layout.XAxis(title='Acquisition Time'),
            margin=dict(l=50, r=50, b=50, t=50, pad=4),
            height=600,
        )
    )


if __name__ == '__main__':
    app.run_server(debug=DEBUG, host=HOST, port=PORT)
