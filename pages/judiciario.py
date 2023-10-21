import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

dash.register_page(__name__)

layout = html.Div([
            html.H2("Página de Judiciário"),
            html.P("Nome do TSE: <inserir nome do TSE>"),
        ])
