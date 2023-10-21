import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H3("Página Inicial", style={'color': 'white'}),
    # Adicione o conteúdo específico para esta página
    html.P("Seja bem-vindo ao Cérebro Político. Somos uma base de dados aberta sobre informações importantes a respeito de tomada de decisão democrática. Qualquer pessoa pode colaborar com o projeto, e aqui voce podera encontrar informações sobre pessoas que exercem cargos públicos, gastos governamentais, além de diversas métricas de âmbito social, econômico, tecnológico e demográfico. :)")
])
