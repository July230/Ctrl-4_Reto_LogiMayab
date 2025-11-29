from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from utils.file_loader import load_upload_file

def register_callbacks_dashboard_plots(app):
    '''
    Registra los callbacks encargados de generar las gráficas del dashboard.
    Este registrador define los callbacks relacionados con la creación 
    y actualización de los gráficos basados en los datos almacenados en 
    el componente dcc.Store.

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
        Output('plot-1', 'figure'),
        Input('stored-data', 'data'),
        prevent_initial_call=True
    )
    def update_plot(stored_df):
        '''
        Genera y actualiza la figura principal del dashboard a partir de los datos cargados.

        Toma la información almacenada en dcc.Store (formato dict) y la convierte en un 
        DataFrame de pandas. Luego genera un boxplot de la columna 'Importe'.

        Parameters
        ----------
        stored_df : list[dict] or None
            Datos previamente almacenados en memoria por `dcc.Store`.
            Deben representar un DataFrame serializado en formato records.
            Si es None, no se genera ningún gráfico.
        Returns
        --------
        plotly.graph_objects.Figure or str
            Devuelve un objeto Figure si la gráfica se genera correctamente.
            En caso de que no existan datos o ocurra un error, devuelve un mensaje.
            
        '''
        if not stored_df:
            return "Sube un archivo para generar la gráfica."

        try:
            df = pd.DataFrame(stored_df)

            fig = px.box(df, x='Importe', title='Boxplot de los importes periodo Enero-Noviembre')

            return fig

        except Exception as e:
            return f'Error generando gráfica: {e}'
