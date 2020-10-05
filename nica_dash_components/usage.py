import nica_dash_components
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    nica_dash_components.RunSelector(id="input", availableRuns=[
    {
     "number": 1,
     "periods": [1,2,3]
    }, {
     "number": 2,
     "periods": [1,2,3]
    }]),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'selectedRun'), Input('input', 'selectedTimeInterval')])
def display_output(selectedRun, selectedTimeInterval):
    return 'You have entered run = {}; time range = {}'.format(selectedRun, selectedTimeInterval)


if __name__ == '__main__':
    app.run_server(debug=True)
