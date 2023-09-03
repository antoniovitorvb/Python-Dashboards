"""
COMPONENTES DE LAYOUT
"""
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# ========== LAYOUT ========== #
app.layout = html.Div([
    '''
    DBC divide o layout em 12 colunas. Caso não seja especificado pelo
    parâmetro [md] ele divide igualmente as 12 colunas entre os dbc.Col()
    ''',
    dbc.Row([
        dbc.Col(
            html.Div('Column'),
            style={'background': '#ff0000'},
            md = 6, # md -> Medium Display (Grid Options)
            sm = 8
        ),
        dbc.Col(html.Div('Column'), style={'background': '#00ff00'}, md = 1, sm = 2),
        dbc.Col(html.Div('Column'), style={'background': '#0000ff'}, md = 5, sm = 2),
    ])
])



# ========== RUN SERVER ========== #
if __name__ == '__main__':
    app.run_server(port = 8051, debug=True)