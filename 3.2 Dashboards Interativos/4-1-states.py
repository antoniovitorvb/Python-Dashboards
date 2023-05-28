"""
USO DE STATES
"""

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input1', type='text', value='Montreal'),
    dcc.Input(id='input2', type='text', value='Toronto'),

    html.Button(
        id='submit-button', n_clicks=0, children='Submit',
        style={'background-color': '#E6DFD8'}
    ),

    html.Div(id='number-output')
])

"""
State serve para segurar alterações nos callbacks
até que uma condição para o State seja cumprida.
(ideal para formulários e logins)
"""

@app.callback(
    Output(component_id='number-output', component_property='children'),
    # Input(component_id='input1', component_property='value'),
    # Input(component_id='input2', component_property='value'),

    Input(component_id='submit-button', component_property='n_clicks'),
    State(component_id='input1', component_property='value'),
    State(component_id='input2', component_property='value')
)
def update_output(n_clicks, input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)

if __name__ == '__main__':
    app.run_server(debug=True)