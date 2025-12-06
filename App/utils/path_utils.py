import os

def get_data_path(filename):
    '''
    Retorna la ruta absoluta hacia un archivo dentro de /data
    '''
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(base_dir, '..', 'data')
    return os.path.join(data_dir, filename)