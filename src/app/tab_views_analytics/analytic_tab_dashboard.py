from dash import html, dcc
import dash_bootstrap_components as dbc

from src.app.tab_views_analytics import analytic_tab_dashboard_elements as A


def render_analytic_tab_dashboard():

    return html.Div(
        [
            dbc.Row(
                [
                    A.title_box
                ], className='align-items-center mb-0'
            ),
            dbc.Row(
                [
                    A.button
                ]
            ),
            dbc.Row(
                [
                    A.cash_stats_card

                ], className='align-items-center mb-0'
            ),
            dbc.Row(
                [

                ], className='align-items-center mb-0'
            ),
            dbc.Row(
                [
                    A.steps
                ], className='align-items-center mb-0'
            ),

        ],
    )
