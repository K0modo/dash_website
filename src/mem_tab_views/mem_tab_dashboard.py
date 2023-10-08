from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd


from src.mem_tab_views import (
    tabs_menu_member,
    mem_tab_claims,
    mem_tab_services,
)

from src.components import (
    ids,
    comp_graphs,
    comp_tools,
    comp_grids
)

from src.data.mem_data_calculations import MemberCalculations, GridStats

from dash_extensions import Lottie

lottie_charges = "assets/images/lottie/animation_lmdrh57q.json"
lottie_claims = "assets/images/lottie/animation_lme0bab1.json"
lottie_items = "assets/images/lottie/animation_lme16ka1.json"

options = dict(loop=False, autoplay=True, rendererSettings=dict(preserveAspectRatio="xMidYMid slice"))

def render_tab_dashboard_view():



    member_dropdown_box = html.Div([
        html.H4('Select Member',
                className='text-primary'),

        dcc.Dropdown(
            id=ids.MEM_ACCT_DROPDOWN,
            options=[1,2,3,4],
            value=1,
            clearable=False,
            persistence='session',
            style={'width': '50px'}
        )
    ])

    title_box = html.Div([
        html.H3('', ids.MEM_TITLE_DASHBOARD, className='text-primary text-center')
    ])

    mem_ann_card = html.Div([
        dbc.Card([
            dbc.Row([
                dbc.Col([
                    html.Div(Lottie(options=options, width='53%', height='53%', url=lottie_charges))
                ], className='d-grid align-items-center'),
                dbc.Col([
                    dbc.CardBody([
                        html.H4('Charges'),
                        html.H3('',ids.MEM_ANNUAL_CHARGE)
                    ])
                ], className='text-center text-primary')
            ])
        ])
    ])

    mem_ann_claims = html.Div([
        dbc.Card([
            dbc.Row([
                dbc.Col([
                    html.Div(Lottie(options=options, width='33%', height='33%', url=lottie_claims))
                ], className='d-grid align-items-center'),
                dbc.Col([
                    dbc.CardBody([
                        html.H4('Claims'),
                        html.H3('', ids.MEM_ANNUAL_CLAIMS)
                    ])
                ], className='text-center text-primary')
            ])
        ])
    ])

    mem_ann_items = html.Div([
        dbc.Card([
            dbc.Row([
                dbc.Col([
                    html.Div(Lottie(options=options, width='53%', height='53%', url=lottie_items))
                ], className='d-grid align-items-center'),
                dbc.Col([
                    dbc.CardBody([
                        html.H4('Claim Items'),
                        html.H3(id=ids.MEM_ANNUAL_ITEMS)
                    ])
                ], className='text-center text-primary')
            ])
        ])
    ])

    specialty_section_title = html.Div([
        html.H3("Annual Summary of Charges by Specialty",
                className='text-center text-primary')
    ])

    specialty_bar_log_radio_box = html.Div([
        html.H6('Change scale to visualize small charges',
                className='mt-3 fw-bold'),
        html.Div(comp_tools.spec_log_radio(ids.MEM_SPEC_BAR_RADIO))
    ])

    specialty_scatter_log_radio_box = html.Div([
        html.H6('Change scale to visualize small charges',
                className='mt-3 fw-bold'),
        html.Div(comp_tools.spec_log_radio(ids.MEM_SPEC_SCATTER_RADIO))
    ])

    footer = html.Div([
        dbc.Card(
            dbc.CardBody([
                html.H4("Tynan HealthCare Portal",
                        className='card-title text-center')
            ], className='border-0')
        )
    ])


    return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                member_dropdown_box
                            ],
                            className='col-4'
                        ),
                        dbc.Col(
                            [
                                title_box
                            ],
                            className='col-4',
                        )
                    ],
                    id='title-container',
                    justify='start',
                    className='align-items-center my-4'
                ),
                dbc.Row(
                    [
                        dbc.Col(mem_ann_card),
                        dbc.Col(mem_ann_claims),
                        dbc.Col(mem_ann_items)
                    ],
                    id='stat-row-container',
                    className='g-5 mb-5'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(ids.MEM_DASH_BAR_CHARGE)
                            ]
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(ids.MEM_DASH_BAR_CLAIMS)
                            ]
                        )
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(ids.MEM_DASH_PIE_FACILITY)
                            ]
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(ids.MEM_DASH_PIE_SPECIALTY)
                            ]
                        )
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(ids.MEM_DASH_BAR_PURPOSE)
                            ]
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                specialty_section_title
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id=ids.MEM_SPEC_BAR_CHARGE)
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    [
                        specialty_bar_log_radio_box
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(id=ids.MEM_SPEC_SCATTER)
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        specialty_scatter_log_radio_box
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                footer
                            ]
                        )
                    ], className='my-5'
                )
            ],
        )

