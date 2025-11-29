import pandas as pd

def load_upload_file(contents, filename):
    if filename.endswith('.csv'):
        return pd.read_csv(contents)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        return pd.read_excel(contents)
    else:
        raise ValueError('Formato no válido')