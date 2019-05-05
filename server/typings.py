# coding: utf-8
from typing import List

import plotly.graph_objs as go
from mypy_extensions import TypedDict

ScatterPlots = List[go.Scatter]
RunEntry = TypedDict('RunsList', {'label': str, 'value': int})