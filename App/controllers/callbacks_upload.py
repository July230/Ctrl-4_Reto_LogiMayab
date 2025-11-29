from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from models.file_loader import load_upload_file

def register_callbacks_upload(app):
    @app.callback(
        Output('uploaded-file-info', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'contents'),
    )
    def load_file(contents, filename):
        if contents:
            df = load_upload_file(contents, filename)
            return f'Archivo cargado: {filename}, filas: {len(df)}'
        return 'Ningún archivo cargado'