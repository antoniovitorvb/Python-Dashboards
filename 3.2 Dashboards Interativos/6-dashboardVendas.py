"""
PROJETO DE VENDAS EM SUPERMERCADOS
"""
import os
from dash import Dash, Input, Output, html, dcc
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

cwd = os.path.dirname(os.path.realpath(__file__))

data = pd.read_csv(os.path.join(cwd, 'datasets/supermarket_sales.csv'))
data['Date'] = pd.to_datetime(data['Date'])

load_figure_template('minty')

app = Dash(external_stylesheets=[dbc.themes.MINTY])
server = app.server

# ========== LAYOUT ========== #
app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2('SALES', style={'font-family':'AirStrip Four', 'font-size':'60px'}),
                html.H5('Cidades:'),
                dcc.Checklist(
                    id='check_city',
                    options=data['City'].sort_values().unique(),
                    value=data['City'].sort_values().unique(),
                    inputStyle={'margin-right':'10px', 'margin-left':'10px'}
                ),

                html.H5('Variável de análise:', style={'margin-top':'30px'}),
                dcc.RadioItems(
                    id='radio_var',
                    options=['gross income', 'Rating'],
                    value='gross income',
                    labelStyle={'display': 'inline-block'},
                    inputStyle={'margin-right':'10px', 'margin-left':'10px'}
                )
            ], 
            style={'height':'90vh',
                   'margin':'20px',
                   'padding':'20px'})
        ], sm=2),

        dbc.Col([
            dbc.Row([
                dbc.Col([dcc.Graph(id='city-fig')],
                        sm = 4, style={'height':'30vh'}),

                dbc.Col([dcc.Graph(id='gender-fig')],
                        sm = 4, style={'height':'30vh'}),

                dbc.Col([dcc.Graph(id='pay-fig')],
                        sm = 4, style={'height':'30vh'})
            ]),

            dbc.Row([dcc.Graph(id='income-per-date-fig')]),
            
            dbc.Row([dcc.Graph(id='income-per-product-fig')]),

            
        ],
        style={'padding':'20px'},
        sm = 10)
    ])
])



# ========== CALLBACKS ========== #
@app.callback(
    [
        Output(component_id='city-fig', component_property='figure'),
        Output(component_id='gender-fig', component_property='figure'),
        Output(component_id='pay-fig', component_property='figure'),
        Output(component_id='income-per-date-fig', component_property='figure'),
        Output(component_id='income-per-product-fig', component_property='figure')
    ],

    [
        Input(component_id='check_city', component_property='value'),
        Input(component_id='radio_var', component_property='value')
    ]
)
def render_graph(cities, data_var):
    # cities = data['City'].sort_values().unique()
    # data_var = 'gross income'

    operation = np.sum if data_var == 'gross income' else np.mean

    filtered_data = data[data['City'].isin(cities)]
    data_city = filtered_data.groupby('City')[data_var].apply(operation).to_frame().reset_index()
    data_gender = filtered_data.groupby(['Gender', 'City'])[data_var].apply(operation).to_frame().reset_index()
    data_pay = filtered_data.groupby('Payment')[data_var].apply(operation).to_frame().reset_index()
    data_date_income = filtered_data.groupby('Date')[data_var].apply(operation).to_frame().reset_index()
    data_prod_income = filtered_data.groupby(['Product line', 'City'])[data_var].apply(operation).to_frame().reset_index()

    city_fig = px.bar(
        data_frame=data_city,
        x='City', y=data_var#, color='City'
    )
    city_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=200
    )

    gender_fig = px.bar(
        data_frame=data_gender,
        x='Gender', y=data_var, color='City', barmode='group'
    )
    gender_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=200
    )

    pay_fig = px.bar(
        data_frame=data_pay,
        x=data_var, y='Payment', 
        orientation='h'#,color='City'
    )
    pay_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=200
    )

    date_income_fig = px.bar(
        data_frame=data_date_income,
        x='Date', y=data_var, barmode='group'
    )
    date_income_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=250
    )

    prod_income_fig = px.bar(
        data_frame=data_prod_income,
        x=data_var, y='Product line',
        color='City', orientation='h', barmode='group'
    )
    prod_income_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        # height=500
    )

    return city_fig, gender_fig, pay_fig, date_income_fig, prod_income_fig



# ========== RUN SERVER ========== #
if __name__ == '__main__':
    app.run_server(debug=True)