from dash import html
from .components_upload import upload_component

layout = html.Div([
    html.H1('Dashboard interactivo'),
    upload_component,
])