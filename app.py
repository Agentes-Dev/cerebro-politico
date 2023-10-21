import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.config.suppress_callback_exceptions = True

navbar = dbc.NavbarSimple(        
    brand=html.Img(src='/assets/logo.svg', height='80px', className='clickable-logo'),
    brand_href="/",
    color="primary",
    dark=True,
    children=[
        dbc.NavLink("Home", href="/"),
        dbc.NavLink("Legislativo", href="/legislativo"),
        dbc.NavLink("Executivo", href="/executivo"),
        dbc.NavLink("Judiciário", href="/judiciario"),
        dbc.NavLink("Dados Gerais", href="/dados-gerais"),
    ],
)

# Layout do aplicativo
app.layout = html.Div([navbar, dash.page_container])

if __name__ == '__main__':
    app.run_server(debug=True)
