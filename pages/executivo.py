import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

dash.register_page(__name__)

layout = html.Div([
            html.H2("Página de Executivo"),
            # Adicione aqui o conteúdo da página de Executivo
            dcc.RadioItems(
                id='tipo-politico-executivo',
                options=[
                    {'label': 'Presidente', 'value': 'presidente'},
                    {'label': 'Governadores', 'value': 'governadores'},
                    {'label': 'Prefeitos', 'value': 'prefeitos'},
                ],
                value='presidente'
            ),
        ])
