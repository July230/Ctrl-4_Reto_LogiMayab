from dash.dependencies import Input, Output, State
import pandas as pd
from dash.exceptions import PreventUpdate
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
        State('stored-data', 'data'),
        prevent_initial_call=True
    )
    def load_file(contents, filename, stored_data):
        '''
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
        stored_data : JSON or None
            Datos previamente almacenados en dcc.Store en formato JSON. 
            Puede ser None si no hay datos previos.
        Returns
        -------
        tuple
            (data_serialized, message)
            data_serialized : JSON or None
                El DataFrame procesado convertido a formato json para ser almacenado.
                Devuelve None si ocurre un error o si el archivo carece de estructura válida.

            message : str
                Mensaje informativo sobre el estado de la carga del archivo, ya sea éxito,
                advertencia o error.
            
        '''

        # Si NO hay un archivo nuevo y SÍ hay datos previos, no tocar nada
        if not contents and stored_data is not None:
            print('No hay nuevo archivo, pero sí datos previos. Manteniendo estado.')
            raise PreventUpdate
        
        # Si no hay archivo y tampoco había datos previos, pedir archivo
        if not contents:
            return None, 'Ningún archivo cargado.'

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

            return df.to_json(date_format='iso', orient='records'), f'Archivo cargado: {filename}, filas: {len(df)}'

        except Exception as e:
            return None, f'Error: {e}'