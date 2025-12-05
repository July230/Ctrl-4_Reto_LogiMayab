from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd
import io

def register_callbacks_dashboard_filters(app):
    '''
    Registra los callbacks encargados de actualizar los filtros del dashboard
    basados en los datos cargados.

    Parameters
    ----------
    app : dash.Dash
        Instancia principal de la aplicación Dash donde se registran
        todos los callbacks.
    
    Returns
    -------
    None
    '''
    @app.callback(
        Output('month-filter', 'options'),
        Input('stored-data', 'data'),
        prevent_initial_call=False
    )
    def load_months(stored_data):
        '''
        Carga los meses únicos disponibles en los datos para el filtro de mes.

        Parameters
        ----------
        stored_data : JSON or None
            Datos previamente almacenados como JSON en memoria por dcc.Store.
            Deben representar un DataFrame serializado en formato records.
            Si es None, no se generan opciones.

        Returns
        --------
        list of dict
            Lista de opciones para el dropdown de meses, cada una como un diccionario
            con 'label' y 'value'.
        '''
        if stored_data is None:
            return []

        df_json = stored_data['df']
        df = pd.read_json(io.StringIO(df_json), orient='records')
        df['Fecha'] = pd.to_datetime(df['Fecha'], format='mixed', dayfirst=False)

        # Extraer meses presentes en el archivo
        meses_num = df['Fecha'].dt.month.unique()
        meses_num.sort()

        # Diccionario para nombres en español
        meses_es = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
            5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
            9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        return [
            {'label': meses_es[m], 'value': m}
            for m in meses_num
        ]