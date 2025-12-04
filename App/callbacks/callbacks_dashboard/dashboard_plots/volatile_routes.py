from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px
import datetime as dt
from .empty_fig import empty_fig

def plot_volatile_routes(df):
    '''
    Genera la gráfica de las top 10 rutas más volátiles.
    Hace los cálculos necesarios para determinar la volatilidad de las rutas
    basándose en el coeficiente de variación de los viajes mensuales.
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los datos cargados y limpios.
    Returns
    -------
    plotly.graph_objects.Figure
        Gráfica de barras horizontales con las 10 rutas más volátiles.
    '''
    if 'Ruta' not in df.columns:
        return empty_fig('La columna "Ruta" no existe en los datos.')
    KPIS = df.copy()
    
    # Normaliza las rutas para que A/B sea igual a B/A
    KPIS['Ruta_norm'] = df['Ruta'].apply(normalizar_ruta)

    KPIS['Mes'] = KPIS['Fecha'].dt.to_period('M')
    viajes_mensuales = (KPIS
                        .groupby(['Ruta_norm', 'Mes'])
                        .size()
                        .reset_index(name='ViajesRuta'))
    viajes_mensuales = (KPIS
                        .groupby(['Ruta_norm', 'Mes'])
                        .size()
                        .reset_index(name='ViajesRuta'))
    
    cv_por_ruta = viajes_mensuales.groupby('Ruta_norm')['ViajesRuta'].agg(
        lambda x: x.std() / x.mean()
    )

    # Top rutas por coeficiente de variación
    top_volatile_routes = cv_por_ruta.nlargest(10).reset_index()
    top_volatile_routes.columns = ['Ruta', 'Coeficiente de Variación']
    top_volatile_routes = top_volatile_routes.sort_values('Coeficiente de Variación', ascending=True)

    fig = px.bar(
        top_volatile_routes,
        x='Coeficiente de Variación',
        y='Ruta',
        orientation='h',
        title='Top 10 rutas más volátiles'
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    return fig


def normalizar_ruta(r):
    try:
        a, b = r.split('/')
        return ' / '.join(sorted([a.strip(), b.strip()]))
    except:
        return r