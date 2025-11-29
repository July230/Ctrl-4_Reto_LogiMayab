from .callbacks_upload import register_callbacks_upload

def register_callbacks_all(app):
    '''
    Concentra los callbacks functions de la aplicación
    Argumentos:
        app: Objeto app de la aplicación
    '''
    register_callbacks_upload(app)
