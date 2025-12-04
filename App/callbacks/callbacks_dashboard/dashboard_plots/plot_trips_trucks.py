from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px
from .empty_fig import empty_fig

def plot_trips_per_truck(df, color_palette=None):
    '''
    Genera la gráfica del número de viajes por tractocamión.
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los datos cargados y limpios.
    color_palette : list, optional
        Lista de colores en formato hex para usar en la gráfica.
        Si es None, usa los colores por defecto de Plotly.
    Returns
    -------
    plotly.graph_objects.Figure
        Gráfica de barras con el número de viajes por tractocamión.
    '''
    if 'Tractocamión' not in df.columns:
        return empty_fig('La columna "Tractocamión" no existe en los datos.')

    top_10_trips_per_trucks = df['Tractocamión'].value_counts().nlargest(10).reset_index()
    top_10_trips_per_trucks.columns = ['Tractocamión', 'Frecuencia']
    top_10_trips_per_trucks = top_10_trips_per_trucks.sort_values('Frecuencia', ascending=True)

    fig = px.bar(
        top_10_trips_per_trucks,
        x='Frecuencia',
        y='Tractocamión',
        orientation='h',
        title='Cantidad de viajes por tracto',
        color='Tractocamión',
        color_discrete_sequence=color_palette if color_palette else None
    )
    fig.update_layout(showlegend=False)

    return fig