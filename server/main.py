# -*- coding: utf-8 -*-
from typing import List, Union

import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sqlalchemy import text

from server import app, db
from server.config import DEBUG, PORT, HOST
from server.layout import layout
from server.orm.hdbpp import AttConf
from server.typings import DomainEntry, Style, ScatterPlots
from server.utils import _get_run, _get_run_attrs, initialize_domains, _get_attrs_for_params, get_values

app.layout = layout


@app.callback(Output('run-apply', 'disabled'),
              [Input('run-period', 'value'), Input('run-number', 'value')])
def run_apply_disabled(period, number) -> bool:
    return (period is None) or (number is None)


@app.callback([Output('curr-run-period', 'value'),
               Output('curr-run-number', 'value'),
               Output('notfound-warning', 'hidden')],
              [Input('run-apply', 'n_clicks_timestamp')],
              [State('run-period', 'value'),
               State('run-number', 'value')])
def apply_run_selection(
        apply_click_time: int, period: int, run: int) -> (Union[int, None], Union[int, None]):
    entry = _get_run(period, run)
    if entry:
        return period, run, True
    else:
        return None, None, period is None or run is None


@app.callback([Output('selected-run-view', 'style'),
               Output('run_info', 'children'),
               Output('domain-dropdown', 'options')],
              [Input('curr-run-period', 'value'),
               Input('curr-run-number', 'value')])
def apply_run_view(period: int, run: int) -> (Style, List[DomainEntry]):
    run_model = _get_run(period, run)

    if run_model:
        md = """
        Period number: {}
        
        Run number: {}
        
        Start time: {}
        
        End time: {}
        """.format(
            run_model.period_number,
            run_model.run_number,
            run_model.start_datetime,
            run_model.end_datetime
        )

        return {'display': 'inherit'}, md, initialize_domains(period, run)
    else:
        return {'display': 'none'}, None, []


@app.callback(Output('family-dropdown', 'options'),
              [Input('domain-dropdown', 'value')],
              [State('curr-run-period', 'value'),
               State('curr-run-number', 'value')])
def update_families(domain: str, period: int, run: int) -> List[DomainEntry]:
    if domain is None:
        return []

    query = db.session.query(AttConf.family) \
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_run_attrs(period, run))))) \
        .filter(AttConf.domain == domain) \
        .distinct()
    return [{'label': v[0], 'value': v[0]} for v in query]


@app.callback(Output('member-dropdown', 'options'),
              [Input('family-dropdown', 'value')],
              [State('domain-dropdown', 'value'),
               State('curr-run-period', 'value'),
               State('curr-run-number', 'value')])
def update_members(family: str, domain: str, period: int, run: int):
    if family is None:
        return []
    return [{'label': v[0], 'value': v[0]} for v in db.session.query(AttConf.member)
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_run_attrs(period, run)))))
        .filter(AttConf.family == family)
        .filter(AttConf.domain == domain)
        .distinct()]


@app.callback(Output('name-dropdown', 'options'),
              [Input('member-dropdown', 'value')],
              [State('family-dropdown', 'value'),
               State('domain-dropdown', 'value'),
               State('curr-run-period', 'value'),
               State('curr-run-number', 'value')])
def update_names(member: str, family: str, domain: str, period: int, run: int):
    if member is None:
        return []

    query = db.session.query(AttConf.name) \
        .filter(text("att_conf_id in ({})".format(", ".join(str(v) for v in _get_run_attrs(period, run))))) \
        .filter(AttConf.member == member) \
        .filter(AttConf.family == family) \
        .filter(AttConf.domain == domain) \
        .distinct()
    return [{'label': v[0], 'value': v[0]} for v in query]


@app.callback(Output('data-apply', 'disabled'),
              [Input('name-dropdown', 'value')])
def data_apply_disabled(name: str) -> bool:
    return name is None


@app.callback(Output('live-update-graph', 'figure'),
              [Input('data-apply', 'n_clicks')],
              [State('name-dropdown', 'value'),
               State('member-dropdown', 'value'),
               State('family-dropdown', 'value'),
               State('domain-dropdown', 'value'),
               State('curr-run-period', 'value'),
               State('curr-run-number', 'value')])
def draw_group(
        n_clicks: int, name: str, member: str, family: str, domain: str, period: int, run: int) -> go.Figure:
    if n_clicks is None:
        return go.Figure()

    attrs = _get_attrs_for_params(domain, family, member, name)

    data: ScatterPlots = []
    for attr in attrs:
        graphs_data = get_values(attr[0], attr[1], period, run)
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
            title="{}-{}-{}-{}".format(domain, family, member, name),
            xaxis=go.layout.XAxis(title='Acquisition Time'),
        )
    )


if __name__ == '__main__':
    app.run_server(debug=DEBUG, host=HOST, port=PORT)
