from dash import html
import dash_bootstrap_components as dbc
from src.app.components import ids


def render_analytic_tab_menu():
    tab_menu = [
        {"tab_id": ids.ANALYTIC_TAB_DASHBOARD, 'label': 'Dashboard'},
        {"tab_id": ids.ANALYTIC_TAB_SERVICES, 'label':'Services'},
        # {"tab_id": ids.TAB_CLAIMS, 'label':'Medical Claims'},
    ]
    return html.Div(
        id='tabs',
        children=[
            dbc.Tabs(
                id=ids.ANALYTIC_APP_TABS,
                active_tab=ids.ANALYTIC_TAB_DASHBOARD,
                className='dbc fs-4 mt-4 nav nav-pills nav-fill',
                children=[
                    dbc.Tab(
                        tab_id=item['tab_id'],
                        label=item['label'],

                    ) for item in tab_menu
                ]
            ),
            html.Hr()
        ],
    )
