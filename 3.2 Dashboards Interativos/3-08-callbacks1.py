"""
CALLBACKS 1
"""

import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children = [
    html.H4(
        'Altere o valor abaixo para ver o callback em ação!',
        style={'color': '#E6DFD8'}
    ),
    html.Div([
        'Entrada:   ',
        dcc.Input(
            id='my-input',
            value='Valor Inicial',
            type='text'
        )
    ]),
    html.Br(),

    html.Output(id='my-output') #
])

# Espaço para Callbacks

"""
[Outputs],
[Inputs],
[State]

Toda vez que houver uma alteração na Property 'value' de 'my-input'
isso será passado como parâmetro para a função update_output_div
e após executar essa função ele será passado para 'my-output'
"""
@app.callback( # Decorador
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')],
    []
)
def update_output_div(value):
    return 'Saída: {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)