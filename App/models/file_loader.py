import pandas as pd
import base64
import io

def load_upload_file(contents, filename):
    '''
    Decodifica el archivo subido desde dcc.Upload y lo retorna como DataFrame.
    Argumentos:
        contents: cadena base64 del archivo
        filename: nombre del archivo original
    Retorna:
        DataFrame 
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