from .callbacks_upload import register_callbacks_upload
from .callbacks_dashboard import register_callbacks_dashboard_graph

def register_callbacks_all(app):
    '''
    Registra todos los callbacks de la aplicación Dash.

    Args:
        app (Dash): Instancia principal de la aplicación Dash donde se registran
            todos los callbacks.
    Returns:
        None
    '''
    register_callbacks_upload(app)
    register_callbacks_dashboard_graph(app)
