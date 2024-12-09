import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Crear la aplicación principal de Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Inicio - Mujeres STEM en Bolivia"

# Layout de la página de inicio
app.layout = dbc.Container(fluid=True, style={"padding": "0"}, children=[
    # Imagen de fondo con encabezado
    html.Div(
        style={
            "background-image": "url('Screen Shot 2024-12-09 at 3.53.28 PM.png')",  # Cambia esta URL a la ubicación pública de tu imagen
            "background-size": "cover",
            "background-position": "center",
            "height": "600px",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "color": "white",
            "text-align": "center",
            "flex-direction": "column",
        },
        children=[
            html.H1("Mujeres STEM en Bolivia", style={"font-size": "48px", "font-weight": "bold", "text-shadow": "2px 2px 4px rgba(0,0,0,0.6)"}),
            html.P(
                "Descubre los proyectos y logros de las mujeres STEM en Bolivia. ¡Inspírate y explora nuestro contenido!",
                style={"font-size": "20px", "text-shadow": "1px 1px 3px rgba(0,0,0,0.6)"}
            ),
            html.Div([
                dbc.Button("Explorar Proyectos", href="https://papers-bolivia.onrender.com/", color="primary", className="me-3", size="lg"),
                dbc.Button("Ver Mapa Interactivo", href="https://mujeres-stem-bolivia-1.onrender.com", color="success", size="lg")
            ], className="mt-3")
        ]
    ),

    # Sección de información destacada
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H4("¿Qué encontrarás aquí?", className="text-center text-primary mb-3"),
                    html.P(
                        "Este dashboard central te permite descubrir proyectos destacados, explorar el mapa interactivo "
                        "y conocer más sobre las mujeres STEM en Bolivia que están cambiando el mundo.",
                        style={"font-size": "16px", "text-align": "center", "line-height": "1.8"}
                    ),
                ])
            ], width=12),
        ])
    ], style={"background-color": "#f8f9fa", "padding": "40px 20px"})
])

server = app.server

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True, port=8070)

