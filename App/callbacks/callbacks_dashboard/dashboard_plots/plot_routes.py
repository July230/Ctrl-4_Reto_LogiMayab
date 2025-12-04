from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px
from .empty_fig import empty_fig

def plot_frequent_routes(df, color_palette=None):
    '''
    Genera la gráfica de las top 10 rutas más frecuentes.
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
        Gráfica de barras horizontales con las 10 rutas más frecuentes.
    '''
    if 'Ruta' not in df.columns:
        return empty_fig('La columna "Ruta" no existe en los datos.')

    top_routes = df['Ruta'].value_counts().nlargest(10).reset_index()
    top_routes.columns = ['Ruta', 'Frecuencia']
    top_routes = top_routes.sort_values('Frecuencia', ascending=True)

    fig = px.bar(
        top_routes,
        x='Frecuencia',
        y='Ruta',
        orientation='h',
        title='Top 10 rutas más frecuentes',
        color_discrete_sequence=[color_palette[0]] if color_palette else None
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    return fig
