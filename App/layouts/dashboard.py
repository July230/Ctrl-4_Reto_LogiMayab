from dash import html, dcc
import dash_bootstrap_components as dbc

dashboard_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Dashboard', style={'textAlign': 'left', 'font-family': 'MuseoModerno'}),
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Arrastra o selecciona un archivo'
                ]),
                multiple=False,
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'textAlign': 'center'
                }
            ),
            html.Br(),
            html.Div(id='uploaded-file-info', style={'color': 'gray'})
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='plot-1', className='dashboard-graph')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='plot-2', className='dashboard-graph')
        ], width=6)
    ]),


    dbc.Row([
        dbc.Col([
            dcc.Graph(id='plot-3', className='dashboard-graph')
        ], width=6),
        #dbc.Col([
            # Placeholder for a fourth plot to complete a 2x2 grid. Add a callback for 'plot-4' when available.
        #    dcc.Graph(id='plot-4', className='dashboard-graph')
        #], width=6)
    ])
])