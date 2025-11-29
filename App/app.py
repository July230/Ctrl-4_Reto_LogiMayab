from dash import Dash
import dash_bootstrap_components as dbc
from views.layout_main import layout
from controllers.callbacks_upload import register_callbacks_upload

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout

register_callbacks_upload(app)

if __name__ == '__main__':
    app.run(debug=True)