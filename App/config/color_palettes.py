'''
Paletas de colores personalizadas para las gráficas de la app.

Contiene diferentes paletas de colores predefinidas que pueden ser 
usadas en plotly para mantener consistencia visual en el dashboard.
'''

# Paleta profesional: azules y grises
PROFESSIONAL = [
    '#1f77b4',  # Azul oscuro
    '#ff7f0e',  # Naranja
    '#2ca02c',  # Verde
    '#d62728',  # Rojo
    '#9467bd',  # Púrpura
    '#8c564b',  # Marrón
    '#e377c2',  # Rosa
    '#7f7f7f',  # Gris
    '#bcbd22',  # Amarillo-verde
    '#17becf',  # Cian
]

# Paleta moderna: colores vibrantes
VIBRANT = [
    '#FF6B6B',  # Rojo brillante
    '#4ECDC4',  # Turquesa
    '#45B7D1',  # Azul cielo
    '#FFA07A',  # Salmón
    '#98D8C8',  # Verde menta
    '#F7DC6F',  # Amarillo
    '#BB8FCE',  # Púrpura
    '#85C1E2',  # Azul pálido
    '#F8B739',  # Naranja
    '#52B788',  # Verde bosque
]

# Paleta pastel: colores suaves
PASTEL = [
    '#FFB3BA',  # Rosa pastel
    '#FFFFCC',  # Amarillo pastel
    '#BAE1FF',  # Azul pastel
    '#BAFFC9',  # Verde pastel
    '#FFD8B8',  # Naranja pastel
    '#E0BBE4',  # Púrpura pastel
    '#FFDFD3',  # Coral pastel
    '#B4E7FF',  # Cian pastel
    '#D5FFBA',  # Lima pastel
    '#FFD6A5',  # Durazno pastel
]

# Paleta oscura: para fondos claros
DARK = [
    '#264653',  # Azul oscuro
    '#2A9D8F',  # Verde azulado
    '#E9C46A',  # Amarillo cálido
    '#F4A261',  # Naranja quemado
    '#E76F51',  # Rojo terracota
    '#D62828',  # Rojo oscuro
    '#A23B72',  # Púrpura oscuro
    '#6A3E37',  # Marrón oscuro
    '#1D3557',  # Azul marino
    '#457B9D',  # Azul esquila
]

# Paleta corporativa: azules y grises profesionales
CORPORATE = [
    '#003366',  # Azul corporativo
    '#0099CC',  # Azul claro
    '#66CC99',  # Verde corporativo
    '#FFCC00',  # Amarillo corporativo
    '#FF9900',  # Naranja corporativo
    '#CC0000',  # Rojo corporativo
    '#999999',  # Gris corporativo
    '#666666',  # Gris oscuro
    '#33CCFF',  # Cian corporativo
    '#FF33CC',  # Magenta corporativo
]

# Paleta por defecto (Plotly estándar)
DEFAULT = [
    '#636EFA',  # Azul
    '#EF553B',  # Rojo
    '#00CC96',  # Verde
    '#AB63FA',  # Púrpura
    '#FFA15A',  # Naranja
    '#19D3F3',  # Cian
    '#FF6692',  # Rosa
    '#B6E880',  # Verde lima
    '#FF97FF',  # Magenta
    '#FECB52',  # Amarillo
]

LOGIMAYAB = [
    '#2e3242', # Azul oscuro
    '#fd5e2c', # Naranja
    '#ffffff', # Blanco
    '#eaeaea', # Gris claro
    '#eb7d28', # Naranja claro
    '#667a8a', # Azul grisáceo
    '#000000', # Negro
]

NARANJA_TRIADA = [
    '#fd5e2c', 
    '#2cfd5e', 
    '#5e2cfd',
]

NARANJA_TRIADA_ASCENDENTE = [
    '#fd5e2c', 
    '#f38700', 
    '#dbad00', 
    '#b3d000', 
    '#73ef34', 
    '#00f389', 
    '#00d9e7', 
    '#00b7ff', 
    '#0088ff', 
    '#5e2cfd'
]

def get_palette(name: str = 'DEFAULT'):
    '''
    Retorna una paleta de colores por nombre.
    
    Parameters
    ----------
    name : str
        Nombre de la paleta. Opciones: 'PROFESSIONAL', 'VIBRANT', 'PASTEL', 
        'DARK', 'CORPORATE', 'DEFAULT'.
        
    Returns
    -------
    list
        Lista de colores en formato hex.
    '''
    palettes = {
        'PROFESSIONAL': PROFESSIONAL,
        'VIBRANT': VIBRANT,
        'PASTEL': PASTEL,
        'DARK': DARK,
        'CORPORATE': CORPORATE,
        'DEFAULT': DEFAULT,
    }
    return palettes.get(name, DEFAULT)
