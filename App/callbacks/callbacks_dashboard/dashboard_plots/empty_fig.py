import plotly.graph_objects as go

def empty_fig(message):
    '''
    Genera una figura vacía con un mensaje centralizado.

    Parameters
    ----------
    message : str
        Mensaje a mostrar en la figura vacía.

    Returns
    -------
    plotly.graph_objects.Figure
        Figura vacía con el mensaje proporcionado.
    '''
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        xref='paper', yref='paper',
        showarrow=False,
        font=dict(size=20),
        x=0.5, y=0.5,
        align='center'
    )
    fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        plot_bgcolor='white'
    )
    return fig