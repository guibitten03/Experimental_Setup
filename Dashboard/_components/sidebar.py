from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
from app import app

style_sidebar = style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)",
                    "margin": "10px",
                    "padding": "10px",
                    "height": "90vh"}

layout = dbc.Card([
            dbc.Row([
                dbc.Col([
                    html.H1("@Gui")
                ])
            ]),

            html.Hr(),

            html.P("Choise Dataset"),

            dbc.Nav([
                dbc.NavLink("Stats", href = "/", active = "exact"),
                dbc.NavLink("Reviews", href = "/reviews", active = "exact"),
                dbc.NavLink("Feeling", href = "/f-analisys", active = "exact"),
                dbc.NavLink("Business", href = "/business", active = "exact"),
                dbc.NavLink("Tips", href = "/tips", active = "exact"),
                dbc.NavLink("Users", href = "/users", active = "exact")
            ], vertical = True, pills = True, style = {"margin-bottom" : "50px"}),



], style = style_sidebar)