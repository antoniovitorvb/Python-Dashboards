# ========== DASH APP ========== #
import dash
from dash import Dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

load_figure_template('quartz')

app = Dash(__name__, external_stylesheets = [dbc.themes.QUARTZ])
server = app.server