import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

# Load the data set from the provided link
url = 'https://plotly.github.io/datasets/country_indicators.csv'
df = pd.read_csv(url)

# Create the Dash app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([
    html.H1('Country Indicators Dashboard'),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Country Name'].unique()],
        value='United States'
    ),
    html.Div([
        dcc.Graph(id='indicator-graph'),
        dcc.Graph(id='map-graph'),
    ], className='row'),
])

# Define the callback function for the graphs
@app.callback(
    [dash.dependencies.Output('indicator-graph', 'figure'),
     dash.dependencies.Output('map-graph', 'figure')],
    [dash.dependencies.Input('country-dropdown', 'value')])
def update_graph(selected_country):
    filtered_df = df[df['Country Name'] == selected_country]
    trace1 = {
        'x': filtered_df['Year'],
        'y': filtered_df['CO2 emissions (kt)'],
        'type': 'scatter',
        'name': 'CO2 emissions'
    }
    trace2 = {
        'x': filtered_df['Year'],
        'y': filtered_df['Population, total'],
        'type': 'scatter',
        'name': 'Population'
    }
    # Create a map of the selected country using plotly.graph_objects
    map_data = filtered_df[['Country Code', 'Latitude', 'Longitude']].drop_duplicates()
    map_fig = go.Figure(go.Scattermapbox(
        lat=map_data['Latitude'],
        lon=map_data['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10,
            color='rgb(255, 0, 0)',
        ),
        text=map_data['Country Code'],
    ))
    map_fig.update_layout(
        hovermode='closest',
        mapbox=dict(
            accesstoken='your_mapbox_token',
            center=dict(
                lat=filtered_df['Latitude'].iloc[0],
                lon=filtered_df['Longitude'].iloc[0],
            ),
            zoom=4,
        ),
    )
    return (
        {
            'data': [trace1, trace2],
            'layout': {
                'title': f'{selected_country} Indicators',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Value'}
            }
        },
        map_fig,
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
