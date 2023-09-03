from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
# os.system('pip install dash-auth==2.0.0')
import dash_auth

from dash_bootstrap_templates import load_figure_template
load_figure_template(['quartz'])

app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])
server = app.server

user = {'av':'123'}
auth = dash_auth.BasicAuth(app=app, username_password_list=user)

# ========== LAYOUT ========== #
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

app.layout = html.Div([
    dbc.Card([
        dcc.Graph(figure=fig)
    ], style=card_style)
],
style={'position':'absolute','top':'50%', 'left':'50%',
       'transform':'translate(-50%, -50%)'})

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)