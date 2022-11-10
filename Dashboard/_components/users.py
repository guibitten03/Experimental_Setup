from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
from app import app

layout = html.Div([
            dbc.Row([
                dbc.Col([
                    html.H1("users")
                ])
            ])
])