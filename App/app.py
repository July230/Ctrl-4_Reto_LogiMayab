from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from layouts.sidebar import sidebar
from callbacks.callbacks_master import register_callbacks_all

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           suppress_callback_exceptions=True) # Permite callbacks en páginas no cargadas

# Store global para que todas las paginas usen el mismo archivo cargado
app.layout = dbc.Container([
    dcc.Store(id='stored-data', storage_type='memory'), # Almacena datos cargados
    dcc.Location(id='url', refresh=False), # Componente para manejar la URL
    sidebar,
    html.Div(id='page-content', style={'margin-left': '20rem', 'padding': '2rem'})
], fluid=True)

register_callbacks_all(app)

if __name__ == '__main__':
    app.run(debug=True)