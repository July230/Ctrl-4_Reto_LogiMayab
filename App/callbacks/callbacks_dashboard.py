from dash.dependencies import Input, Output, State
from dash import html, dcc
import pandas as pd
import plotly.express as px
from utils.file_loader import load_upload_file

def register_callbacks_dashboard_graph(app):
    '''
    Genera todas las gráficas y elementos del dashboard
    Args:
        app (Dash): Instancia principal de la aplicación Dash donde se registran
            todos los callbacks.
    Returns:
        None
    '''
    @app.callback(
        Output('our-plot', 'figure'),
        Output('uploaded-file-info', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
        prevent_initial_call=True
    )
    def update_graph(contents, filename):
        '''
        Obtiene el dataframe y genera los gráficos y elementos del dashboard
        Args:
            contents (str | None): Cadena base64 generada por dcc.Upload, que contiene
                tanto los metadatos como el contenido del archivo. Puede ser None si no
                se ha cargado ningún archivo.
            filename (str | None): Nombre original del archivo subido. Usado para
                determinar la extensión y el formato. Puede ser None si no se proporciona.
        Returns:
            fig: Gráfico generado usando plotly
            str:
            
        '''
        if not contents:
            return "Sube un archivo para generar la gráfica."

        try:
            df = load_upload_file(contents, filename)

            if 'Importe' in df.columns:
                df['Importe'] = (
                    df['Importe']
                    .astype(str)
                    .str.replace('$', '', regex=False)
                    .str.replace(',', '', regex=False)
                    .str.strip()
                )
                df['Importe'] = pd.to_numeric(df['Importe'], errors='coerce')
            else:
                return {}, "La columna 'Importe' no existe en el archivo."

            fig = px.box(df, x='Importe', title='Boxplot de los importes periodo Enero-Noviembre')

            return fig, f'Archivo cargado: {filename}, filas: {df.shape[0]}, columnas: {df.shape[1]}'

        except Exception as e:
            return f'Error generando gráfica: {e}'
