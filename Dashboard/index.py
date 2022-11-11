import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from app import *
from _components import sidebar, business, fanalisys, reviews, stats, tips, users


# === DATABASE === #
data_b = pd.read_csv("../datasets/yelp_csv/business_yelp_dataset.csv")
data_b = data_b.dropna()
data_b_dict = data_b.to_dict()


# === LAYOUT === #

content = html.Div(id = "page-content")

app.layout = html.Div([

    dcc.Store(id = "data-b", data = data_b_dict),

                dbc.Row([
                    dbc.Col([
                        dcc.Location(id = "url"),
                        sidebar.layout
                    ], md = 2),

                    dbc.Col([
                        content
                    ], md = 10)
                ], style = {"padding" : "0px"})
])

# === CALLBACKS === #
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def rote(pathname):
    if pathname == "/":
        return stats.layout

    if pathname == "/reviews":
        return reviews.layout

    if pathname == "/business":
        return business.layout

    if pathname == "/f-analisys":
        return fanalisys.layout

    if pathname == "/tips":
        return tips.layout

    if pathname == "/users":
        return users.layout


if __name__ == "__main__":
    app.run_server(debug = True)