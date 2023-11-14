from dash import html, dcc
import dash_bootstrap_components as dbc

from src.app.components import ids


def render_corp_tab_dashboard():

    title_box = html.H3("Corporate Dashboard", id=ids.CORP_TITLE_DASHBOARD, className='text-primary text-center p-4')

    corp_claims_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Daily Claims Processed"
                ], className= 'text-primary text-center'
            ),

            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            html.H6("Variance from YTD", className='text-primary')
                        ], className='d-flex justify-content-end pt-2'),
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_CARD_CLAIM_IND, figure={}, config={'displayModeBar':False})
                        ], className='')
                    ], className=''),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_CARD_CLAIM_CHART, figure={}, config={'displayModeBar':False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('YTD Ave', className='my-0'),
                            html.P(id=ids.CORP_CARD_CLAIM_START, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Current', className='my-0',),
                            html.P(id=ids.CORP_CARD_CLAIM_END, className='mb-0')
                        ], className='fs-6 text-end')
                    ])
                ],
            )
        ],
    )

    corp_claims_stats_card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col("Metric"),
                    dbc.Col("Current"),
                    dbc.Col('Prior'),
                    dbc.Col('Change')
                ],
                className='border-bottom border-primary border-2 p-2 align-items-center text-center'
            ),
            dbc.Row(
                [
                    dbc.Col("NUMBER OF CLAIMS - ALL MEMBERS"),
                ], className='text-center p-2',
            ),
            dbc.Row(
                [
                    dbc.Col("Top 25"),
                    dbc.Col(id=ids.CORP_CLAIM_MEM25_C),
                    dbc.Col(id=ids.CORP_CLAIM_MEM25_P),
                    dbc.Col(
                        dcc.Graph(id=ids.CORP_CLAIM_MEM25_IND, figure={}, config={'displayModeBar': False})
                    )
                ], className='align-items-center text-center',
            ),
            dbc.Row(
                [
                    dbc.Col("Max Claims"),
                    dbc.Col(id=ids.CORP_CLAIM_MEMMAX_C),
                    dbc.Col(id=ids.CORP_CLAIM_MEMMAX_P),
                    dbc.Col(
                        dcc.Graph(id=ids.CORP_CLAIM_MEMMAX_IND, figure={},
                                  config={'displayModeBar': False})
                    )
                ], className='align-items-center text-center',
            ),
        ]
    )

    corp_claims_scatbox_card = dbc.Card(
        [
            dbc.Col(
                [
                    dcc.Graph(id=ids.CORP_CLAIM_SCATBOX),
                ],
            )
        ]
    )

    corp_charges_card = dbc.Card(
        [
            html.Label(
                [
                    "Average Charges by Day"
                ], className='text-primary text-center'
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            html.H6("YTD vs Current  FIX THIS STUFF FOR BOTH CHARTS", className='text-primary')
                        ], className='d-flex justify-content-end pt-2'),
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_CARD_CHARGE_IND, figure={}, config={'displayModeBar':False})
                        ],)
                    ],),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_CARD_CHARGE_CHART, figure={}, config={'displayModeBar':False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('YTD Charge Ave', className='my-0'),
                            html.P(id=ids.CORP_CARD_CHARGE_START, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Current Charge Ave', className='my-0',),
                            html.P(id=ids.CORP_CARD_CHARGE_END, className='mb-0')
                        ], className='fs-6 text-end')
                    ])
                ],
            )
        ],
    )





    return html.Div(
        [
            dbc.Row(
                [
                    title_box
                ], className='align-items-center'
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            corp_claims_card
                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            corp_charges_card
                        ], width=5, className='border border-primary border-3 p-0',
                    )
                ], className='p-0 m-0', justify='evenly'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    corp_claims_stats_card
                                ],
                            ),
                            dbc.Row(
                                [
                                    corp_claims_scatbox_card
                                ]
                            )
                        ], width=5, className='border border-primary border-3 mt-5',
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col("Metric"),
                                    dbc.Col("Current"),
                                    dbc.Col('Prior'),
                                    dbc.Col('Change')
                                ], className='border-bottom border-primary border-2 p-2 align-items-center text-center',
                            ),
                            dbc.Row(
                                [
                                    dbc.Col("CLAIM CHARGES ($) - ALL MEMBERS"),
                                ], className='text-center p-2',
                            ),
                            dbc.Row(
                                [
                                    dbc.Col("Top 25"),
                                    dbc.Col(id=ids.CORP_CHARGE_MEM25_C),
                                    dbc.Col(id=ids.CORP_CHARGE_MEM25_P),
                                    dbc.Col(
                                        dcc.Graph(id=ids.CORP_CHARGE_MEM25_IND, figure={},
                                                  config={'displayModeBar': False})
                                    )
                                ], className='align-items-center text-center',
                            ),
                        ], width=5, className='border border-primary border-3 mt-5',
                    ),
                ], justify='evenly'
            )
        ],
    )


