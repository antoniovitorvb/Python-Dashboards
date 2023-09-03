"""
LAYOUT 2
"""

import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Label('Dropdown'),
    dcc.Dropdown(
        id='dp-1',

        options=[ # cada option tem que ter um Label e um Value!
            {'label': 'Rio Grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Bahia', 'value': 'BA'},
        ],

        value='BA', # default
        style={'margin-bottom': '30px'}
    ),

    html.Label('Checklist'),
    dcc.Checklist(
        id='cl-1',

        options=[ # cada option tem que ter um Label e um Value!
            {'label': 'Rio Grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Bahia', 'value': 'BA'},
        ],

        value=['BA'], # Default de checklist tem que list
        style={'margin-bottom': '30px'}
    ),

    html.Label('Text input'),
    dcc.Input(
        value='Digita ae', 
        type='text',
        style={'margin-bottom': '30px'}
    ),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=10,
        value=5
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)