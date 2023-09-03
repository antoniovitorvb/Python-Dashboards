import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

from app import *

def render_layout():
    register = dbc.Card([
        html.Legend('Register'),

        dbc.Input(id='user_register', placeholder='Username', type='text'),
        dbc.Input(id='pwd_register', placeholder='Password', type='text'),
        dbc.Input(id='email_register', placeholder='E-mail', type='text'),

        dbc.Button('Register!', id='register_button'),
        html.Span('', style={"text-align": "center"}),

        html.Div([
            html.Label('Or', style={'margin-right':'5px'}),
            dcc.Link('Login', href='/login')
        ], style={'padding': '20px', 'justify-content':'center', 'display':'flex'})

    ], className='login_card')
    return register