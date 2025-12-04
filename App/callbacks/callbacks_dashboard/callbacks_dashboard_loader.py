from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from utils.file_loader import load_upload_file
import pandas as pd
import numpy as np

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

            # Limpieza de variables
            df['SubTotal'] = df['SubTotal'].replace(r'[\$, ]', '', regex=True).astype(float)
            df['IVA'] = df['IVA'].replace(r'[\$, ]', '', regex=True).astype(float)
            df['Retención'] = df['Retención'].replace(r'[\$, ]', '', regex=True).astype(float)
            df['Total'] = df['Total'].replace(r'[\$, ]', '', regex=True).astype(float)
            df['Liquidación'] = df['Liquidación'].replace(r'[\$, ]', '', regex=True).astype(float)
            df['Peso Kgs'] = df['Peso Kgs'].str.replace(',', '', regex=False).astype(float)
            df['Peso Descarga Kgs'] = df['Peso Descarga Kgs'].str.replace(',', '', regex=False).astype(float)
            df['Diferencia'] = df['Diferencia'].str.replace(',', '', regex=False).astype(float)
            df['Fecha'] = pd.to_datetime(df['Fecha'],format='mixed',dayfirst=False)
            df['Fecha.1'] = pd.to_datetime(df['Fecha.1'],format='mixed',dayfirst=False)
            df['Fecha Vencimiento'] = df['Fecha Vencimiento'].str.replace(r'/\d{4}$', '/2025', regex=True)
            df['Fecha Vencimiento'] = pd.to_datetime(df['Fecha Vencimiento'],format='mixed',dayfirst=False)

            df = df.rename(columns={'Numero':'Cliente'})

            # Eliminar duplicados
            df_sindupes = df.drop_duplicates(keep='first')

            df_cleaned = df_sindupes.copy()

            # Eliminar columnas innecesarias
            columns_to_drop = ['Nombre Cliente',
                                   'Diferencia',
                                   'Liquidación',
                                   'Dolly',
                                   'Remolque 2',
                                   'Operador',
                                   'Peso Kgs',
                                   'Peso Descarga Kgs',
                                   'Moneda',
                                   'Viaje Docto',
                                   'Fecha.1',
                                   'Fecha Vencimiento',
                                   'Remolque 1',
                                   'Fecha Salida',
                                   'Fecha Llegada',
                                   'Estatus de Viaje',
                                   'Retención',
                                   'Factura',
                                   'SubTotal',
                                   'IVA',
                                   'Viaje Docto',
                                   'Operador',
                                   'Documentos',
                                   'UUID CP',
                                   'Nro Ope']

            df_cleaned = df.drop(columns=columns_to_drop)

            # Imputación de valores faltantes
            df_cleaned['Tractocamión'] = df_cleaned['Tractocamión'].fillna('Desconocido')

            # Transformación de la columna 'Total'
            df_cleaned['Total_log'] = np.log1p(df_cleaned['Total'])

            return df_cleaned.to_json(date_format='iso', orient='records'), f'Archivo cargado: {filename}, filas: {len(df)}'

        except Exception as e:
            return None, f'Error: {e}'