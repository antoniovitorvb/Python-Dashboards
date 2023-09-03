"""
LAYOUT 1
"""

import dash
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    'fruit': ['apples', 'oranges', 'bananas', 'apples', 'oranges', 'bananas'],
    'amount': [4, 1, 2, 2, 4, 5],
    'city': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})

fig = px.bar(
    df,
    x='fruit', y='amount', color='city'
)

# =============================
# Layout
from dash import html, dcc # Dash Code Components

app.layout = html.Div(id='div1',
    children=[
        html.H1('Hello Dash!', id='h1'),

        html.Div('Dash: Um framework web para Python'),

        dcc.Graph(figure=fig, id='graph1')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)