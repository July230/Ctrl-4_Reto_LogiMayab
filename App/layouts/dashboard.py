from dash import html, dcc
import dash_bootstrap_components as dbc

tooltip = html.Div(
    [
        html.I(
            id='tooltip-target',
            className='bi bi-info-circle-fill me-2', 
            style={'margin-right': '0.5rem'},
        ),
        dbc.Tooltip(
            'Sube un archivo haciendo click o arrastrando aquí.',
            target='tooltip-target',
            style={'font-family': 'MuseoModerno'},
        ),
    ]
)

dashboard_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(
                'Dashboard', 
                style={'textAlign': 'left', 'font-family': 'MuseoModerno'}
            ),
            tooltip
        ],
        style={
            'display': 'flex',
            'alignItems': 'center',
            'gap': '0.5rem',
            'justifyContent': 'left',
            'width': '100%'
        }
        ),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    html.Div('Arrastra o selecciona un archivo', id='upload-box-content', style={'color': 'gray'})
                ]),
                multiple=False,
                style={
                    'width': '100%',
                    'minHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'textAlign': 'center',
                    'display': 'flex',
                    'flexDirection': 'column',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'padding': '0.5rem'
                }
            ),
            html.Br()
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        dcc.Dropdown(
                            id='month-filter',
                            placeholder='Filtrar por mes',
                            clearable=True,
                        )
                    ], id='month-filter-container'),
                    dcc.Graph(id='plot-1', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-2', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width=6)
    ]),


    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='plot-3', className='dashboard-graph')
                ])
            ], className='shadow-sm mb-3', style={'minHeight': '300px'})
        ], width=6),
        #dbc.Col([
            # Placeholder for a fourth plot to complete a 2x2 grid. Add a callback for 'plot-4' when available.
        #    dcc.Graph(id='plot-4', className='dashboard-graph')
        #], width=6)
    ])
])