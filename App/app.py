from dash import Dash, dcc
import dash
import dash_bootstrap_components as dbc
from layouts.dashboard import layout
from callbacks.callbacks_master import register_callbacks_all

app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP])

# Store global para que todas las paginas usen el mismo archivo cargado
app.layout = dbc.Container([
    dcc.Store(id='stored-data', storage_type='memory'),
    dash.page_container,
], fluid=True)

register_callbacks_all(app)

if __name__ == '__main__':
    app.run(debug=True)