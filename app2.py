import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Crear la aplicación principal de Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.title = "Inicio - Mujeres STEM en Bolivia"

# Layout de la página de inicio
inicio_layout = dbc.Container(fluid=True, style={"padding": "0"}, children=[
    # Imagen de fondo con encabezado
    html.Div(
        style={
            "background-image": "url('assets/assets')",  # Ruta a la imagen en la carpeta 'assets'
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
                dbc.Button("Explorar Proyectos", href="/pagina2", color="primary", className="me-3", size="lg"),
                dbc.Button("Ver Mapa Interactivo", href="/pagina3", color="success", size="lg")
            ], className="mt-3")
        ]
    )
])

# Definir el layout principal con rutas
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

# Callback para manejar las rutas
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/pagina2":
        from pagina2 import layout as pagina2_layout
        return pagina2_layout
    elif pathname == "/pagina3":
        from pagina3 import layout as pagina3_layout
        return pagina3_layout
    else:
        return inicio_layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)











