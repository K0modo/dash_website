from dash import html, dcc
import dash_bootstrap_components as dbc
from src.app.components import ids



title_box = html.H3("Analytic Dashboard", className='text-primary text-center p-2')

cash_stats_card = dbc.Card(
    [
        html.H4("Statistics - Charge & Payment"),
        html.Div(id=ids.ANALYTIC_DASHBOARD_CHARGE_TABLE)
    ]
)

button = html.Div(
    html.Button('Request Stats', id=ids.ANALYTIC_DASHBOARD_BUTTON, n_clicks=0)
)




todo_card = dbc.Card(
    [
        dbc.Row(
            [
                html.H4("To Do"),
                html.Br(),
                html.Li("Set tabs"),
                html.Li("Create Analytic_tab_claims and claim_elements"),
                html.Li("Follow stats book "),
                html.Li("Create Analytic_tab_services and service_elements")

            ], className='my-4'
        ),
    ]
)

steps = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Steps to Create Data and Graphs", className='mb-4'),
                        html.Li("Create Container or Card"),
                        html.Li("Create id"),
                        html.Li("Assign Container with id to Layout"),
                        html.Li("Create Postgres Table"),
                        html.Li("Create ORM Model for Table"),
                        html.Li("Test ORM query in JupyterLab"),
                        html.Li("Create Callback Output and Input Components"),
                        html.Li("Make Graph functions "),
                        html.Li("Test Callback")
                    ], width=5
                )
            ], className='d-flex justify-content-center'
        )
    ]
)
