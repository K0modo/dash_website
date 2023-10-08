import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/',
                   name='Home',
                   title='Portals',
                   description='Cards to Login'
                   )

member_card = dbc.Card(
    [
        dbc.CardImg(src='assets/images/member1.jfif', alt='healthcare_binder', top=True, style={'width': '100%', 'height':'15vw', 'object-fit':'cover'}),
        dbc.CardBody(
            [
                html.H4("Membership", className='card-title text-center'),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Annual Statement'),
                        dbc.ListGroupItem('Claim Summary'),
                        dbc.ListGroupItem('Claim Details'),
                        dbc.ListGroupItem('Statistics'),
                    ],
                    flush=True,
                ),
                dbc.Button('LOG IN', href='/member', color='primary', className='mt-4')
            ]
        )
    ],
    className='h-100'
)

administration_card = dbc.Card(
    [
        dbc.CardImg(src='assets/images/admin1.jfif', alt='administration', top=True, style={'width': '100%', 'height':'15vw', 'object-fit':'cover'}),
        dbc.CardBody(
            [
                html.H4("Administration", className='card-title text-center'),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Member Activity'),
                        dbc.ListGroupItem('Provider Activity'),
                        dbc.ListGroupItem('Cash Disbursed'),
                        dbc.ListGroupItem('Performance Metrics'),
                    ],
                    flush=True,
                ),
                dbc.Button('LOG IN', href='/corporate', color='primary', className='mt-4')
            ]
        )
    ],
    className='h-100'
)

analytics_card = dbc.Card(
    [
        dbc.CardImg(src='assets/images/data1.jfif', alt='healthcare_binder', top=True, style={'width': '100%', 'height':'15vw', 'object-fit':'cover'}),
        dbc.CardBody(
            [
                html.H4("Analytics", className='card-title text-center'),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem('Distribution'),
                        dbc.ListGroupItem('Heat Map'),
                        dbc.ListGroupItem('Correlation'),
                        dbc.ListGroupItem('Statistics'),
                    ],
                    flush=True,
                ),
                dbc.Button('LOG IN', href='/member', color='primary', className='mt-4')
            ]
        )
    ],
    className='h-100'
)

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1('Health Analytic Portals', className='mt-2 text-center'),
                className='my-3'
            )
        ),
        dbc.Row(
            [
                dbc.Col(member_card),
                dbc.Col(administration_card),
                dbc.Col(analytics_card)
            ]
        )
    ],
    className='mt-1'
)