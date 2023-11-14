from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

from src.app.components import (
    comp_grids
)
from src.app.components import ids

'''
Present Grid by Specialty
    - Charges
    - Count
    - Max
    - Average
    - Deduct/CoPay

Present Grid for Selected Specialty
    - Date
    - Claim_id
    - Charge
    - Deduct/CoPay

Present Scatter-Dot by Period for Selected Specialty

'''


def render_tab_services_view():
    title_box = html.Div(
        [
            html.H3('', ids.MEM_TITLE_SERVICES, className='text-primary text-center')
        ]
    )

    statistics_grid_title = html.Div([
        dbc.Card(
            [
                dbc.CardBody(
                    html.H4("Annual Member Statistics by Specialty", className='card-title text-center')
                )
            ],
            className='border-0'
        )
    ])

    statistics_grid = dag.AgGrid(
        id=ids.MEM_SERV_GRID1,
        defaultColDef=comp_grids.grid1_defaultColDef,
        columnDefs=comp_grids.grid1_columnDefs,
        columnSize='sizeToFit',
        style={'height': 600},
        dashGridOptions={
            'pagination': True,
            'paginationAutoPageSize': True,
            'rowSelection': 'single'
        },
    )

    specialty_claims_grid_title = html.Div([
        dbc.Card(
            [
                dbc.CardBody(
                    html.H4("Claims for Specialty Selected",
                            className='card-title text-center')
                )
            ],
            className='border-0'
        )
    ])

    specialty_claims_grid = dag.AgGrid(
        id=ids.MEM_SERV_GRID1_TABLE,
        columnDefs=comp_grids.spec_grid2_columnDefs,
        columnSize='sizeToFit'
    )

    return html.Div(
        [
            dbc.Row(
                [
                    title_box
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        statistics_grid_title
                    )
                ],
                className='mt-5'
            ),
            dbc.Row(
                statistics_grid
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            specialty_claims_grid_title,
                            specialty_claims_grid
                        ]
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id=ids.MEM_SERV_GRID1_GRAPH)
                        ]
                    )
                ]
            )
        ]
    )



