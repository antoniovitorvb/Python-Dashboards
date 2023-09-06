"""
CALLBACKS COM MÚLTIPLOS INPUTS
"""

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

available_indicators = df['Indicator Name'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='x_axis-col',
            options=[
                {'label': i, 'value': i} for i in available_indicators
            ],
            value='Fertility rate, total (births per woman)'
        ),

        dcc.RadioItems(
            id='x_axis-type',
            options=[
                {'label': i, 'value': i} for i in ['Linear', 'Log']
            ],
            value='Linear',
            labelStyle={'display': 'inline-block'}
        )
        ],
        style={'width': '48%', 'display': 'inline-block'}
    ),

    html.Div([
        dcc.Dropdown(
            id='y_axis-col',
            options=[
                {'label': i, 'value': i} for i in available_indicators
            ],
            value='Life expectancy at birth, total (years)'
        ),

        dcc.RadioItems(
            id='y_axis-type',
            options=[
                {'label': i, 'value': i} for i in ['Linear', 'Log']
            ],
            value='Linear',
            labelStyle={'display': 'inline-block'}
        )
        ],
        style={'width': '48%', 'display': 'inline-block', 'float': 'right'}
    ),

    dcc.Graph(id='indicator-graph'),

    dcc.Slider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'][round(len(df)/2)],

        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
    )
])

# CALLBACK SPACE
@app.callback(
    Output(component_id='indicator-graph', component_property='figure'),

    [Input(component_id='x_axis-col', component_property='value'),
    Input(component_id='x_axis-type', component_property='value'),
    Input(component_id='y_axis-col', component_property='value'),
    Input(component_id='y_axis-type', component_property='value'),
    Input(component_id='year-slider', component_property='value')
    ]
)
def update_graph(
    x_axis_col, x_axis_type,
    y_axis_col, y_axis_type,
    selected_year):

    filter_df = df[df['Year'] == selected_year]

    fig = px.scatter(
        x=filter_df[filter_df['Indicator Name'] == x_axis_col]['Value'],
        y=filter_df[filter_df['Indicator Name'] == y_axis_col]['Value'],
        hover_name=filter_df[filter_df['Indicator Name'] == y_axis_col]['Country Name']
    )

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r':0},
        hovermode='closest'
    )

    fig.update_xaxes(
        title = x_axis_col,
        type = 'linear' if x_axis_type == 'Linear' else 'log'
    )

    fig.update_yaxes(
        title = y_axis_col,
        type = 'linear' if y_axis_type == 'Linear' else 'log'
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)