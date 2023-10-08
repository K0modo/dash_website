from dash import html
import dash_bootstrap_components as dbc

from src.components import (
    ids,
    comp_tools,
)
from dash_extensions import Lottie

lottie_charges = "assets/images/lottie/animation_lmdrh57q.json"
lottie_claims = "assets/images/lottie/animation_lme0bab1.json"
lottie_items = "assets/images/lottie/animation_lme16ka1.json"

options = dict(loop=False, autoplay=False, rendererSettings=dict(preserveAspectRatio="xMidYMid slice"))


def render_tab_claims_view():

    return [
        html.Div(
            [
                dbc.Row(
                    [
                        html.H3('', ids.MEM_TITLE_CLAIMS, className='text-primary text-center')
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        Lottie(options=options, width='33%', height='33%', url=lottie_charges)                                            )
                                                ], className='d-flex align-items-center'
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.CardBody(
                                                        [
                                                            html.H4('Charges'),
                                                            html.H3('',ids.MEM_ANNUAL_CHARGEt)
                                                        ], className=''
                                                    )
                                                ], className='text-center text-primary'
                                            )
                                        ]
                                    )
                                ]
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        Lottie(options=options, width='33%', height='33%', url=lottie_claims)                                            )
                                                ], className='d-flex align-items-center'
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.CardBody(
                                                        [
                                                            html.H4('Claims'),
                                                            html.H3('',ids.MEM_ANNUAL_CLAIMSt)
                                                        ]
                                                    )
                                                ], className='text-center text-primary'
                                            )
                                        ]
                                    )
                                ],
                            ),
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        Lottie(options=options, width='60%', height='60%', url=lottie_items)                                            )
                                                ], className='d-flex align-items-center'
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.CardBody(
                                                        [
                                                            html.H4('Line Items'),
                                                            html.H3('',ids.MEM_ANNUAL_LINE_ITEMSt)
                                                        ]
                                                    )
                                                ], className='text-center text-primary'
                                            )
                                        ]
                                    )
                                ],
                            ),
                        ),
                    ],
                    id='stat-row-container',
                    className='d-flex g-5 mb-5'
                ),
            ]
        ),
    ]
