from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.H2('Menú', className='sidebar-title'),
        html.Hr(),
        html.P('A simple sidebar layout with navigation links', className='lead'),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className='bi bi-house-door-fill', style={'margin-right': '0.5rem'}),
                        html.Span('Dashboard')
                    ],
                    href='/dashboard',
                    active='exact',
                    className='nav-link'
                ),
                dbc.NavLink(
                    [
                        html.I(className='bi bi-file-earmark', style={'margin-right': '0.5rem'}),
                        html.Span('Otra Página')
                    ],
                    href='/otra-pagina',
                    active='exact',
                    className='nav-link'
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar'
)