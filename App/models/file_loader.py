import pandas as pd

def load_upload_file(contents, filename):
    if filename.endswith('.csv'):
        return pd.read_csv(contents)
    elif filename.endswith('xlsx'):
        pd.read_excel(contents)
    else:
        return ValueError('Formato no válido')