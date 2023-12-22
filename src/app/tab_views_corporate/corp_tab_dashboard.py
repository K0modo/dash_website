from dash import html, dcc
import dash_bootstrap_components as dbc
from src.app.components import ids
from src.app.tab_views_corporate import corp_tab_dashboard_elements as D


def render_corp_tab_dashboard():

    return html.Div(
        [
            dbc.Row(
                [
                    D.title_box
                ], className='align-items-center mb-0'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.period_dropdown_box
                        ], width=2
                    )
                ], className='mb-2'
            ),
            dbc.Row(
                [
                    html.H3("MEDICAL CLAIMS PROCESSED")
                ], className='text-primary text-center p-2'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.corp_daily_claims_card
                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            D.corp_annual_claims_card
                        ], width=5, className='border border-primary border-3 p-0',
                    )
                ], className='p-0 m-0', justify='evenly'
            ),
            dbc.Row(
                [
                    html.H3("MEDICAL CLAIMS PAID")
                ], className='text-primary text-center p-2 mt-3'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.corp_daily_paid_card
                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            D.corp_annual_paid_card
                        ], width=5, className='border border-primary border-3 p-0',
                    )
                ], className='p-0 m-0', justify='evenly'
            ),
            dbc.Row(
                [
                    html.H3("MEMBER PARTICIPATION")
                ], className='text-primary text-center p-2 mt-3'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            D.corp_period_member_card
                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            D.corp_annual_member_card
                        ], width=5, className='border border-primary border-3 p-0',
                    )
                ], className='p-0 m-0', justify='evenly'
            ),
        ],
    )


