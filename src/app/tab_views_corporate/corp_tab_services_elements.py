from dash import html, dcc
import dash_bootstrap_components as dbc
from src.app.components import ids

title_box = html.H3("Corporate Services", id=ids.CORP_TITLE_SERVICES, className='text-primary text-center p-2')

icd_dropdown_box = html.Div(
    [
        html.H4("Select Category",
                className='text-primary'),
        dcc.Dropdown(
            id=ids.CORP_SERVICES_DROPDOWN,
            options=['Injury_Disease', 'Specialty', 'Facility'],
            value='Injury_Disease',
            clearable=False,
            persistence='session',
            style={'width': '150px'}
        )
    ], className='pt-0, mt-0'
)

corp_services_count_card = dbc.Card(
    [
        dcc.Graph(id=ids.CORP_SERVICES_COUNT)
    ]
)

corp_services_paid_card = dbc.Card(
    [
        dcc.Graph(id=ids.CORP_SERVICES_PAID)
    ]
)

corp_services_racing = dbc.Card(
    [
        dcc.Graph(id=ids.CORP_SERVICES_RACING)
    ]
)