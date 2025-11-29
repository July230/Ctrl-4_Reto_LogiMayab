from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from models.file_loader import load_upload_file

def register_callbacks_upload(app):
    '''
    Registra los callbacks relacionados con la carga de archivos en la aplicación Dash.

    El resultado (nombre del archivo y número de filas) se muestra en el componente
    'uploaded-file-info'.

    Args:
        app (Dash): Instancia principal de la aplicación Dash donde se registran los callbacks.

    Returns:
        None
    '''
    @app.callback(
        Output('uploaded-file-info', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
    )
    def load_file(contents, filename):
        '''
        Callback que procesa un archivo subido por el usuario mediante dcc.Upload.

        Args:
            contents (str | None): Cadena base64 generada por dcc.Upload, que contiene
                tanto los metadatos como el contenido del archivo. Puede ser None si no
                se ha cargado ningún archivo.
            filename (str | None): Nombre original del archivo subido. Usado para
                determinar la extensión y el formato. Puede ser None si no se proporciona.
        
        Returns:
            str: Mensaje para mostrar en la interfaz indicando éxito o error al cargar
            el archivo.

        Raises:
            PreventUpdate: Cuando contents o filename son None, evitando que el
                callback actualice la interfaz.

        '''
        if contents is None or filename is None:
            raise PreventUpdate
        try:
            df = load_upload_file(contents, filename)
            return f'Archivo cargado: {filename}, filas: {len(df)}'
        except Exception as e:
            return f"Error al cargar archivo: {str(e)}"