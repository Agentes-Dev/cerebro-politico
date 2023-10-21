import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

dash.register_page(__name__)

layout = html.Div([
            html.H2("Página de Dados Gerais"),
            # Adicione aqui o conteúdo da página de Dados Gerais
        ])