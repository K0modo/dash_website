from dash import html, dcc
import dash_bootstrap_components as dbc
from src.app.components import ids


def render_corp_tab_dashboard():

    title_box = html.H3("Corporate Dashboard", id=ids.CORP_TITLE_DASHBOARD, className='text-primary text-center p-2')

    period_dropdown_box = html.Div([
        html.H4('Select Period',
                className='text-primary'),

        dcc.Dropdown(
            id=ids.CORP_PERIOD_DROPDOWN,
            options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            value=1,
            clearable=False,
            persistence='session',
            style={'width': '50px'}
        )
    ], className='pt-0, mt-0')


    """
    ROW - MEDICAL CLAIMS PROCESSED
    """

    corp_daily_claims_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Daily Claims Processed"
                ], className= 'text-primary text-center'
            ),

            dbc.CardBody(
                [
                    # dbc.Row([
                    #     dbc.Col([
                    #         html.H6("Variance from YTD", className='text-primary')
                    #     ], className='d-flex justify-content-end pt-2'),
                    #     dbc.Col([
                    #         dcc.Graph(id=ids.CORP_CARD_CLAIM_IND, figure={}, config={'displayModeBar':False})
                    #     ], className='')
                    # ], className=''),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_DAILY_CLAIMS_CHART, figure={}, config={'displayModeBar':False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('Daily Average', className='my-0'),
                            html.P(id=ids.CORP_DAILY_CLAIMS_AVERAGE, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Period Total', className='my-0',),
                            html.P(id=ids.CORP_DAILY_CLAIMS_SUM, className='mb-0')
                        ], className='fs-6 text-end')
                    ])
                ],
            )
        ]
    )

    corp_annual_claims_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Annual Daily Claims"
                ], className='text-primary text-center'
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_ANNUAL_CLAIMS_CHART, figure={}, config={'displayModeBar': False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('Period Average', className='my-0'),
                            html.P(id=ids.CORP_ANNUAL_CLAIMS_AVERAGE, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Annual Total', className='my-0', ),
                            html.P(id=ids.CORP_ANNUAL_CLAIMS_SUM, className='mb-0')
                        ], className='fs-6 text-end')
                    ])
                ],
            )
        ],
    )

    """
    ROW - CASHFLOW
    """

    corp_daily_cashflow_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Daily Claims Paid"
                ], className='text-primary text-center'
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_DAILY_PAID_CHART, figure={}, config={'displayModeBar': False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('Daily Average', className='my-0'),
                            html.P(id=ids.CORP_DAILY_PAID_AVERAGE, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Period Total', className='my-0', ),
                            html.P(id=ids.CORP_DAILY_PAID_SUM, className='mb-0')
                        ], className='fs-6 text-end')
                    ])
                ],
            )
        ]
    )

    corp_annual_cashflow_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Annual Claims Paid"
                ], className='text-primary text-center'
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_ANNUAL_PAID_CHART, figure={}, config={'displayModeBar': False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('Period Average', className='my-0'),
                            html.P(id=ids.CORP_ANNUAL_PAID_AVERAGE, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Annual Total', className='my-0', ),
                            html.P(id=ids.CORP_ANNUAL_PAID_SUM, className='mb-0')
                        ], className='fs-6 text-end')
                    ])
                ],
            )
        ]
    )



    """
    ROW - MEMBER ACTIVITY    
    """
    corp_mem_participation_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Daily Member Activity"
                ], className='text-primary text-center'
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_DAILY_MEMBER_CHART, figure={}, config={'displayModeBar': False})
                        ], width=12),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P('Daily Average', className='my-0'),
                            html.P(id=ids.CORP_DAILY_MEMBER_AVERAGE, className='mb-0')
                        ], className='fs-6'),
                        dbc.Col([
                            html.P('Period Total', className='my-0', ),
                            html.P(id=ids.CORP_DAILY_MEMBER_SUM, className='mb-0')
                        ], className='fs-6 text-end')
                    ])

                ]
            )
        ]
    )

    corp_mem_charges_card = dbc.Card(
        [
            dbc.Label(
                [
                    "Average Charges by Member"
                ], className='text-primary text-center'
            ),
            dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id=ids.CORP_MEM_CHARGE_CHART, figure={}, config={'displayModeBar': False})
                        ], width=12),
                    ]),
                ]
            )
        ]
    )

    # corp_claims_stats_card = dbc.Card(
    #     [
    #         dbc.Row(
    #             [
    #                 dbc.Col("Metric"),
    #                 dbc.Col("Current"),
    #                 dbc.Col('Prior'),
    #                 dbc.Col('Change')
    #             ],
    #             className='border-bottom border-primary border-2 p-2 align-items-center text-center'
    #         ),
    #         dbc.Row(
    #             [
    #                 dbc.Col("NUMBER OF CLAIMS - ALL MEMBERS"),
    #             ], className='text-center p-2',
    #         ),
    #         dbc.Row(
    #             [
    #                 dbc.Col("Top 25"),
    #                 dbc.Col(id=ids.CORP_CLAIM_MEM25_C),
    #                 dbc.Col(id=ids.CORP_CLAIM_MEM25_P),
    #                 dbc.Col(
    #                     dcc.Graph(id=ids.CORP_CLAIM_MEM25_IND, figure={}, config={'displayModeBar': False})
    #                 )
    #             ], className='align-items-center text-center',
    #         ),
    #         dbc.Row(
    #             [
    #                 dbc.Col("Max Claims"),
    #                 dbc.Col(id=ids.CORP_CLAIM_MEMMAX_C),
    #                 dbc.Col(id=ids.CORP_CLAIM_MEMMAX_P),
    #                 dbc.Col(
    #                     dcc.Graph(id=ids.CORP_CLAIM_MEMMAX_IND, figure={},
    #                               config={'displayModeBar': False})
    #                 )
    #             ], className='align-items-center text-center',
    #         ),
    #     ]
    # )

    """
    ROW - SCATTER PLOTS
    """
    # corp_claims_scatbox_card = dbc.Card(
    #     [
    #         dbc.Col(
    #             [
    #                 dcc.Graph(id=ids.CORP_CLAIM_SCATBOX),
    #             ],
    #         )
    #     ]
    # )



    return html.Div(
        [
            dbc.Row(
                [
                    title_box
                ], className='align-items-center mb-0'
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            period_dropdown_box
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
                            corp_daily_claims_card
                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            corp_annual_claims_card
                        ], width=5, className='border border-primary border-3 p-0',
                    )
                ], className='p-0 m-0', justify='evenly'
            ),

            dbc.Row(
                [
                    html.H3("CASHFLOW")
                ], className='text-primary text-center p-2 mt-3'
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            corp_daily_cashflow_card

                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            corp_annual_cashflow_card

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
                            corp_mem_participation_card

                        ], width=5, className='border border-primary border-3 p-0',
                    ),
                    dbc.Col(
                        [
                            corp_mem_charges_card

                        ], width=5, className='border border-primary border-3 p-0',
                    )
                ], className='p-0 m-0', justify='evenly'
            ),

        ],
    )


