from typing import List

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from server.config import INITIAL_RUN_PERIOD, INITIAL_RUN_NUMBER
from server.typings import DomainEntry

_navbar = dbc.NavbarSimple(
    brand="BM@N slow controls viewer",
    sticky="top",
)

_body = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Alert("Couldn't find run in database", color='warning')
            ])
        ]),
    ], id='notfound-warning', hidden=True),
    dbc.Row([
        dbc.Col([
            html.H3("Run selection")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Form([
                dbc.FormGroup([
                    dbc.Input(
                        id="run-period",
                        placeholder='Period',
                        type='number',
                        step=1, min=0,
                        value=INITIAL_RUN_PERIOD
                    )
                ]),
                dbc.FormGroup([
                    dbc.Input(
                        id="run-number",
                        placeholder='Number',
                        type='number',
                        step=1, min=0,
                        value=INITIAL_RUN_NUMBER
                    )
                ]),
                dbc.Button('apply', color='primary', id='run-apply',
                           disabled=True, n_clicks_timestamp='0'),
            ], inline=True),
        ])
    ]),
    html.Div([
        dbc.Row([
            dbc.Col([
                html.H3("Selected run info")
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Input(
                    id="curr-run-period",
                    type='number',
                    disabled=True,
                    value=None,
                    style={'display': 'none'}
                ),
                dcc.Input(
                    id="curr-run-number",
                    type='number',
                    disabled=True,
                    value=None,
                    style={'display': 'none'}
                ),
                dcc.Markdown(id='run_info')
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Form([
                    dbc.FormGroup([
                        # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
                        dcc.Dropdown(id='domain-dropdown', placeholder="domain", style={"width": 100})
                    ]),
                    dbc.FormGroup([
                        # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
                        dcc.Dropdown(id='family-dropdown', placeholder="domain", style={"width": 100})
                    ]),
                    dbc.FormGroup([
                        # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
                        dcc.Dropdown(id='member-dropdown', placeholder="domain", style={"width": 150})
                    ]),
                    dbc.FormGroup([
                        # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
                        dcc.Dropdown(id='name-dropdown', placeholder="domain", style={"width": 150})
                    ]),
                    dbc.Button('apply', color='primary', id='data-apply', disabled=True),
                ], inline=True),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='live-update-graph', animate=False)
            ], md=12)
        ]),
    ], id='selected-run-view', style={'display': 'none'})

], fluid=False)

layout = html.Div([
    _navbar, _body
])


def to_dropdown_items(entries: List[DomainEntry]) -> List[dbc.DropdownMenuItem]:
    return [
        dbc.DropdownMenuItem(entry['label'], key=entry['value']) for entry in entries]
