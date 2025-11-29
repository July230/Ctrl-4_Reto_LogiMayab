from dash import html, dcc
from .components_upload import upload_component

layout = html.Div([
    html.H1('Dashboard interactivo'),
    upload_component,
    html.Hr(),
    html.Div(id='graph-container')
])