import pandas as pd
import base64
import io

def load_upload_file(contents, filename):
    '''
    Decodifica y carga un archivo subido desde un componente dcc.Upload
    y lo convierte en un DataFrame de pandas.

    Esta función recibe el contenido base64 del archivo enviado por Dash
    y lo decodifica. Dependiendo de la extensión del archivo, lo procesa
    como CSV o Excel y retorna un DataFrame.

    Parameters
    ----------
    contents : str
        Cadena codificada en base64 generada por dcc.Upload. Contiene
        metadatos y el contenido real del archivo, separados por una coma.
        Ejemplo: `"data:application/vnd.ms-excel;base64,XXXXX..."`.
    filename : str 
        Nombre original del archivo subido. Utilizado para determinar el tipo
        de archivo según su extensión.
    Retorns
    -------
    pandas.DataFrame
        DataFrame resultante de decodificar y leer el archivo.

    Raises
    ------
    ValueError
        Si el contenido es None o si la extensión del archivo no es válida.

    '''
    if contents is None:
        raise ValueError("No se recibió contenido")

    # Separar metadata del contenido
    content_type, content_string = contents.split(',')

    # Decodificar base64
    decoded = base64.b64decode(content_string)

    # Procesar según extensión
    if filename.endswith('.csv'):
        return pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        return pd.read_excel(io.BytesIO(decoded))
    else:
        raise ValueError("Formato no válido")