from dash import html
from dash.dependencies import Input, Output
from layouts.dashboard import dashboard_content
from layouts.routes import routes_content


def register_callbacks_router(app):
    '''
    Registra los callbacks encargados de renderizar el contenido según la URL.

    Separar el router en su propio módulo respeta SRP (Single Responsibility)
    y facilita pruebas y mantenimiento.

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
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        '''
        Actualiza el contenido de la página según la URL.

        Parameters
        ----------
        pathname : str
            Ruta actual de la URL.

        Returns
        -------
        dash.html.Div
            Contenido correspondiente a la página solicitada.
        '''
        if not pathname or pathname == '/' or pathname == '/dashboard':
            return dashboard_content
        if pathname == '/rutas':
            return routes_content
        return html.H1('404: Página no encontrada', style={'color': 'red'})
