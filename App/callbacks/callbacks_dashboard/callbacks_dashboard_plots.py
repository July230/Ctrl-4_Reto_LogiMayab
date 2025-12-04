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
        prevent_initial_call=False
    )
    def update_plot(df_json):
        '''
        Genera y actualiza la figura principal del dashboard a partir de los datos cargados.

        Toma la información almacenada en dcc.Store (formato dict) y la convierte en un 
        DataFrame de pandas.

        Llama a funciones auxiliares para crear cada gráfico específico.

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
            # Retorna una figura vacía con mensaje en lugar de PreventUpdate
            fig = go.Figure()
            fig.update_layout(
                xaxis={'visible': False},
                yaxis={'visible': False},
                annotations=[{
                    'text': 'Sube un archivo para generar la gráfica.',
                    'xref': 'paper',
                    'yref': 'paper',
                    'showarrow': False,
                    'font': {'size': 16}
                }]
            )
            return fig

        try:
            print("Generando gráfica con los datos cargados...")
            # Usar io.StringIO para evitar deprecation warning al leer JSON
            df = pd.read_json(io.StringIO(df_json), orient='records')

            if 'Ruta' not in df.columns:
                # Si no existe la columna, informar al usuario
                fig = go.Figure()
                fig.update_layout(
                    xaxis={'visible': False},
                    yaxis={'visible': False},
                    annotations=[{
                        'text': 'La columna "Ruta" no existe en los datos.',
                        'xref': 'paper',
                        'yref': 'paper',
                        'showarrow': False,
                        'font': {'size': 14, 'color': 'red'}
                    }]
                )
                return fig

            # Calcular frecuencias y quedarnos con las 10 más frecuentes
            top_routes = df['Ruta'].value_counts().nlargest(10).reset_index()
            top_routes.columns = ['Ruta', 'Frecuencia']

            # Asegurar orden descendente en la gráfica
            top_routes = top_routes.sort_values('Frecuencia', ascending=True)

            fig = px.bar(top_routes, x='Frecuencia', y='Ruta', orientation='h',
                         title='Top 10 rutas más frecuentes',
                         labels={'Frecuencia': 'Frecuencia', 'Ruta': 'Ruta'})
            fig.update_layout(yaxis={'categoryorder':'total ascending'})

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
