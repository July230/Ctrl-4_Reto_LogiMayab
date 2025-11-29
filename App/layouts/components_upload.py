from dash import html, dcc

upload_component = html.Div([
    html.H3('Sube aquí tu archivo'),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Arrastra o selecciona un archivo']),
        multiple=False
    ),
    html.Div(id='uploaded-file-info')
])