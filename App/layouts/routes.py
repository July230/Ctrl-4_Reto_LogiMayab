from dash import html, dcc
import dash_bootstrap_components as dbc

routes_content = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1('Rutas', style={'textAlign': 'left', 'font-family': 'MuseoModerno'}),
            html.P('Contenido para la página de rutas')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-routes-1', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width=6),
    ]),
])