# En este archivo se llaman los diferentes callbacks
from .callbacks_upload import register_callbacks_upload

def register_callbacks_all(app):
    register_callbacks_upload(app)
