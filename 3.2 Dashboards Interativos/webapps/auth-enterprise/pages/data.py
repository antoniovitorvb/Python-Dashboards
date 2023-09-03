import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
import numpy as np
import plotly.express as px

from app import *
from pages import login, register

load_figure_template('quartz')

card_style = {
    'width': '800px',
    'min-height': '300px',
    'padding': '25px',
    'aligh-self': 'center'
}

df = pd.DataFrame(
    np.random.randn(100,1) + np.arange(100).reshape(100, 1),
    columns=['data']
)

fig = px.line(
    data_frame = df,
    x = df.index, y = 'data',
    template = 'quartz'
)

def render_layout(username):
    template = dbc.Card([
        dcc.Location(id='data-url'),
        html.Legend(f"Olá, {username}"),
        dcc.Graph(figure=fig),

        html.Div([
            dbc.Button('Logout', id='logout_button')
        ], style={'padding':'20px', 'justify-content':'end', 'display':'flex'})
    ], style=card_style, className='align-self-center')

    return template