from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px
from utils.empty_fig import empty_fig
import numpy as np
import pandas as pd
from scipy.stats import norm

def plot_cv_buffer(df):
    '''
    Genera la gráfica de costos basada en el coeficiente de variación mensual por cliente.             
    '''
    fig = px.bar(
        df,
        x='Valor',
        y='Nombre_Cliente',
        orientation='h',
        color='Métrica',
        barmode='group',
        title='Comparación de CV Semanal Promedio y CV de Viajes con Buffer por Cliente'
    )

    fig.update_layout(
        xaxis_title='Nombre del Cliente',
        yaxis_title='Coeficiente de Variación',
        xaxis_tickangle=90, 
        legend_title='Métrica'
    )
    
    return fig