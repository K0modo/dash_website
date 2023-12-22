from dash import html, dcc
import dash_bootstrap_components as dbc
from src.app.components import ids

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
   ROW 1 - MEDICAL CLAIMS PROCESSED
"""

corp_daily_claims_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=ids.CORP_DAILY_CLAIMS_CHART, figure={}, config={'displayModeBar': False})
                    ], width=12),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.P('Daily Claims Average', className='my-0'),
                        html.P(id=ids.CORP_DAILY_CLAIMS_AVERAGE, className='mb-0')
                    ], className=''),
                    dbc.Col([
                        html.P('Total Claims', className='my-0', ),
                        html.P(id=ids.CORP_DAILY_CLAIMS_SUM, className='mb-0')
                    ], className='text-end')
                ])
            ],
        )
    ]
)

corp_annual_claims_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=ids.CORP_ANNUAL_CLAIMS_CHART, figure={}, config={'displayModeBar': False})
                    ], width=12),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.P('YTD Period Average', className='my-0'),
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
   ROW 2 - CLAIMS PAID
"""

corp_daily_paid_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=ids.CORP_DAILY_PAID_CHART, figure={}, config={'displayModeBar': False})
                    ], width=12),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.P('Daily Paid Average', className='my-0'),
                        html.P(id=ids.CORP_DAILY_PAID_AVERAGE, className='mb-0')
                    ], className='fs-6'),
                    dbc.Col([
                        html.P('Total Paid', className='my-0', ),
                        html.P(id=ids.CORP_DAILY_PAID_SUM, className='mb-0')
                    ], className='fs-6 text-end')
                ])
            ],
        )
    ]
)

corp_annual_paid_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=ids.CORP_ANNUAL_PAID_CHART, figure={}, config={'displayModeBar': False})
                    ], width=12),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.P('YTD Period Average', className='my-0'),
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
    ROW 3 - MEMBER ACTIVITY    
"""
corp_period_member_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=ids.CORP_DAILY_MEMBER_CHART, figure={}, config={'displayModeBar': False})
                    ], width=12),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.P('Daily Member Average', className='my-0'),
                        html.P(id=ids.CORP_DAILY_MEMBER_AVERAGE, className='mb-0')
                    ], className='fs-6'),
                    dbc.Col([
                        html.P('Total Members', className='my-0', ),
                        html.P(id=ids.CORP_DAILY_MEMBER_SUM, className='mb-0')
                    ], className='fs-6 text-end')
                ])

            ]
        )
    ]
)

corp_annual_member_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id=ids.CORP_ANNUAL_MEMBER_CHART, figure={}, config={'displayModeBar': False})
                    ], width=12),
                ]),
                dbc.Row([
                    dbc.Col([
                        html.P('YTD Period Average', className='my-0'),
                        html.P(id=ids.CORP_ANNUAL_MEMBER_AVERAGE, className='mb-0')
                    ], className='fs-6'),
                    dbc.Col([
                        html.P('Annual Total', className='my-0', ),
                        html.P(id=ids.CORP_ANNUAL_MEMBER_SUM, className='mb-0')
                    ], className='fs-6 text-end')
                ])
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

