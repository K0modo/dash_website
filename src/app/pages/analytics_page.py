import dash
from dash import Dash, dcc, html, Input, Output, State, callback, dash_table
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__,
                   path='/analytics',
                   name='Analytics',
                   title='Analytics',
                   description='Analytical Data Analysis'
                   )


layout = dbc.Container(
    [
        dcc.Tabs(className='dbc', children=[
            dbc.Tab(label='Claims', children=[
                dbc.Row(
                    [

                    ]
                )
            ]),
            dbc.Tab(label='Services', children=[
                dbc.Row(
                    [

                    ]
                )
            ]),

        ])
    ]
)
