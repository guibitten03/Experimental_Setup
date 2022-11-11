from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
import pandas as pd
import plotly.express as px

from app import app

layout = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id = "per-state")

                            ], md = 6),
                            dbc.Col([
                                dcc.Graph(id = "per-city")

                            ], md = 6)
                        ])
                    ], style = {"margin-top": "10px", "margin-right": "10px"})
                ])
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id = "is_open")

                            ], md = 6),
                            dbc.Col([
                                dcc.Graph(id = "stars")

                            ], md = 6)
                        ])
                    ], style = {"margin-top": "10px", "margin-right": "10px"})
                ])
            ])
])


# === CALLBACKS === #
@app.callback(
    Output("per-state", "figure"),
    [Input("data-b", "data")]
)
def per_state(data):
    df = pd.DataFrame(data)

    df = df.groupby('state').size().sort_values(ascending = False).reset_index()
    df.rename(columns = {0:'size'}, inplace=True)

    fig = px.bar(df, x = 'state', y = 'size', title="Nb Establishments per State", template = "plotly_white")

    return fig

@app.callback(
    Output("per-city", "figure"),
    [Input("data-b", "data")]
)
def per_city(data):
    df = pd.DataFrame(data)

    df = df.groupby('city').size().sort_values(ascending = False).reset_index().head(10)
    df.rename(columns = {0:'size'}, inplace=True)

    fig = px.bar(df, x = 'city', y = 'size', title="Top 10 per City", template = "plotly_white")

    return fig


@app.callback(
    Output("is_open", "figure"),
    [Input("data-b", "data")]
)
def is_open(data):
    df = pd.DataFrame(data)

    is_open = df.groupby('is_open').size().reset_index()
    is_open.rename(columns = {'is_open': 'Openned', 0: 'Size'}, inplace = True)
    is_open['Openned'] = is_open['Openned'].map({0 : 'Não', 1 : 'Sim'})

    fig = px.bar(is_open, x = 'Openned', y = 'Size', template = "plotly_white", title = "Is Open?")

    return fig
    

@app.callback(
    Output("stars", "figure"),
    [Input("data-b", "data")]
)
def stars(data):
    df = pd.DataFrame(data)

    stars = df.groupby('stars').size().sort_values(ascending = False).reset_index()
    stars.rename(columns = {"stars":"Stars", 0:"Size"}, inplace=True)

    fig = px.bar(stars, x = 'Stars', y = 'Size', template = "plotly_white", title = "Stars")

    return fig