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
from src.app.models import ClaimsPaid, DailyClaims, DailyMember, PeriodSummary, PeriodMember

dash.register_page(__name__,
                   path='/corporate',
                   name='Corporate',
                   title='Corporate',
                   description='Corporate Level Claim Data'
                   )


# layout = dbc.Container([
#
#     'Page_1 Container',
#     html.Br(),
#     html.Div(children='My First App with Dash & SqlAlchemy'),
#     html.Hr(),
#     dcc.Dropdown(
#             id=ids.CORP_PERIOD_DROPDOWN,
#             options=[1,2,3,4,5,6,7,8,9,10,11,12],
#             value=1,
#             clearable=False,
#             persistence='session',
#             style={'width': '50px'}
#         ),
#     dcc.Graph(id=ids.CORP_DAILY_CLAIMS_MONTH)
#     # dcc.RadioItems(options=['charge_allowed', 'deduct_copay'], value='charge_allowed', id='controls'),
#     # dcc.Graph(id='first-graph')
#
# ])

# @callback(
#         Output(ids.CORP_DAILY_CLAIMS_MONTH, component_property='figure'),
#         Input(ids.CORP_PERIOD_DROPDOWN, component_property='value')
#     )
# def update_graph(period_chosen):
#     daily_per = (db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.count)
#                                     .where(DailyClaims.period == period_chosen)))
#     daily_per_df = pd.DataFrame(daily_per)
#     fig = px.bar(daily_per_df, x='charge_trans_date', y='count')

#     # query = db.session.query(
#     #     ClaimsPaid.period,
#     #     sa.func.avg(getattr(ClaimsPaid, col_chosen)).label('measure')).group_by(ClaimsPaid.period).all()
#     # x = [q.period for q in query]
#     # y = [q.measure for q in query]
#     # fig = go.Figure([go.Bar(x=x, y=y)])
#     return fig


#######################################################################
#######################################################################


layout = dbc.Container(
    [
        html.Div(
            id='corp-app-container',
            children=[
                tmc.render_corporate_tab_menu(),
                html.Div(id=ids.CORP_APP_CONTENT)
            ]
        )
    ]
)

""" Callback 1 - Link to Tabs """

@callback(
    Output(ids.CORP_APP_CONTENT, 'children'),
    Input(ids.CORP_APP_TABS, 'active_tab')
)
def render_tab_content(tab_selected):
    if tab_selected == ids.CORP_TAB_DASHBOARD:
        return corp_tab_dashboard.render_corp_tab_dashboard()


@callback(
    Output(ids.CORP_DAILY_CLAIMS_CHART, 'figure'),
    Output(ids.CORP_DAILY_CLAIMS_AVERAGE, 'children'),
    Output(ids.CORP_DAILY_CLAIMS_SUM, 'children'),
    Output(ids.CORP_ANNUAL_CLAIMS_CHART, 'figure'),
    Output(ids.CORP_ANNUAL_CLAIMS_AVERAGE, 'children'),
    Output(ids.CORP_ANNUAL_CLAIMS_SUM, 'children'),

    Output(ids.CORP_DAILY_PAID_CHART, 'figure'),
    Output(ids.CORP_DAILY_PAID_AVERAGE, 'children'),
    Output(ids.CORP_DAILY_PAID_SUM, 'children'),
    Output(ids.CORP_ANNUAL_PAID_CHART, 'figure'),
    Output(ids.CORP_ANNUAL_PAID_AVERAGE, 'children'),
    Output(ids.CORP_ANNUAL_PAID_SUM, 'children'),

    Output(ids.CORP_DAILY_MEMBER_CHART, 'figure'),
    Output(ids.CORP_DAILY_MEMBER_AVERAGE, 'children'),
    Output(ids.CORP_DAILY_MEMBER_SUM, 'children'),

    Output(ids.CORP_MEM_CHARGE_CHART, 'figure'),

    Input(ids.CORP_PERIOD_DROPDOWN, 'value')
)
def update_graph(period_chosen):

    # ROW 1 - MEDICAL CLAIMS PROCESSED
    # ROW 1 - COLUMN 1

    daily_claims = (db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.claims_count)
                                    .where(DailyClaims.period == period_chosen)))
    daily_claims_chart = pd.DataFrame(daily_claims)
    daily_claims_chart = px.bar(daily_claims_chart, x='charge_trans_date', y='claims_count')
    daily_claims_average = (db.session.execute(db.select(PeriodSummary.claims_daily_avg)
                                  .where(PeriodSummary.period == period_chosen)).scalar())
    daily_claims_sum = (db.session.execute(db.select(PeriodSummary.claims_period_count)
                                .where(PeriodSummary.period == period_chosen)).scalar())

    # ROW 1 - COLUMN 2

    annual_claims = (db.session.execute(db.select(PeriodSummary.period, PeriodSummary.claims_period_count)
                                      .order_by(PeriodSummary.period)))
    annual_claims_chart = pd.DataFrame(annual_claims)
    # print(annual_claims_chart)
    annual_claims_chart = px.bar(annual_claims_chart, x='period', y='claims_period_count')
    annual_claims_average = (db.session.execute(db.select(PeriodSummary.claims_period_average_cum)
                                                .where(PeriodSummary.period == 12)).scalar())
    annual_claims_sum = (db.session.execute(db.select(PeriodSummary.claims_period_count_cum)
                                                .where(PeriodSummary.period == 12)).scalar())


    # ROW 2 - CASHFLOW

    # ROW 2 - COLUMN 1

    daily_paid = db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.charges_paid)
                                                .where(DailyClaims.period == period_chosen))
    daily_paid_chart = pd.DataFrame(daily_paid)
    daily_paid_chart = px.bar(daily_paid_chart, x='charge_trans_date', y='charges_paid')
    daily_paid_average = (db.session.execute(db.select(PeriodSummary.claims_paid_daily_avg)
                                                .where(PeriodSummary.period == period_chosen)).scalar())
    daily_paid_sum = (db.session.execute(db.select(PeriodSummary.claims_period_paid)
                                                .where(PeriodSummary.period == period_chosen)).scalar())


    # ROW 2 COLUMN 2

    annual_paid = db.session.execute(db.select(PeriodSummary.period, PeriodSummary.claims_period_paid))
    annual_paid_chart = pd.DataFrame(annual_paid)
    annual_paid_chart = px.bar(annual_paid_chart, x='period', y='claims_period_paid')
    annual_paid_average = (db.session.execute(db.select(PeriodSummary.claims_period_paid_average_cum)
                                              .where(PeriodSummary.period == 12)).scalar())
    annual_paid_sum = (db.session.execute(db.select(PeriodSummary.claims_period_paid_cum)
                                              .where(PeriodSummary.period == 12)).scalar())



    # ROW 3 - MEMBER PARTICIPATION

    # ROW 3 - COLUMN 1

    daily_member = db.session.execute(db.select(DailyMember.charge_trans_date, DailyMember.member_count)
                                              .where(DailyMember.period == period_chosen))
    daily_member_chart = pd.DataFrame(daily_member)
    daily_member_chart = px.bar(daily_member_chart, x='charge_trans_date', y='member_count')
    daily_member_average = 100
    daily_member_sum = 1000

    # ROW 3 - COLUMN 2

    mem_charges = (db.session.execute(db.select(PeriodMember.period, sa.func.count(PeriodMember.mem_acct_id.distinct()),
                                                sa.func.avg(PeriodMember.charges_member))
                                      .group_by(PeriodMember.period)
                                      ))
    mem_charges_df = pd.DataFrame(mem_charges)
    mem_charges_df['avg'] = mem_charges_df['avg'].astype(int)
    mem_charges_fig = px.bar(mem_charges_df, x='period', y='avg')

    return daily_claims_chart, daily_claims_average, daily_claims_sum, annual_claims_chart, annual_claims_average, annual_claims_sum, \
           daily_paid_chart, daily_paid_average, daily_paid_sum, annual_paid_chart, annual_paid_average, annual_paid_sum, \
           daily_member_chart, daily_member_average, daily_member_sum,  mem_charges_fig,




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

