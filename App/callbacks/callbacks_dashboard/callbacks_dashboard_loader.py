from dash.dependencies import Input, Output, State
import pandas as pd
from utils.file_loader import load_upload_file

def register_callbacks_dashboard_loader(app):
    '''
    Registra los callbacks encargados de procesar y cargar archivos en el dashboard.

    Este registrador define los callbacks responsables de leer, validar y limpiar 
    los archivos cargados mediante `dcc.Upload`. Su resultado es almacenar el 
    DataFrame procesado en `dcc.Store` y mostrar información relevante al usuario.

    Parameters
    ----------
    app : dash.Dash
        Instancia principal de la aplicación Dash donde se registran
        todos los callbacks.
    Returns
    -------
    None

    '''
    @app.callback(
        Output('stored-data', 'data'),
        Output('uploaded-file-info', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
        prevent_initial_call=True
    )
    def load_file(contents, filename):
        '''
        Carga, procesa y limpia el archivo subido por el usuario.
        Esta función recibe los datos codificados en base64 desde dcc.Upload, 
        los decodifica mediante load_upload_file, convierte la columna "Importe" 
        a formato numérico y almacena el resultado en un formato serializado apto 
        para dcc.Store.

        Parameters
        ----------
        contents : str or None
            Cadena base64 generada por dcc.Upload, que contiene tanto los metadatos como el contenido del archivo. 
            Puede ser None si no se ha cargado ningún archivo.
        filename : str or None 
            Nombre del archivo original, utilizado para determinar su extensión.
        Será None si el componente no proporciona nombre.
        Returns
        -------
        tuple
            (data_serialized, message)
            data_serialized : list[dict] or None
                El DataFrame procesado convertido a formato records para ser almacenado.
                Devuelve None si ocurre un error o si el archivo carece de estructura válida.

            message : str
                Mensaje informativo sobre el estado de la carga del archivo, ya sea éxito,
                advertencia o error.
            
        '''

        if not contents:
            return None, 'Sube un archivo para iniciar.'

        try:
            df = load_upload_file(contents, filename)

            # Limpieza "Importe"
            if 'Importe' in df.columns:
                df['Importe'] = (
                    df['Importe'].astype(str)
                    .str.replace('$', '', regex=False)
                    .str.replace(',', '', regex=False)
                    .str.strip()
                )
                df['Importe'] = pd.to_numeric(df['Importe'], errors='coerce')
            else:
                return None, 'La columna "Importe" no existe.'

            return df.to_dict('records'), f'Archivo cargado: {filename}'

        except Exception as e:
            return None, f'Error: {e}'