import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

dash.register_page(__name__)

layout = html.Div([
            html.H2("Página de Legislativo"),
            dcc.RadioItems(
                id='tipo-politico-legislativo',
                options=[
                    {'label': 'Senadores', 'value': 'senadores'},
                    {'label': 'Dep Federais', 'value': 'dep-federais'},
                    {'label': 'Dep Estaduais', 'value': 'dep-estaduais'},
                    {'label': 'Vereadores', 'value': 'vereadores'},
                ],
                value='senadores'
            ),
            # Adicione aqui as visualizações com base na seleção de tipo de político
        ])
