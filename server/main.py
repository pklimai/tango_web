# -*- coding: utf-8 -*-
import json
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

import dash_extensions as de
import dash_bootstrap_components as dbc

# import dash_core_components as dcc
from dash import dcc

# import dash_html_components as html
from dash import html

import nica_dash_components
#from nica_dash_components import nica_dash_components

from server.utils import get_available_runs, get_values_from_api

from server import app
from server.config import DEBUG, PORT, HOST, ALIASES
from server.typings import ScatterPlots
from server.utils import get_run, _get_available_attrs, prepare_datetime

_container_style = {
    'background': "#e0e0e0",
    "height": "100vh"
}

_toolbar_style = {
    "justifyContent": 'center',
    "textAlign": 'center',
    "color": "white",
    "width": "100%"
}
_selectors_style = {
    "minWidth": "250px",
    "margin": "10px",
    "borderRadius": "0.6em"
}
_button_style = {"margin": "15px"}


def make_layout():
    return dbc.Container(
        fluid=1,
        style=_container_style,
        children=[
            # de.Keyboard(id="keyboard"),
            dbc.Navbar(color='primary', children=[html.H3(
                "BM@N Slow Control Viewer",
                style=_toolbar_style)]),
            dbc.Row(style={"display": "flex", "width": "100%"},
                    children=[
                        dbc.Col(style={"paddingRight": "0px", "minWidth": "270px", "maxWidth": "330px"}, children=[
                            dbc.Row(children=dbc.Col(
                                children=nica_dash_components.TangoParameterSelector(
                                    id="param-selector",
                                    style=_selectors_style,
                                    availableParams=_get_available_attrs(),
                                    dictionary=ALIASES,
                                )
                            )
                            ),
                            dbc.Row(children=dbc.Col(
                                children=nica_dash_components.RunSelector(
                                    id="run-selector",
                                    style=_selectors_style,
                                    # selectedRun=dict(period=7, number=5158),
                                    availableRuns=get_available_runs()
                                )
                            )),
                            dbc.Row(children=dbc.Col(
                                style={
                                    "justifyContent": 'center',
                                    "textAlign": 'center',

                                },
                                children=[
                                    dbc.Button(id="button-reset", children="RESET", style=_button_style, href="/",
                                               external_link=True),
                                    dbc.Button(id="button-show", children="SHOW", style=_button_style)
                                    # html.A(html.Button('Refresh Data'),href='/')
                                ]
                            )
                            )
                        ]),
                        dbc.Col(style={"paddingLeft": "0px"}, children=[
                            dbc.Card(
                                style={
                                    "width": "min(1200px, 100%)",
                                    "margin": "10px",
                                    "borderRadius": "0.6em",
                                    "padding": "20px",
                                    "display": "flex"
                                },
                                children=[
                                    html.H6(
                                        id="graph-title",
                                        children="Graph",
                                        style={"textAlign": "center"}
                                    ),
                                    dcc.Graph(
                                        id="live-update-graph",
                                        style={"width": "min(1200px, 100%)"}
                                    )
                                ]
                            )
                        ]),
                    ])
        ])


app.layout = make_layout()


@app.callback(Output('run-selector', 'selectedTimeInterval'),
              [Input('run-selector', 'selectedRun')],
              (State('run-selector', 'selectedTimeInterval'),))
def update_timerange(selected_run, selected_time_interval):
    if selected_run:
        run = get_run(selected_run.get('period'), selected_run.get('number'))
        if not run:
            return selected_time_interval
        return dict(start=run.start_datetime, end=run.end_datetime)
    return selected_time_interval


@app.callback(Output('graph-title', 'children'),
              [Input('button-show', 'n_clicks')],
              (State('param-selector', 'selectedParam'),))
def set_graph_title(n_clicks, selected_param) -> str:
    if n_clicks == 0 or not selected_param:
        return "Graph"

    domain = selected_param["domain"]
    family = selected_param["family"]
    member = selected_param["member"]
    name = selected_param["name"]

    if domain == "" or family == "" or member == "" or name == "":
        return "Graph"

    return "{}/{}/{}/{}".format(domain, family, member, name)


@app.callback(Output('button-show', 'disabled'),
              [Input('run-selector', 'selectedTimeInterval'),
               Input('run-selector', 'selectedRun'),
               Input('run-selector', 'timeCheckedProperty'),
               Input('run-selector', 'wrongRunProperty'),
               Input('param-selector', 'selectedParam'),
               Input('param-selector', 'isCustomProperty')])
def enable_show_button(selected_time_interval, selected_run, time_checked_property, wrong_number_property, selected_param, is_custom_property):
    # return (not selected_param) or (not selected_time_interval)
    # print(f"enable_show_button: {selected_param} {selected_time_interval}")
    # print(f"enable_show_button: selected_param={selected_param}")
    # print(f"enable_show_button: selected_run={selected_run}")

    if (not selected_time_interval) or not selected_param:
        return True

    if time_checked_property in [False, None]:
        if selected_run is None:
            return True
        if selected_run.get("period") is None or selected_run.get("number") is None:
            return True

    if wrong_number_property == True:
        return True

    if (selected_param.get("domain") == "" or
            selected_param.get("family") == "" or
            selected_param.get("member") == "" or
            selected_param.get("name") == ""):
        return True

    return False


@app.callback(Output('live-update-graph', 'figure'),
              [Input('button-show', 'n_clicks')],
              (State('run-selector', 'selectedTimeInterval'),
               State('run-selector', 'selectedRun'),
               State('param-selector', 'selectedParam'),
               State('run-selector', 'timeCheckedProperty')))
def draw_group(n_clicks, selected_time_interval, selected_run, selected_param, time_checked) -> go.Figure:
    # Override time interval if there is a run selected and slider is on Run selection
    if time_checked == False:
        if selected_run:
            run = get_run(selected_run['period'], selected_run['number'])
            if run:
                selected_time_interval = dict(start=str(run.start_datetime), end=str(run.end_datetime))

    if n_clicks == 0 or (not selected_param) or (not selected_time_interval) \
            or (time_checked in [False, None] and (selected_run.get("period") is None or selected_run.get("number") is None)):
        return go.Figure(layout=go.Layout(
            margin=dict(l=50, r=50, b=50, t=50, pad=4),
            height=600,
        ))

    offset_min = 0
    if selected_time_interval is not None:
        offset_min = int(selected_time_interval.get("timezoneOffset") or 0)

    start_dt = prepare_datetime(selected_time_interval["start"], offset_min)
    end_dt = prepare_datetime(selected_time_interval["end"], offset_min)

    # print(selected_time_interval)
    # print(start_dt, end_dt)

    domain = selected_param["domain"]
    family = selected_param["family"]
    member = selected_param["member"]
    name = selected_param["name"]

    graph_data = get_values_from_api(domain, family, member, name, start_dt, end_dt)
    # print(graph_data)

    data = [go.Scatter(x=graph_data['datetimes'], y=graph_data['values'], mode='lines + markers')]

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
