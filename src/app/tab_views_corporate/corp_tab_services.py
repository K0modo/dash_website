from dash import html
import dash_bootstrap_components as dbc

from src.app.tab_views_corporate import corp_tab_services_elements as S


def render_corp_tab_services():

    return html.Div(
        [
            dbc.Row(
                [
                    S.title_box
                ], className='align-items-center mb-0'
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.icd_dropdown_box
                        ], width=2
                    )
                ], className='mb-2'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.corp_services_count_card
                        ], width=5
                    ),
                    dbc.Col(
                        [
                            S.corp_services_paid_card
                        ], width=5
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            S.corp_services_racing
                        ], width=9
                    )
                ], className='align-center'
            )
        ]
    )