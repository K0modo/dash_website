import dash

import pandas as pd
from dash import html, dcc, Input, Output, callback

import dash_bootstrap_components as dbc
from src.app.components import corp_graphs
import plotly.graph_objects as go
import plotly.express as px
from src.app.components import ids

from src.app.tab_views_corporate import tabs_menu_corporate as tmc, corp_tab_dashboard, corp_tab_services

from src.app.server import db
import sqlalchemy as sa
from src.app.models import (Claims, ClaimsPaid,
                            DailyClaims, DailyMember,
                            PeriodSummary, PeriodMember, MemberSummary,
                            InjuryDisease, InjuryDiseaseSummary, InjuryDiseaseRacing,
                            SpecialtySummary, SpecialtyRacing,
                            FacilitySummary, FacilityRacing)

dash.register_page(__name__,
                   path='/corporate',
                   name='Corporate',
                   title='Corporate',
                   description='Corporate Level Claim Data'
                   )


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

""" Callback 1 - Call for Tabs """


@callback(
    Output(ids.CORP_APP_CONTENT, 'children'),
    Input(ids.CORP_APP_TABS, 'active_tab')
)
def render_tab_content(tab_selected):
    if tab_selected == ids.CORP_TAB_DASHBOARD:
        return corp_tab_dashboard.render_corp_tab_dashboard()
    if tab_selected == ids.CORP_TAB_SERVICES:
        return corp_tab_services.render_corp_tab_services()


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

    Output(ids.CORP_ANNUAL_MEMBER_CHART, 'figure'),
    Output(ids.CORP_ANNUAL_MEMBER_AVERAGE, 'children'),
    Output(ids.CORP_ANNUAL_MEMBER_SUM, 'children'),

    Input(ids.CORP_PERIOD_DROPDOWN, 'value')
)
def update_graph(period_chosen):
    # ROW 1 - MEDICAL CLAIMS PROCESSED
    # ROW 1 - COLUMN 1

    daily_claims = (db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.claims_count)
                                       .where(DailyClaims.period == period_chosen)))
    daily_claims_chart = pd.DataFrame(daily_claims)
    daily_claims_chart = corp_graphs.make_daily_claims_chart(daily_claims_chart)

    daily_claims_average = (db.session.execute(db.select(PeriodSummary.claims_daily_avg)
                                               .where(PeriodSummary.period == period_chosen)).scalar())
    daily_claims_average = f"{daily_claims_average:,.0f}"

    daily_claims_sum = (db.session.execute(db.select(PeriodSummary.claims_period_count)
                                           .where(PeriodSummary.period == period_chosen)).scalar())
    daily_claims_sum = f"{daily_claims_sum:,.0f}"

    # ROW 1 - COLUMN 2

    annual_claims = (db.session.execute(db.select(PeriodSummary.period, PeriodSummary.claims_period_count)
                                        .order_by(PeriodSummary.period)))
    annual_claims_chart = pd.DataFrame(annual_claims)
    annual_claims_chart = corp_graphs.make_annual_claims_chart(annual_claims_chart)

    # annual_claims_chart = px.bar(annual_claims_chart, x='period', y='claims_period_count')
    annual_claims_average = (db.session.execute(db.select(PeriodSummary.claims_period_average_cum)
                                                .where(PeriodSummary.period == 12)).scalar())
    annual_claims_average = f"{annual_claims_average:,.0f}"
    annual_claims_sum = (db.session.execute(db.select(PeriodSummary.claims_period_count_cum)
                                            .where(PeriodSummary.period == 12)).scalar())
    annual_claims_sum = f"{annual_claims_sum:,.0f}"

    # ROW 2 - MEDICAL CLAIMS PAID

    # ROW 2 - COLUMN 1

    daily_paid = db.session.execute(db.select(DailyClaims.charge_trans_date, DailyClaims.charges_paid)
                                    .where(DailyClaims.period == period_chosen))
    daily_paid_chart = pd.DataFrame(daily_paid)
    daily_paid_chart = corp_graphs.make_daily_paid_chart(daily_paid_chart)

    daily_paid_average = (db.session.execute(db.select(PeriodSummary.claims_paid_daily_avg)
                                             .where(PeriodSummary.period == period_chosen)).scalar())
    daily_paid_average = f"${daily_paid_average:,.0f}"
    daily_paid_sum = (db.session.execute(db.select(PeriodSummary.claims_period_paid)
                                         .where(PeriodSummary.period == period_chosen)).scalar())
    daily_paid_sum = f"${daily_paid_sum:,.0f}"

    # ROW 2 COLUMN 2

    annual_paid = db.session.execute(db.select(PeriodSummary.period, PeriodSummary.claims_period_paid))
    annual_paid_chart = pd.DataFrame(annual_paid)
    annual_paid_chart = corp_graphs.make_annual_paid_chart(annual_paid_chart)

    annual_paid_average = (db.session.execute(db.select(PeriodSummary.claims_period_paid_average_cum)
                                              .where(PeriodSummary.period == 12)).scalar())
    annual_paid_average = f"${annual_paid_average:,.0f}"
    annual_paid_sum = (db.session.execute(db.select(PeriodSummary.claims_period_paid_cum)
                                          .where(PeriodSummary.period == 12)).scalar())
    annual_paid_sum = f"${annual_paid_sum:,.0f}"

    # ROW 3 - MEMBER PARTICIPATION

    # ROW 3 - COLUMN 1

    daily_member = db.session.execute(db.select(DailyMember.charge_trans_date, DailyMember.member_count)
                                      .where(DailyMember.period == period_chosen))
    daily_member_chart = pd.DataFrame(daily_member)
    daily_member_chart = corp_graphs.make_daily_member_chart(daily_member_chart)

    daily_member_average = (db.session.execute(db.select(MemberSummary.daily_member_avg)
                                               .where(MemberSummary.period == period_chosen)).scalar())
    daily_member_average = f"{daily_member_average:,.0f}"

    daily_member_sum = (db.session.execute(db.select(MemberSummary.daily_member_sum)
                                           .where(MemberSummary.period == period_chosen)).scalar())
    daily_member_sum = f"{daily_member_sum:,.0f}"

    # ROW 3 - COLUMN 2

    annual_member = (db.session.execute(db.select(MemberSummary.period, MemberSummary.daily_member_sum)))
    annual_member_chart = pd.DataFrame(annual_member)
    annual_member_chart = corp_graphs.make_annual_member_chart(annual_member_chart)

    annual_member_average = db.session.execute(db.select(MemberSummary.annual_ytd_avg)
                                               .where(MemberSummary.period == 12)).scalar()
    annual_member_average = f"{annual_member_average:,.0f}"
    annual_member_sum = db.session.execute(db.select(sa.func.count(PeriodMember.mem_acct_id.distinct()))).scalar()
    annual_member_sum = f"{annual_member_sum:,.0f}"

    return daily_claims_chart, daily_claims_average, daily_claims_sum, \
           annual_claims_chart, annual_claims_average, annual_claims_sum, \
           daily_paid_chart, daily_paid_average, daily_paid_sum, \
           annual_paid_chart, annual_paid_average, annual_paid_sum, \
           daily_member_chart, daily_member_average, daily_member_sum, \
           annual_member_chart, annual_member_average, annual_member_sum


@callback(
    Output(ids.CORP_SERVICES_COUNT, 'figure'),
    Output(ids.CORP_SERVICES_PAID, 'figure'),
    Output(ids.CORP_SERVICES_RACING, 'figure'),

    Input(ids.CORP_SERVICES_DROPDOWN, 'value')
)
def update_services_icd(val):
    if val == 'Injury_Disease':
        icd_table = db.session.execute(db.select(InjuryDiseaseSummary.name,
                                                 InjuryDiseaseSummary.claim_count,
                                                 InjuryDiseaseSummary.claim_paid,
                                                 InjuryDiseaseSummary.color_code).order_by(
            InjuryDiseaseSummary.claim_count))
        icd_table = pd.DataFrame(icd_table)
        icd_table = icd_table.nlargest(10, 'claim_count').sort_values('claim_count')
        icd_count_chart = corp_graphs.make_services_icd_count_chart(icd_table)

        icd_table = icd_table.sort_values('claim_paid')
        icd_paid_chart = corp_graphs.make_services_icd_paid_chart(icd_table)

        # RACING CHART
        icd_racing_table = db.session.execute(db.select(InjuryDiseaseRacing.name, InjuryDiseaseRacing.period,
                                      InjuryDiseaseRacing.color_code,InjuryDiseaseRacing.claim_count_ytd))
        icd_racing_table = pd.DataFrame(icd_racing_table)
        icd_racing_chart = corp_graphs.make_services_icd_racing_chart(icd_racing_table)

        return icd_count_chart, icd_paid_chart, icd_racing_chart

    elif val == 'Specialty':
        specialty_table = (db.session.execute(db.select(SpecialtySummary.name, SpecialtySummary.claim_count,
                                                        SpecialtySummary.claim_paid,
                                                        SpecialtySummary.color_code)
                                              .order_by(SpecialtySummary.claim_count))
                           )
        specialty_table = pd.DataFrame(specialty_table)
        specialty_table = specialty_table[specialty_table['name'] != 'Hospital_Clinic']
        specialty_table = specialty_table.nlargest(10, 'claim_count').sort_values('claim_count')

        specialty_count_chart = corp_graphs.make_services_specialty_count_chart(specialty_table)

        specialty_table = specialty_table.sort_values('claim_paid')
        specialty_paid_chart = corp_graphs.make_services_specialty_paid_chart(specialty_table)

        # RACING CHART

        specialty_racing_table = db.session.execute(db.select(SpecialtyRacing.name, SpecialtyRacing.period,
                                                              SpecialtyRacing.color_code, SpecialtyRacing.claim_count_ytd))
        specialty_racing_table = pd.DataFrame(specialty_racing_table)
        specialty_racing_table = specialty_racing_table[specialty_racing_table['name'] != 'Hospital_Clinic']
        specialty_racing_chart = corp_graphs.make_services_specialty_racing_chart(specialty_racing_table)

        return specialty_count_chart, specialty_paid_chart, specialty_racing_chart

    else:
        facility_table = (db.session.execute(db.select(FacilitySummary.name, FacilitySummary.claim_count,
                                                        FacilitySummary.claim_paid,
                                                        FacilitySummary.color_code)
                                              .order_by(FacilitySummary.claim_count))
                           )
        facility_table = pd.DataFrame(facility_table)
        facility_table = facility_table[facility_table['name'] != 'Hospital']
        facility_table = facility_table.nlargest(5, 'claim_count').sort_values('claim_count')

        facility_count_chart = corp_graphs.make_services_facility_count_chart(facility_table)

        facility_table = facility_table.sort_values('claim_paid')
        facility_paid_chart = corp_graphs.make_services_facility_paid_chart(facility_table)

        # RACING CHART

        facility_racing_table = db.session.execute(db.select(FacilityRacing.name, FacilityRacing.period,
                                                              FacilityRacing.color_code,
                                                             FacilityRacing.claim_count_ytd))
        facility_racing_table = pd.DataFrame(facility_racing_table)
        facility_racing_table = facility_racing_table[facility_racing_table['name'] != 'Hospital']
        facility_racing_chart = corp_graphs.make_services_facility_racing_chart(facility_racing_table)

        return facility_count_chart, facility_paid_chart, facility_racing_chart




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
