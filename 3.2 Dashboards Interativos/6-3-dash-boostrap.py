"""
UTILIZANDO TEMAS DO DASH-BOOTSTRAP-COMPONENTS
"""
import os
from dash import Dash, Input, Output, html, dcc
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

cwd = os.path.dirname(os.path.realpath(__file__))

data = pd.read_csv(os.path.join(cwd, 'datasets/supermarket_sales.csv'))
data['Date'] = pd.to_datetime(data['Date'])


app = Dash(external_stylesheets = [dbc.themes.DARKLY])
server = app.server

# ========== LAYOUT ========== #
app.layout = html.Div(
    children = [
        html.H5('Cidades:'),
        dcc.Checklist(
            id='check_city',
            options=data['City'].sort_values().unique(),
            value=data['City'].sort_values().unique(),
            labelStyle={'display': 'inline-block'}
        ),

        html.H5('Variável de análise:'),
        dcc.RadioItems(
            id='radio_var',
            options=['gross income', 'Rating'],
            value='gross income',
            labelStyle={'display': 'inline-block'}
        ),

        dcc.Graph(id='city-fig'),
        dcc.Graph(id='pay-fig'),
        dcc.Graph(id='income-per-product-fig')
    ]
)



# ========== CALLBACKS ========== #
@app.callback(
    [
        Output(component_id='city-fig', component_property='figure'),
        Output(component_id='pay-fig', component_property='figure'),
        Output(component_id='income-per-product-fig', component_property='figure')
    ],

    [
        Input(component_id='check_city', component_property='value'),
        Input(component_id='radio_var', component_property='value')
    ]
)
def render_graph(cities, data_var):
    operation = np.sum if data_var == 'gross income' else np.mean

    filtered_data = data[data['City'].isin(cities)]
    data_city = filtered_data.groupby('City')[data_var].apply(operation).to_frame().reset_index()
    data_pay = filtered_data.groupby('Payment')[data_var].apply(operation).to_frame().reset_index()
    data_prod_income = filtered_data.groupby(['Product line', 'City'])[data_var].apply(operation).to_frame().reset_index()

    city_fig = px.bar(
        data_frame=data_city,
        x='City', y=data_var#, color='City'
    )
    city_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=400,
        template = 'plotly_dark'
    )

    pay_fig = px.bar(
        data_frame=data_pay,
        x=data_var, y='Payment', 
        orientation='h'#,color='City'
    )
    pay_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=200,
        template = 'plotly_dark'
    )

    prod_income_fig = px.bar(
        data_frame=data_prod_income,
        x=data_var, y='Product line',
        color='City', orientation='h', barmode='group'
    )
    prod_income_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=500,
        template = 'plotly_dark'
    )

    return city_fig, pay_fig, prod_income_fig



# ========== RUN SERVER ========== #
if __name__ == '__main__':
    app.run_server(debug=True)