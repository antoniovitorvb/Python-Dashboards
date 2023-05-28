"""
CUSTOMIZAÇÃO DO LAYOUT
"""

import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc

"""
Para editar o layout da aplicação existem 3 formas:

1) Buscar estilo padrão achado na internet
"""
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

"""
2) usar a pasta 'assets'
"""
app = dash.Dash(__name__)

app.layout = html.Div(id='div1',
    children=[
        html.H1('Hello Dash!', id='h1'),

        html.Div('Dash: Um framework web para Python'),
    ]
)

"""
3) Editar o atributo 'style' dentro do app.layout
"""
app1 = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app1.layout = html.Div(id='div2',
    children=[
        html.H1('Hello Dash!', id='h1', style={'color': '#202444'}),

        html.Div('Dash: Um framework web para Python'),
    ],
    style={'background-color': '#E6DFD8'}
)

if __name__ == '__main__':
    # app.run_server(debug=True)
    app1.run_server(debug=True)