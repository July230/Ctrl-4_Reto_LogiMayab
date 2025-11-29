from dash.dependencies import Input, Output
from layouts.dashboard import layout as dashboard_layout
from .callbacks_dashboard.callbacks_dashboard_loader import register_callbacks_dashboard_loader
from .callbacks_dashboard.callbacks_dashboard_plots import register_callbacks_dashboard_plots

def register_callbacks_all(app):
    '''
    Registra todos los callbacks de la aplicación Dash.

    Parameters
    -----
        app : dash.Dash
            Instancia principal de la aplicación Dash donde se registran
            todos los callbacks.
    Returns:
    --------
        None
    '''
    register_callbacks_dashboard_loader(app)
    register_callbacks_dashboard_plots(app)
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
        if pathname == '/dashboard':
            return dashboard_layout
        else:
            return '404 - Página no encontrada'
