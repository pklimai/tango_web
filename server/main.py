# -*- coding: utf-8 -*-
from typing import List

from dateutil.parser import parse

import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sqlalchemy import text

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import sd_material_ui

import nica_dash_components

from server.utils import _get_available_runs

from server import app, db
from server.config import DEBUG, PORT, HOST
from server.orm.bmn import Run
from server.orm.hdbpp import AttConf
from server.typings import ScatterPlots
from server.utils import _get_run, _get_attrs_for_params, get_values, _get_attrs, prepare_datetime


def make_layout(runs: List[int]):
    return dbc.Container(fluid=1,
        style={'background': "#e0e0e0", "height": "100vh"},
        children=[
        dbc.Navbar(color='primary', children=[html.H3(
            "BM@N Slow Control Viewer",
            style={
                "justify-content": 'center',
                "text-align": 'center',
                "color": "white",
                "width": "100%"
            })]),
        dbc.Row([
            dbc.Col(xs=2, children=[
                dbc.Row(children=dbc.Col(
                    children=nica_dash_components.RunSelector(
                        id="run_selector",
                        selectedRun=dict(period=7, number=5158),
                        availableRuns=_get_available_runs()))),
                dbc.Row(children=dbc.Col(
                    children=[
                        nica_dash_components.TangoParameterSelector(
                            id="param_selector",
                            availableParams={}
                        )
                    ]
                ))
            ]),
            dbc.Col(xs=10, children=[
                sd_material_ui.Card(
                    id="graph-card",
                    style={"margin": "10px", "border-radius": "0.6em"},
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


app.layout = make_layout([n[0] for n in sorted(
    db.session.query(Run.period_number).distinct())])


@app.callback(Output('run_selector', 'selectedTimeInterval'),
              [Input('run_selector', 'selectedRun')],
              (State('run_selector', 'selectedTimeInterval'),))
def update_timerange(selected_run, selected_time_interval):
    if selected_run:
        run = _get_run(selected_run['period'], selected_run['number'])
        return dict(start=run.start_datetime, end=run.end_datetime)
    return selected_time_interval


@app.callback(Output('param_selector', 'selectedParam'),
              [Input('run_selector', 'selectedTimeInterval')])
def reset_selected_param(selected_time_interval):
    return None


@app.callback(Output('param_selector', 'availableParams'),
              [Input('run_selector', 'selectedTimeInterval')])
def update_attrs(selected_time_interval):
    if selected_time_interval:

        start_dt = prepare_datetime(selected_time_interval["start"])
        end_dt = prepare_datetime(selected_time_interval["end"])

        time_filter = text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_attrs(
            start_dt.isoformat(), end_dt.isoformat()))))

        domains: List[str] = [d[0] for d in db.session.query(AttConf.domain)
            .filter(time_filter).distinct()]

        result = {d: {} for d in domains}

        for domain in domains:
            families = [f[0] for f in db.session.query(AttConf.family)
                .filter(AttConf.domain == domain)
                .filter(time_filter)
                .distinct()]
            result[domain] = {f: {} for f in families}

            for family in families:
                members = [f[0] for f in db.session.query(AttConf.member)
                    .filter(AttConf.domain == domain)
                    .filter(AttConf.family == family)
                    .filter(time_filter)
                    .distinct()]
                result[domain][family] = members
        return result
    return {}


@app.callback(Output('graph-card', 'headerTitle'),
              [Input('param_selector', 'selectedParam')])
def set_graph_title(selected_param) -> str:
    if not selected_param:
        return "Graph"
    domain = selected_param["domain"]
    family = selected_param["family"]
    member = selected_param["member"]

    return "{}/{}/{}".format(domain, family, member)


@app.callback(Output('live-update-graph', 'figure'),
              [Input('param_selector', 'selectedParam')],
              (State('run_selector', 'selectedTimeInterval'),))
def draw_group(selected_param, selected_time_interval) -> go.Figure:
    if (not selected_param) or (not selected_time_interval):
        return go.Figure(layout=go.Layout(
            margin=dict(l=50, r=50, b=50, t=50, pad=4),
            height=600,
        ))

    start_dt = prepare_datetime(selected_time_interval["start"])
    end_dt = prepare_datetime(selected_time_interval["end"])

    domain = selected_param["domain"]
    family = selected_param["family"]
    member = selected_param["member"]

    attrs = _get_attrs_for_params(domain, family, member)

    data: ScatterPlots = []

    for attr in attrs:
        graphs_data = get_values(attr[0], attr[1], start_dt, end_dt)
        print(graphs_data)
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
