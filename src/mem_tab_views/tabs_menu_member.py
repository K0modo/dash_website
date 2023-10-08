from dash import html
import dash_bootstrap_components as dbc

from src.components import ids


def render_member_tab_menu():
    tab_menu = [
        {"tab_id": ids.MEM_TAB_DASHBOARD, 'label': 'Dashboard'},
        {"tab_id": ids.MEM_TAB_SERVICES, 'label': 'Medical Services'},
        {"tab_id": ids.MEM_TAB_CLAIMS, 'label': 'Medical Claims'},
    ]
    return html.Div(
        id='tabs',
        children=[
            dbc.Tabs(
                id=ids.MEM_APP_TABS,
                active_tab=ids.MEM_TAB_DASHBOARD,
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
