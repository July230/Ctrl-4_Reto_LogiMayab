from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Img(src='/assets/img/icono-logi-mayab.png', className='sidebar-logo', alt='Logo'),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className='bi bi-house-door-fill', style={'margin-right': '0.5rem'}),
                        html.Span('Dashboard')
                    ],
                    href='/dashboard',
                    className='nav-link'
                ),
                dbc.NavLink(
                    [
                        html.I(className='bi bi-truck', style={'margin-right': '0.5rem'}),
                        html.Span('Rutas')
                    ],
                    href='/rutas',
                    className='nav-link'
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar'
)