from dash import html, dcc

upload_component = html.Div([
    html.H3('Sube aquí tu archivo'),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Arrastra o selecciona un archivo']),
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
    html.Div(id='uploaded-file-info')
])