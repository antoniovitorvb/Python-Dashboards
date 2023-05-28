"""
CALLBACKS EM CADEIA
"""

import dash
from dash import Dash, html, dcc, Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options={
    'USA': ['Boston', 'NYC', 'San Francisco'],
    'Canada': ['Ottawa', 'Montreal', 'Toronto']
}

app.layout = html.Div([
    dcc.RadioItems(
        id='countries',
        options=list(all_options.keys()),
        value='USA'
    ),

    html.Hr(),
    dcc.RadioItems(id='cities'),
    html.Hr(),

    html.Div(id='display-selected-values')
])

"""
O primeiro callback servirá para qualquer alteração do input de 'countries'
Após a alteração do valor, o segundo callback irá alterar 'cities'
e a alteração em 'cities' irá mostrar o output em 'display-selected-values'
"""

# Cria lista de cidades de acordo com o Input de 'countries'
@app.callback(
    Output(component_id='cities', component_property='options'),
    Input(component_id='countries', component_property='value')
)
def city_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

# Pega a cidade selecionada das que foram disponibilizadas em city_options()
@app.callback(
    Output(component_id='cities', component_property='value'),
    Input(component_id='cities', component_property='options')
)
def city_value(available_options):
    return available_options[0]['value']

# Mostra os valores selecionados para 'countries' e 'cities'
@app.callback(
    Output(component_id='display-selected-values', component_property='children'),
    Input(component_id='countries', component_property='value'),
    Input(component_id='cities', component_property='value')
)
def display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(selected_city, selected_country)

if __name__ == '__main__':
    app.run_server(debug=True)