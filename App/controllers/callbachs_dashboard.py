from dash.dependencies import Input, Output, State
from dash import html, dcc
import plotly.express as px
from models.file_loader import load_upload_file

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
        Output('graph-container', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename')
    )
    def update_graph(contents, filename):
        '''
        Obtiene el dataframe y genera los gráficos y elementos del dashboard
        '''
        if not contents:
            return "Sube un archivo para generar la gráfica."

        try:
            df = load_upload_file(contents, filename)

            # Gráfica de líneas si tiene columnas numéricas
            fig = px.line(df)

            return html.Div([
                html.H3('Gráfica generada'),
                html.Div(children=[
                    dcc.Graph(figure=fig)
                ])
            ])

        except Exception as e:
            return f'Error generando gráfica: {e}'
