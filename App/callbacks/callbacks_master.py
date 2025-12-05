from .callbacks_dashboard.callbacks_dashboard_loader import register_callbacks_dashboard_loader
from .callbacks_dashboard.callbacks_dashboard_plots import register_callbacks_dashboard_plots
from .callbacks_dashboard.callbacks_dashboard_filters import register_callbacks_dashboard_filters
from .callbacks_routes.callbacks_routes_plots import register_callbacks_routes_plots
from .router import register_callbacks_router

def register_callbacks_all(app):
    '''
    Registra todos los callbacks de la aplicación Dash.

    Parameters
    ----------
    app : dash.Dash
        Instancia principal de la aplicación Dash donde se registran
        todos los callbacks.

    Returns
    -------
    None
    '''
    register_callbacks_dashboard_loader(app)
    register_callbacks_dashboard_plots(app)
    register_callbacks_dashboard_filters(app)
    register_callbacks_routes_plots(app)
    register_callbacks_router(app)