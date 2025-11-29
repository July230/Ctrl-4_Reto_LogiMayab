from dash import Dash
import dash_bootstrap_components as dbc
from views.dashboard import layout
from controllers.callbacks_master import register_callbacks_all

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout

register_callbacks_all(app)

if __name__ == '__main__':
    app.run(debug=True)