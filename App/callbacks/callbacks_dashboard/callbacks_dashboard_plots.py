from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io

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
    def update_plot(df_json):
        '''
        Genera y actualiza la figura principal del dashboard a partir de los datos cargados.

        Toma la información almacenada en dcc.Store (formato dict) y la convierte en un 
        DataFrame de pandas. Luego genera un boxplot de la columna 'Importe'.

        Parameters
        ----------
        df_json : JSON or None
            Datos previamente almacenados como JSON en memoria por dcc.Store.
            Deben representar un DataFrame serializado en formato records.
            Si es None, no se genera ningún gráfico.
        Returns
        --------
        plotly.graph_objects.Figure or str
            Devuelve un objeto Figure si la gráfica se genera correctamente.
            En caso de que no existan datos o ocurra un error, devuelve un mensaje.
            
        '''
        if df_json is None:
            raise PreventUpdate

        try:
            # Usar io.StringIO para evitar deprecation warning al leer JSON
            df = pd.read_json(io.StringIO(df_json), orient='records')

            fig = px.box(df, x='Importe', title='Boxplot de los importes periodo Enero-Noviembre')

            return fig

        except Exception as e:
            # Devuelve una figura con el mensaje de error para no romper el componente Graph
            fig = go.Figure()
            fig.update_layout(
                xaxis={'visible': False},
                yaxis={'visible': False},
                annotations=[{
                    'text': f'Error generando gráfica: {e}',
                    'xref': 'paper',
                    'yref': 'paper',
                    'showarrow': False,
                    'font': {'size': 12, 'color': 'red'}
                }]
            )
            return fig
