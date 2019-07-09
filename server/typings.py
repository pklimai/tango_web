# coding: utf-8
from typing import List

import plotly.graph_objs as go
from mypy_extensions import TypedDict

ScatterPlots = List[go.Scatter]
Style = TypedDict('Style', {'display': str})
DomainEntry = TypedDict('DomainEntry', {'label': str, 'value': int})