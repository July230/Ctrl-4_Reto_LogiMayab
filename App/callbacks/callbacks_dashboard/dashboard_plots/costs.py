from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px
from utils.empty_fig import empty_fig
import numpy as np
import pandas as pd



def plot_costs(df):
    '''
                    
    '''
    fig=px.bar(df, x='Nombre_Cliente', y='CV_Mensual')

    return fig