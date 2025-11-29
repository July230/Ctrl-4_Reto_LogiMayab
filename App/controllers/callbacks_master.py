from .callbacks_upload import register_callbacks_upload

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
