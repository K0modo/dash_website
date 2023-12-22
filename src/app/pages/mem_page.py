import dash
from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc

import pandas as pd

from src.app.tab_views_member import (
    tabs_menu_member,
    mem_tab_services,
    mem_tab_dashboard
)
from src.app.tab_views_member import mem_tab_claims

from src.app.components import (
    comp_graphs
)
from src.app.components import ids

from src.app.data.mem_data_calculations import MemberCalculations, GridStats

dash.register_page(__name__,
                   path='/member',
                   name='Member',
                   title='Member Claims',
                   description='Member claims statistics and details')




layout = dbc.Container(

    [
        html.Div(
            id='mem-app-container',
            children=[
                tabs_menu_member.render_member_tab_menu(),
                html.Div(id=ids.MEM_APP_CONTENT)
            ]
        )
    ]
)


"""  RENDER TABS  """

@callback(
    Output(ids.MEM_APP_CONTENT, 'children'),
    Input(ids.MEM_APP_TABS, 'active_tab'))
def render_tab_content(tab_selected):
    if tab_selected == ids.MEM_TAB_DASHBOARD:
        return mem_tab_dashboard.render_tab_dashboard_view()
    elif tab_selected == ids.MEM_TAB_SERVICES:
        return mem_tab_services.render_tab_services_view()
    else:
        return mem_tab_claims.render_tab_claims_view()



""" Create Dropdown to select Member 
- Data will be filtered based on member selected
"""

@callback(
    Output(ids.MEM_ACCT_DROPDOWN, 'options'),
    Input(ids.STORE_MEM_TABLE, 'data'))
def populate_member_dropdown(options):
    # print(options)
    return options


""" Data is loaded from file in Data directory and "stored" using dcc.Store component.
- Database (csv) is loaded into dcc.STORE(id=STORE_DATA) and then filtered by Member selected in dropdown.  
- The filtered data is returned to dcc.STORE(id=STORE_DATA_FILTER)

"""


@callback(
    Output(ids.MEM_TITLE_DASHBOARD, 'children'),
    Output(ids.STORE_MEM_ACCT, 'data'),
    Output(ids.STORE_DATA_FILTER, 'data'),
    Input(ids.MEM_ACCT_DROPDOWN, 'value'),
    State(ids.STORE_DATA, 'data')
)
def filter_store_data(member, store_data):
    df = pd.DataFrame(store_data)
    df_filter = df[df['mem_acct'] == member]

    title = f'Dashboard for Member ID 000{member}'
    # print(df_filter)
    return title, member, df_filter.to_dict('records')



####################################
##    CALLBACKS - DASHBOARD TAB   ##
####################################

""" Dashboard Section 1 - Simple Output
- DataFrame is passed to 'DataCalculations' class (mem_data_calculations.py) for data calculations.
- Class returns data or table
- Individual data statistics are formatted for currency and commas
- Table is passed to Graph (comp_graph.py) or Grid (comp_grids.py) function for processing and returned
- Data, Graphs or Grids are returned to Layout (mem_tab_dashboard.py)
"""


@callback(
    Output(ids.MEM_ANNUAL_CHARGE, 'children'),
    Output(ids.MEM_ANNUAL_CLAIMS, 'children'),
    Output(ids.MEM_ANNUAL_ITEMS, 'children'),
    Output(ids.MEM_DASH_BAR_CHARGE, 'figure'),
    Output(ids.MEM_DASH_BAR_CLAIMS, 'figure'),
    Output(ids.MEM_DASH_PIE_FACILITY, 'figure'),
    Output(ids.MEM_DASH_PIE_SPECIALTY, 'figure'),
    Output(ids.MEM_DASH_BAR_PURPOSE, 'figure'),

    Input(ids.STORE_DATA_FILTER, 'data'))
def populate_dashboard(store_data_filter):
    df = pd.DataFrame(store_data_filter)

    member_table = MemberCalculations(df)

    annual_charge = member_table.annual_charge_calc()
    annual_charge = f'${annual_charge:,.0f}',

    annual_claims = member_table.annual_claims_calc()
    annual_claims = f'{annual_claims}'

    annual_line_items = member_table.annual_line_items_calc()
    annual_line_items = f'{annual_line_items}'


    bar1_table = member_table.charge_by_period()
    bar1 = comp_graphs.make_dash_bar1(bar1_table)

    bar2_table = member_table.claims_by_period()
    bar2 = comp_graphs.make_dash_bar2(bar2_table)

    pie1_table = member_table.charge_by_facility_class()
    pie1 = comp_graphs.make_dash_pie1(pie1_table)

    pie2_table = member_table.count_by_specialty()
    pie2 = comp_graphs.make_dash_pie2(pie2_table)

    bar3_table = member_table.charge_by_injury_disease()
    bar3 = comp_graphs.make_dash_bar3(bar3_table)

    return annual_charge,\
           annual_claims, \
           annual_line_items, \
           bar1, \
           bar2, \
           pie1, \
           pie2, \
           bar3



"""  Dashboard Section 2 
- Graphs uses Radio Button to change the Y_axis to logrithmetic scale
- Data processing same as Section 1 with added function
"""


@callback(
    Output(ids.MEM_SPEC_BAR_CHARGE, 'figure'),
    Output(ids.MEM_SPEC_SCATTER, 'figure'),
    Input(ids.MEM_SPEC_BAR_RADIO, 'value'),
    Input(ids.MEM_SPEC_SCATTER_RADIO, 'value'),

    Input(ids.STORE_DATA_FILTER, 'data'),
)
def populate_dashboard_specialty(log_scale_bar, log_scale_scatter, store_data_filter):
    df = pd.DataFrame(store_data_filter)

    member_table = MemberCalculations(df)  # send data to Data_Calculations class
    charge_count_bar_table = member_table.charge_count_spec8()  # call func to get DATA from Data_Calculations class
    bar4 = comp_graphs.make_dash_bar4(charge_count_bar_table, log_scale_bar)  # Send data as arg to chart BUILD func
    spec_list = member_table.spec_nlargest_list8()
    scatter_table1 = member_table.spec_filter_to_list8()
    scatter1 = comp_graphs.make_dash_scatter1(scatter_table1, spec_list, log_scale_scatter)

    return bar4, scatter1




############################################
##    CALLBACKS - MEDICAL SERVICES TAB    ##
############################################


""" Specialty (tab_services_view) utilizes AG-Grid
- Main Statistics grid interacts with a "Claims" sub-grid and scatter plot.
- The AG Grid creates a "claims" history table/output from the dashGridOption:'rowSelection'.
- DataFrame is passed to 'GridStats' class in mem_data_calculations.py for data calculations.
- Class returns "grid_table" grouped by 'specialty'
"""


@callback(
    Output(ids.MEM_TITLE_SERVICES, 'children'),
    Output(ids.MEM_SERV_GRID1, 'rowData'),
    Output(ids.MEM_SERV_GRID1_TABLE, 'rowData'),
    Input(ids.STORE_MEM_ACCT, 'data'),
    Input(ids.STORE_DATA_FILTER, 'data'),
    Input(ids.MEM_SERV_GRID1, 'selectedRows')
)
def display_services_stats(member, store_data_filter, selected_row):
    df = pd.DataFrame(store_data_filter)

    title = f'Medical Services for Member ID 000{member}'

    mem_serv_stats = GridStats(df)
    mem_serv_stats = mem_serv_stats.calc_serv_stats()
    mem_serv_stats = mem_serv_stats.to_dict('records')

    if selected_row is None:
        specialty = 'General_Medicine'
    else:
        specialty = selected_row[0]['specialty']

    mem_claim_hist = GridStats(df)
    mem_claim_hist = mem_claim_hist.spec_claim_hist()
    mem_claim_hist = mem_claim_hist[mem_claim_hist['specialty'] == specialty]
    mem_claim_hist = mem_claim_hist.to_dict('records')

    return title, mem_serv_stats, mem_claim_hist



############################################
##     CALLBACKS - MEDICAL CLAIMS TAB     ##
############################################

@callback(
    Output(ids.MEM_TITLE_CLAIMS, 'children'),
    Output(ids.MEM_ANNUAL_CHARGEt, 'children'),
    Output(ids.MEM_ANNUAL_CLAIMSt, 'children'),
    Output(ids.MEM_ANNUAL_LINE_ITEMSt, 'children'),
    Input(ids.STORE_MEM_ACCT, 'data'),
    Input(ids.STORE_DATA_FILTER, 'data')
)
def display_claims(member, store_data_filter):
    df = pd.DataFrame(store_data_filter)

    title = f'Medical Claims for Member ID 000{member}'

    member_table = MemberCalculations(df)

    annual_charge = member_table.annual_charge_calc()
    annual_charge = f'${annual_charge:,.0f}',

    annual_claims = member_table.annual_claims_calc()
    annual_claims = f'{annual_claims}'

    annual_line_items = member_table.annual_line_items_calc()
    annual_line_items = f'{annual_line_items}'

    return title, annual_charge, annual_claims, annual_line_items


