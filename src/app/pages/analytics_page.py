import dash
from dash import Dash, dcc, html, Input, Output, State, callback, dash_table
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from src.app.components import ids
from src.app.tab_views_analytics import (
    tabs_menu_analytic as tma,
    analytic_tab_dashboard as atd,
    analytic_tab_services as ats)
from src.app.components import ids

from src.app.server import db
import sqlalchemy as sa
from src.app.models import (Claims, ClaimsPaid,
                            DailyClaims, DailyMember,
                            PeriodSummary, PeriodMember, MemberSummary,
                            InjuryDisease, InjuryDiseaseSummary, InjuryDiseaseRacing,
                            SpecialtySummary, SpecialtyRacing,
                            FacilitySummary, FacilityRacing)

dash.register_page(__name__,
                   path='/analytics',
                   name='Analytics',
                   title='Analytics',
                   description='Analytical Data Analysis'
                   )


layout = dbc.Container(
    [
        html.Div(
            id='analytic-app-container',
            children=[
                tma.render_analytic_tab_menu(),
                html.Div(id=ids.ANALYTIC_APP_CONTENT)
            ]
        )
    ]
)

""" Callback 1 - Call for Tabs """

@callback(
    Output(ids.ANALYTIC_APP_CONTENT, 'children'),
    Input(ids.ANALYTIC_APP_TABS,'active_tab')
)
def render_tab_content(tab_selected):
    if tab_selected == ids.ANALYTIC_TAB_DASHBOARD:
        return atd.render_analytic_tab_dashboard()
    if tab_selected == ids.ANALYTIC_TAB_SERVICES:
        return ats.render_analytic_tab_services()


@callback(
    Output(ids.ANALYTIC_DASHBOARD_CHARGE_TABLE, 'children'),
    Input(ids.ANALYTIC_DASHBOARD_BUTTON, 'n_clicks')
)
def update_dashboard(click):
    if click > 0:
        stmt1 = db.session.execute(db.select(ClaimsPaid.charge_allowed, ClaimsPaid.charge_paid_ins,
                                             ClaimsPaid.deduct_copay))
        stmt1 = pd.DataFrame(stmt1)
        stmt1 = stmt1.describe()
        table = dash_table.DataTable(stmt1.to_dict('records'), [{'name': i, 'id': i} for i in stmt1.columns])

        return table




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