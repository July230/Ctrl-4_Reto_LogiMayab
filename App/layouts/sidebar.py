from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.H2("Menú", className="sidebar-title"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink('Dashboard', href='/dashboard', active='exact'),
                dbc.NavLink('Otra Página', href='/otra-pagina', active='exact'),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "width": "18rem",
        "padding": "2rem",
        "background-color": "#f8f9fa",
        "height": "100vh",
        "position": "fixed",
        "top": 0,
        "left": 0
    }
)