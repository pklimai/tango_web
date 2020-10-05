from typing import List
import datetime

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import sd_material_ui

import nica_dash_components

from server.config import INITIAL_RUN_PERIOD, INITIAL_RUN_NUMBER
from server.typings import DomainEntry
from server.utils import _get_available_runs

_navbar = dbc.NavbarSimple(
    brand="BM@N Slow Control Viewer (Tango Database)",
    sticky="top",
)


def make_timerange(
        start_datetime: datetime.datetime=datetime.datetime.now(),
        end_datetime: datetime.datetime=datetime.datetime.now()):
    return [
            dbc.Input(
                id="start-date",
                type='date',
                disabled=False,
                value=start_datetime.date()
            ),
            dbc.Input(
                id="start-time",
                type='time',
                disabled=False,
                value="{}:{}".format(
                    start_datetime.time().hour,
                    start_datetime.time().minute)
            ),
            dbc.Label(" - "),
            dbc.Input(
                id="end-date",
                type='date',
                disabled=False,
                value=end_datetime.date()
            ),
            dbc.Input(
                id="end-time",
                type='time',
                disabled=False,
                value="{}:{}".format(
                    end_datetime.time().hour,
                    end_datetime.time().minute + 1)
            )
        ]


# def make_body(runs: List[int]):
#
#     return dbc.Container([
#         html.Div([
#             dbc.Row([
#                 dbc.Col([
#                     dbc.Alert("Couldn't find run in database", color='warning')
#                 ])
#             ]),
#         ], id='notfound-warning', hidden=True),
#         dbc.Row([
#             dbc.Col([
#                 html.H3("Run Selector")
#             ])
#         ]),
#         dbc.Row([
#             dbc.Col([
#                 dbc.Form([
#                     dbc.FormGroup([
#                         dcc.Dropdown(
#                             id="run-period",
#                             placeholder="Period",
#                             options=[
#                                 {"label": run, "value": run}
#                                 for run in runs],
#                             value=None,
#                             style={"width": 150}
#                         ),
#                         dbc.Input(
#                             id="run-number",
#                             placeholder='Number',
#                             type='number',
#                             step=1, min=0,
#                             value=INITIAL_RUN_NUMBER
#                         ),
#                         dbc.Button('get run time range', id='run-apply',
#                                    disabled=True, n_clicks_timestamp='0'),
#                     ]),
#                 ], inline=True),
#             ])
#         ]),
#         dbc.Row([
#             dbc.Col([
#                 html.H3("Time Range")
#             ])
#         ]),
#         dbc.Row([
#             dbc.Col([
#                 dbc.Form([
#                     dbc.FormGroup(make_timerange(), id="time-range-formgroup"),
#                     dbc.Button('apply', id='datetime-apply',
#                                disabled=False, n_clicks_timestamp=0),
#                 ], inline=True),
#             ])
#         ]),
#         html.Div([
#             dbc.Row([
#                 dbc.Col([
#                     html.H3("Selected Data")
#                 ])
#             ]),
#             dbc.Row([
#                 dbc.Col([
#
#                     dcc.Input(
#                         id="curr-start-datetime",
#                         type='text',
#                         disabled=True,
#                         value=None,
#                         style={'display': 'none'}
#                     ),
#                     dcc.Input(
#                         id="curr-end-datetime",
#                         type='text',
#                         disabled=True,
#                         value=None,
#                         style={'display': 'none'}
#                     ),
#                     dcc.Markdown(id='run_info')
#                 ]),
#             ]),
#             dbc.Row([
#                 dbc.Col([
#                     dbc.Form([
#                         dbc.FormGroup([
#                             # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
#                             dcc.Dropdown(id='domain-dropdown', placeholder="domain", style={"width": 100})
#                         ]),
#                         dbc.FormGroup([
#                             # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
#                             dcc.Dropdown(id='family-dropdown', placeholder="family", style={"width": 100})
#                         ]),
#                         dbc.FormGroup([
#                             # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
#                             dcc.Dropdown(id='member-dropdown', placeholder="member", style={"width": 150})
#                         ]),
#                         dbc.FormGroup([
#                             # dbc.DropdownMenu(id='domain-dropdown', label='Domain'),
#                             dcc.Dropdown(id='name-dropdown', placeholder="name", style={"width": 150})
#                         ]),
#                         dbc.Button('apply', id='data-apply', disabled=True),
#                     ], inline=True),
#                 ]),
#             ]),
#             dbc.Row([
#                 dbc.Col([
#                     dcc.Graph(id='live-update-graph', animate=False)
#                 ], md=12)
#             ]),
#         ], id='selected-run-view', style={'display': 'none'})
#
#     ], fluid=False)


def make_layout(runs: List[int]):

    return dbc.Container(fluid=1, children=[
        dbc.Row([
            dbc.Col(xs=2, children=[
                nica_dash_components.RunSelector(availableRuns=_get_available_runs())
            ]),
            dbc.Col(xs=10, children=[
                sd_material_ui.Card(
                    headerTitle="Graph",
                    expanded=True,
                    children=[dcc.Graph(

                    )]
            )
            ]),
        ])
    ])


def to_dropdown_items(entries: List[DomainEntry]) -> List[dbc.DropdownMenuItem]:
    return [
        dbc.DropdownMenuItem(entry['label'], key=entry['value']) for entry in entries]
