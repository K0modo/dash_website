from dash import html, dcc
import dash_bootstrap_components as dbc

from src.app.analytic_tab_views import analytic_tab_services_elements as A


def render_analytic_tab_services():

    return html.Div(
        [
            dbc.Row(
                [
                    A.title_box
                ], className='align-items-center mb-0'
            ),

        ],
    )
