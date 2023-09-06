"""
PLANEJAMENTO DE LAYOUT
"""
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# ========== LAYOUT ========== #
card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
] 

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                card_content, color='primary', inverse=True,
                style={'height': '80vh',
                       'margin': '10px'}
            )
        ],
        sm = 4),

        dbc.Col([
            dbc.Row([
                dbc.Col([dbc.Card(card_content, color='info', inverse=False)]),
                dbc.Col([dbc.Card(card_content, color='info', inverse=False)])
            ],
            style={'margin-bottom':'10px'}
            ),
            
            dbc.Row([
                dbc.Col([dbc.Card(card_content, color='warning', inverse=False)]),
                dbc.Col([dbc.Card(card_content, color='error', inverse=False)]),
                dbc.Col([dbc.Card(card_content, color='warning', inverse=False)])
            ])
        ],
        style={'margin':'10px'}),
    ])
])

# ========== RUN SERVER ========== #
if __name__ == '__main__':
    app.run_server(port = 8051, debug=True)