from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import io
from .dashboard_plots.empty_fig import empty_fig
from .dashboard_plots.plot_routes import plot_frequent_routes
from .dashboard_plots.plot_trips_trucks import plot_trips_per_truck
from .dashboard_plots.volatile_routes import plot_volatile_routes

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
        Output('plot-2', 'figure'),
        Output('plot-3', 'figure'),
        Input('stored-data', 'data'),
        prevent_initial_call=False
    )
    def update_plots(df_json):
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
        # Si no hay datos cargados, retorna una figura vacía con mensaje
        if df_json is None:
            return (
                empty_fig('Sube un archivo para generar la gráfica.'),
                empty_fig('Sube un archivo para generar la gráfica.'),
                empty_fig('Sube un archivo para generar la gráfica.')
            )

        try:
            # Usar io.StringIO para evitar deprecation warning al leer JSON
            df = pd.read_json(io.StringIO(df_json), orient='records')

            # Reconvertir columnas de fecha que se perdieron al serializar a JSON
            df['Fecha'] = pd.to_datetime(df['Fecha'],format='mixed',dayfirst=False)

            # Llamar a la función que genera la gráfica de las top 10 rutas más frecuentes
            fig1 = plot_frequent_routes(df)
            fig2 = plot_trips_per_truck(df)
            fig3 = plot_volatile_routes(df)

            return fig1, fig2, fig3

        except Exception as e:
            # Devuelve una figura con el mensaje de error para no romper el componente Graph
            fig_error = empty_fig(f'Error al generar la gráfica: {e}')
            return fig_error, fig_error, fig_error
