import dash

import pandas as pd
from dash import html, dcc, Input, Output, callback

import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from src.app.components import ids

from src.app.corp_tab_views import tabs_menu_corporate as tmc, corp_tab_dashboard

from src.app.data.corp_data_calculations import CorporateCalculations

from src.app.server import db
import sqlalchemy as sa
from src.app.models import ClaimsPaid

dash.register_page(__name__,
                   path='/corporate',
                   name='Corporate',
                   title='Corporate',
                   description='Corporate Level Claim Data'
                   )


layout = dbc.Container([

    'Page_1 Container',
    html.Br(),
    html.Div(children='My First App with Dash & SqlAlchemy'),
    html.Hr(),
    dcc.RadioItems(options=['charge_allowed', 'deduct_copay'], value='charge_allowed', id='controls'),
    dcc.Graph(id='first-graph')

])

@callback(
        Output(component_id='first-graph', component_property='figure'),
        Input(component_id='controls', component_property='value')
    )
def update_graph(col_chosen):
    query = db.session.query(
        ClaimsPaid.period,
        sa.func.avg(getattr(ClaimsPaid, col_chosen)).label('measure')).group_by(ClaimsPaid.period).all()
    x = [q.period for q in query]
    y = [q.measure for q in query]
    fig = go.Figure([go.Bar(x=x, y=y)])
    return fig


#######################################################################
#######################################################################


# layout = dbc.Container(
#     [
#         html.Div(
#             id='corp-app-container',
#             children=[
#                 tmc.render_corporate_tab_menu(),
#                 html.Div(id=ids.CORP_APP_CONTENT)
#             ]
#         )
#     ]
# )
#
# """ Callback 1 - Link to Tabs """
#
# @callback(
#     Output(ids.CORP_APP_CONTENT, 'children'),
#     Input(ids.CORP_APP_TABS, 'active_tab')
# )
# def render_tab_content(tab_selected):
#     if tab_selected == ids.CORP_TAB_DASHBOARD:
#         return corp_tab_dashboard.render_corp_tab_dashboard()
#
#
# """  CARD ICON """
#
#
# @callback(
#     Output(ids.CORP_CARD_CLAIM_IND, 'figure'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def update_corp_card_claim_indicator(store_data):
#     df_corp = pd.DataFrame(store_data)
#     # pd.read_sql_table('claimscounttable', con=engine)
#
#     df_claims = CorporateCalculations(df_corp)
#     df_claims = df_claims.claims_volume_ytd()
#
#     ytd_ave = df_claims.iloc[-1,3]
#     cur_month = df_claims.iloc[-1, 1]
#
#     fig = go.Figure(go.Indicator(
#         mode='delta',
#         value=cur_month,
#         delta={'reference': ytd_ave, 'relative': True, 'valueformat': '.1%'}
#     ))
#     fig.update_traces(delta_font={'size': 14})
#     fig.update_layout(height=30, width=70)
#
#     if cur_month >= ytd_ave:
#         fig.update_traces(delta_increasing_color='green')
#     elif cur_month < ytd_ave:
#         fig.update_traces(delta_decreasing_color='red')
#
#     return fig
#
#
# @callback(
#     Output(ids.CORP_CARD_CLAIM_CHART, 'figure'),
#     Output(ids.CORP_CARD_CLAIM_START, 'children'),
#     Output(ids.CORP_CARD_CLAIM_END, 'children'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def update_corp_card_claim_chart(store_data):
#     df_corp = pd.DataFrame(store_data)
#     period = 12
#
#     df_claims_date = df_corp[df_corp.period == period]
#     df_claims_date = CorporateCalculations(df_claims_date)
#     df_claims_date = df_claims_date.claims_volume_period()
#
#     df_claims = CorporateCalculations(df_corp)
#     df_claims = df_claims.claims_volume_ytd()
#
#     cur_mo_claims = df_claims.iloc[-1,1]
#     prior_mo_claims = df_claims.iloc[-2,1]
#     ytd_ave = df_claims.iloc[-2,3]
#     ytd_ave = f'{ytd_ave:,}'
#     cur_mo = f'{cur_mo_claims:,}'
#
#     fig = px.line(df_claims_date, x='trans_date', y='CLAIMS_DAILY',
#                   height=120)
#     fig.update_layout(margin=dict(t=0, r=0, l=0, b=20),
#                       paper_bgcolor='rgba(0,0,0,0)',
#                       plot_bgcolor='rgba(0,0,0,0)',
#                       yaxis=dict(
#                           title=None,
#                           showgrid=False,
#                           showticklabels=False
#                       ),
#                       xaxis=dict(
#                           title=None,
#                           showgrid=False,
#                           showticklabels=False
#                       )
#                       )
#
#     if cur_mo_claims >= prior_mo_claims:
#         return fig.update_traces(fill='tozeroy', line={'color':'green'}),\
#                ytd_ave, \
#                cur_mo
#
#     elif cur_mo_claims < prior_mo_claims:
#         return fig.update_traces(fill='tozeroy', line={"color": 'red'}), \
#                ytd_ave, \
#                cur_mo
#
#
# @callback(
#     Output(ids.CORP_CLAIM_MEM25_C, 'children'),
#     Output(ids.CORP_CLAIM_MEM25_P, 'children'),
#     Output(ids.CORP_CLAIM_MEM25_IND, 'figure'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def display_table_mem25(store_data):
#     df_corp = pd.DataFrame(store_data)
#     period = 12
#
#     df_claims = CorporateCalculations(df_corp)
#     df_claims = df_claims.claims_member_period()
#     df_claims_c = df_claims.loc[:, period].sort_values(ascending=False).iloc[:24].sum().astype(int)
#     df_claims_cs = f'{df_claims_c:,}'
#     df_claims_p = df_claims.loc[:, period-1].sort_values(ascending=False).iloc[:24].sum().astype(int)
#     df_claims_ps = f'{df_claims_p:,}'
#
#     fig = go.Figure(go.Indicator(
#         mode='delta',
#         value=df_claims_c,
#         delta={'reference': df_claims_p, 'relative': True, 'valueformat': '.1%'}
#     ))
#     fig.update_traces(delta_font={'size': 16})
#     fig.update_layout(height=25)
#
#     if df_claims_c >= df_claims_p:
#         fig.update_traces(delta_increasing_color='green')
#     elif df_claims_c < df_claims_p:
#         fig.update_traces(delta_decreasing_color='red')
#
#     return df_claims_cs, df_claims_ps, fig
#
#
# @callback(
#     Output(ids.CORP_CLAIM_MEMMAX_C, 'children'),
#     Output(ids.CORP_CLAIM_MEMMAX_P, 'children'),
#     Output(ids.CORP_CLAIM_MEMMAX_IND, 'figure'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def display_table_memmax(store_data):
#     df_corp = pd.DataFrame(store_data)
#     period = 12
#
#     df_claims = CorporateCalculations(df_corp)
#     df_claims = df_claims.claims_member_period()
#     df_claims_c = int(df_claims[period].max())
#     df_claims_cs = f'{df_claims_c:,}'
#     df_claims_p = int(df_claims[period - 1].max())
#     df_claims_ps = f'{df_claims_p:,}'
#
#     fig = go.Figure(go.Indicator(
#         mode='delta',
#         value=df_claims_c,
#         delta={'reference': df_claims_p, 'relative': True, 'valueformat': '.1%'}
#     ))
#     fig.update_traces(delta_font={'size': 16})
#     fig.update_layout(height=25)
#
#     if df_claims_c >= df_claims_p:
#         fig.update_traces(delta_increasing_color='green')
#     elif df_claims_c < df_claims_p:
#         fig.update_traces(delta_decreasing_color='red')
#
#     return df_claims_cs, df_claims_ps, fig
#
# @callback(
#     Output(ids.CORP_CLAIM_SCATBOX, 'figure'),
#     # Output(ids.TEST_DIV1, 'children'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def display_claims_boxplot(store_data):
#     df_corp = pd.DataFrame(store_data)
#
#     df_box = CorporateCalculations(df_corp)
#     df_box = df_box.claims_member_quarter()
#
#     fig = go.Figure()
#     fig.add_trace(go.Box(x=df_box.Q1, name='Q1'))
#     fig.add_trace(go.Box(x=df_box.Q2, name='Q2'))
#     fig.add_trace(go.Box(x=df_box.Q3, name='Q3'))
#     fig.add_trace(go.Box(x=df_box.Q4, name='Q4'))
#     fig.update_layout(
#         title=dict(text= 'Claims per Member by Quarter', x=0.5, y=.95),
#         showlegend=False,
#         margin=dict(t=40, r=0, l=0, b=0),
#         plot_bgcolor='rgba(80,157,199,.3)',
#     )
#
#     return fig
#
# ######  END OF CLAIMS  ######
#
#
# ######  START OF CHARGES  #####
#
# @callback(
#     Output(ids.CORP_CARD_CHARGE_IND, 'figure'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def update_corp_card_charge_indicator(store_data):
#     df_corp = pd.DataFrame(store_data)
#
#     df_charges = CorporateCalculations(df_corp)
#     df_charges = df_charges.claims_charges_ytd()
#
#     move_ave = df_charges.iloc[-1,3]
#     cur_month = df_charges.iloc[-1, 1]
#
#     fig = go.Figure(go.Indicator(
#         mode='delta',
#         value=cur_month,
#         delta={'reference': move_ave, 'relative': True, 'valueformat': '.1%'}
#     ))
#     fig.update_traces(delta_font={'size': 14})
#     fig.update_layout(height=30, width=70)
#
#     if cur_month <= move_ave:
#         fig.update_traces(delta_increasing_color='green')
#     elif cur_month > move_ave:
#         fig.update_traces(delta_decreasing_color='red')
#
#     return fig
#
#
# @callback(
#     Output(ids.CORP_CARD_CHARGE_CHART, 'figure'),
#     Output(ids.CORP_CARD_CHARGE_START, 'children'),
#     Output(ids.CORP_CARD_CHARGE_END, 'children'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def update_corp_card_charges_chart(store_data):
#     df_corp = pd.DataFrame(store_data)
#     period = 12
#
#     df_charges_date = df_corp[df_corp.period == period]
#     df_charges_date = CorporateCalculations(df_charges_date)
#     df_charges_date = df_charges_date.claims_charges_period()
#
#     df_charges = CorporateCalculations(df_corp)
#     df_charges = df_charges.claims_charges_ytd()
#
#     end_ave_charges = df_charges.iloc[-1,2]
#     end_ave_charges = f'${end_ave_charges:,.0f}'
#     start_ave_charges = df_charges.iloc[-2,2]
#     start_ave_charges = f'${start_ave_charges:,.0f}'
#
#
#     fig = px.line(df_charges_date, x='trans_date', y='CLAIM_CHARGE_AVE',
#                   height=120)
#     fig.update_layout(margin=dict(t=0, r=0, l=0, b=20),
#                       paper_bgcolor='rgba(0,0,0,0)',
#                       plot_bgcolor='rgba(0,0,0,0)',
#                       yaxis=dict(
#                           title=None,
#                           showgrid=False,
#                           showticklabels=False
#                       ),
#                       xaxis=dict(
#                           title=None,
#                           showgrid=False,
#                           showticklabels=False
#                       )
#                       )
#
#     if end_ave_charges <= start_ave_charges:
#         return fig.update_traces(fill='tozeroy', line={'color':'green'}),\
#                start_ave_charges, \
#                end_ave_charges
#
#     elif end_ave_charges > start_ave_charges:
#         return fig.update_traces(fill='tozeroy', line={"color": 'red'}), \
#                start_ave_charges, \
#                end_ave_charges
#
#
#
#
# @callback(
#     Output(ids.CORP_CHARGE_MEM25_C, 'children'),
#     Output(ids.CORP_CHARGE_MEM25_P, 'children'),
#     Output(ids.CORP_CHARGE_MEM25_IND, 'figure'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def display_charge_mem25(store_data):
#     df_corp = pd.DataFrame(store_data)
#     period = 12
#
#     df_charges = CorporateCalculations(df_corp)
#     df_charges = df_charges.charges_member_period()
#     df_charges_c = df_charges.loc[:, period].sort_values(ascending=False).iloc[:24].sum().astype(int)
#     df_charges_cs = f'{df_charges_c:,}'
#     df_charges_p = df_charges.loc[:, period-1].sort_values(ascending=False).iloc[:24].sum().astype(int)
#     df_charges_ps = f'{df_charges_p:,}'
#
#
#     fig = go.Figure(go.Indicator(
#         mode='delta',
#         value=df_charges_c,
#         delta={'reference': df_charges_p, 'relative': True, 'valueformat': '.1%'}
#     ))
#     fig.update_traces(delta_font={'size': 16})
#     fig.update_layout(height=25)
#
#     if df_charges_c >= df_charges_p:
#         fig.update_traces(delta_increasing_color='green')
#     elif df_charges_c < df_charges_p:
#         fig.update_traces(delta_decreasing_color='red')
#
#     return df_charges_cs, df_charges_ps, fig












# @callback(
#     Output(ids.CORP_CLAIM_MEMQUART_C, 'children'),
#     Output(ids.CORP_CLAIM_MEMQUART_P, 'children'),
#     Output(ids.CORP_CLAIM_MEMQUART_IND, 'figure'),
#     Input(ids.STORE_CORP_DATA, 'data')
# )
# def display_table_memquart(store_data):
#     df_corp = pd.DataFrame(store_data)
#     period = 12
#
#     df_claims = CorporateCalculations(df_corp)
#     df_claims = df_claims.claims_volume_table()
#     df_claims_c = df_claims[period].max()
#     df_claims_cs = f'{df_claims_c:,}'
#     df_claims_p = df_claims[period - 1].max()
#     df_claims_ps = f'{df_claims_p:,}'
#
#
#
#     fig = go.Figure(go.Indicator(
#         mode='delta',
#         value=df_claims_c,
#         delta={'reference': df_claims_p, 'relative': True, 'valueformat': '.1%'}
#     ))
#     fig.update_traces(delta_font={'size': 16})
#     fig.update_layout(height=25)
#
#     if df_claims_c >= df_claims_p:
#         fig.update_traces(delta_increasing_color='green')
#     elif df_claims_c < df_claims_p:
#         fig.update_traces(delta_decreasing_color='red')
#
#     return df_claims_cs, df_claims_ps, fig

