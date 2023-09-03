"""
CALLBACKS COM GRÁFICOS
"""

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.github.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children = [
        html.H3(
        'Callbacks em Gráficos!',
        style={'color': '#E6DFD8'}
        ),

        dcc.Graph(
            id='graph-with-slider'
        ),

        html.Label('Year Slider:'),
        dcc.Slider(
            id='year-slider',

            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'][round(len(df)/2)],

            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        )
])

# Espaço para Callbacks

"""
Output,
[Input],
[State]

Toda vez que houver uma alteração na Property 'value' de 'my-input'
isso será passado como parâmetro para a função update_output_div
e após executar essa função ele será passado para 'my-output'
"""
@app.callback( # Decorador
    Output(component_id='graph-with-slider', component_property='figure'),
    [Input(component_id='year-slider', component_property='value')],
    []
)
def update_figure(selected_year):
    # selected_year = 'value' from 'year-slider'
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(
        data_frame=filtered_df,
        x='gdpPercap', y='lifeExp',
        size='pop', color='continent', hover_name='country',
        log_x=True, size_max=55
    )
    fig.update_layout(transition_duration=500) # miliseconds

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)