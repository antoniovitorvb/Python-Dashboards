import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from app import *
from pages import login, register, data

# ========== LAYOUT ========== #
app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='base-url', refresh=False),
            html.Div(id='page-content', style={'display':'flex', 'justify-content':'center'})
        ])
    ])
], fluid=True)

# ========== CALLBACKS ========== #
@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='base-url', component_property='pathname')
)
def render_page_content(pathname):
    if (pathname == '/login' or pathname == '/'):
        return login.render_layout()
    
    if pathname == '/register':
        return register.render_layout()
    
    if pathname == '/data':
        return data.render_layout('av')
    


# ========== RUN SERVER ========== #
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)