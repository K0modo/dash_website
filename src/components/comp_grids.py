import dash_ag_grid as dag


"""  SPECIALTY GRID1 COLUMN DEFINITIONS  """

grid1_defaultColDef = {
    'editable': True,
    'sortable': True,
    'filter': True,
    # 'floatingFilter': True,
    'unSortIcon': True,
}

grid1_category_filterparams = {
    'closeOnApply': True,
    'debounceMs': 500,
    'buttons': ['apply', 'clear', 'reset', 'cancel'],
    'filterOptions': ['contains'],

}

grid1_columnDefs = [
    {
        'field': 'mem_acct',
        'headerName': 'Member',
        'filter': False,
        'width':70
    },
    {
        'field': 'specialty',
        'headerName': 'Specialty',
        'resizable': True,
        'filterParams': grid1_category_filterparams,
        'flex': 2

    },
    {
        'field': 'CHARGES',
        'headerName': 'Charges',
        'type': 'rightAligned',
        'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        'flex': 1
    },
    {
        'field': 'CLAIMS_COUNT',
        'headerName': 'Claims Count',
        'type': 'rightAligned',
        'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
        'flex': 1
    },
    {
        'field': 'AVERAGE',
        'headerName': 'Average Charge',
        'type': 'rightAligned',
        'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        'flex': 1
    },
    {
        'field': 'MAX',
        'headerName': 'Max Charge',
        'type': 'rightAligned',
        'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        'flex': 1
    },

    {
        'field': 'deduct_copay',
        'headerName': 'Deduct_CoPay',
        'type': ['rightAligned'],
        'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        'flex': 1
    },
]


""" The Callback returns "rowData" as a dictionary to this function -> 'make_spec_grid1'
    AG Grid 'rowSelection' option acts on "selectedRows" and "rowData" property"""

# def make_spec_grid1(id):
#
#     grid = dag.AgGrid(
#         id=id,
#         defaultColDef=grid1_defaultColDef,
#         columnDefs=grid1_columnDefs,
#         columnSize='sizeToFit',
#         style={'height': 600},
#         dashGridOptions={
#             'pagination': True,
#             'paginationAutoPageSize': True,
#             'rowSelection': 'single'
#         },
#     )
#
#     return grid

########################################################################################

"""  SPECIALTY GRID2 COLUMN DEFINITIONS  """

spec_grid2_defaultColDef = {
    'sortable': True,
    'filter': True,
    'floatingFilter': False,
    'unSortIcon': True,
}

spec_grid2_category_filterparams = {
    'closeOnApply': True,
    'debounceMs': 500,
    'buttons': ['apply', 'clear', 'reset', 'cancel'],
    'filterOptions': ['contains'],

}

spec_grid2_columnDefs = [
    {
        'field': 'specialty',
        'resizable': True,
        'filterParams': spec_grid2_category_filterparams,
        'flex': 2
    },
    {
        'field': 'trans_date',
    },
    {
        'field': 'claim_id',
        'filterParams': spec_grid2_category_filterparams,
        'width': 120
    },
    {
        'field': 'charge_allowed',
        'headerName': 'CHARGES',
        'type': 'rightAligned',
        'width': 120,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        'flex': 1
    },
    {
        'field': 'deduct_copay',
        'type': ['rightAligned'],
        'width': 130,
        'filter': 'agNumberColumnFilter',
        'valueFormatter': {"function": "d3.format('($,.0f')(params.value)"},
        'flex': 1
    },
]

# def make_spec_claims_hist(table):
#
#     grid = dag.AgGrid(
#         columnDefs=spec_grid2_columnDefs,
#         rowData=table.to_dict('records'),
#         columnSize='sizeToFit'
#     )
#
#     return grid