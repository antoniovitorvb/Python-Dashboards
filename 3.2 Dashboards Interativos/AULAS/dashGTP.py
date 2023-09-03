import dash
import dash_table
import pandas as pd
import urllib.request

# Download the dataset
url = 'https://plotly.github.io/datasets/country_indicators.csv'
filename = 'country_indicators.csv'
urllib.request.urlretrieve(url, filename)

# Load the dataset
df = pd.read_csv(filename)

# Create the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records')
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)