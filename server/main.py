# -*- coding: utf-8 -*-
from typing import List

from dateutil.parser import parse

import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sqlalchemy import text

import dash_bootstrap_components as dbc
import dash_core_components as dcc

import sd_material_ui

import nica_dash_components

from server.utils import _get_available_runs

from server import app, db
from server.config import DEBUG, PORT, HOST
from server.orm.bmn import Run
from server.orm.hdbpp import AttConf
from server.typings import ScatterPlots
from server.utils import _get_run, _get_attrs_for_params, get_values, _get_attrs


def make_layout(runs: List[int]):
    return dbc.Container(fluid=1, children=[
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
                        # html.H1(id="param_selector", children="Placeholder")
                    ]
                ))
            ]),
            dbc.Col(xs=10, children=[
                sd_material_ui.Card(
                    headerTitle="Graph",
                    expanded=True,
                    children=[dcc.Graph(id="live-update-graph")])
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
        print(run)
        return dict(start=run.start_datetime, end=run.end_datetime)
    return selected_time_interval


@app.callback(Output('param_selector', 'availableParams'),
              [Input('run_selector', 'selectedTimeInterval')])
def update_attrs(selected_time_interval):
    if selected_time_interval:
        start_dt = selected_time_interval["start"]
        end_dt = selected_time_interval["end"]
        time_filter = text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_attrs(start_dt, end_dt))))

        domains: List[str] = [d[0] for d in db.session.query(AttConf.domain) \
            .filter(time_filter).distinct()]

        result = {d: {} for d in domains}

        for domain in domains:
            families = [f[0] for f in db.session.query(AttConf.family)
                .filter(AttConf.domain == domain)
                .distinct()]
            result[domain] = {f: {} for f in families}

            for family in families:
                members = [f[0] for f in db.session.query(AttConf.member)
                    .filter(AttConf.domain == domain)
                    .filter(AttConf.family == family)
                    .distinct()]
                result[domain][family] = members
        return result
    return {}


@app.callback(Output('live-update-graph', 'figure'),
              [Input('param_selector', 'selectedParam')],
              (State('run_selector', 'selectedTimeInterval'),))
def draw_group(selected_param, selected_time_interval) -> go.Figure:
    if not selected_param or not selected_time_interval:
        return go.Figure(layout=go.Layout(
            height=500,
        ))

    start_dt = parse(selected_time_interval["start"])
    end_dt = parse(selected_time_interval["end"])
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
            title="{}/{}/{}".format(domain, family, member),
            xaxis=go.layout.XAxis(title='Acquisition Time'),
            height=500,
        )
    )


if __name__ == '__main__':
    app.run_server(debug=DEBUG, host=HOST, port=PORT)
