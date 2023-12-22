import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

period_range = [0.1, 12]
title_font = dict(size=24)

font = {'size': 16}

yaxis_title = 'Count'
yaxis_currency = dict(tickprefix='$')
yaxis_comma = dict(separatethousands=True)


def make_daily_claims_chart(table):
    fig = px.bar(
        table,
        x=table['charge_trans_date'],
        y=table['claims_count'],
    )

    fig.update_layout(
        title='Daily Claims Processed',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title='Claims Processed',
        yaxis=yaxis_comma,
        # font=font
    )

    return fig


def make_annual_claims_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['claims_period_count'],
    )

    fig.update_layout(
        title='Annual Daily Claims',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title='Claims Processed',
        yaxis=yaxis_comma,
        # font=font
    )

    fig.update_xaxes(dtick=2)

    return fig


def make_daily_paid_chart(table):
    fig = px.bar(
        table,
        x=table['charge_trans_date'],
        y=table['charges_paid'],
    )

    fig.update_layout(
        title='Daily Claims Paid',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title='$  Claims Paid',
        yaxis=yaxis_comma,
        # font=font
    )

    return fig


def make_annual_paid_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['claims_period_paid'],
    )

    fig.update_layout(
        title='Annual Claims Paid',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title='$  Claims Paid',
        yaxis=yaxis_comma,
        # font=font
    )

    fig.update_xaxes(dtick=2)

    return fig


def make_daily_member_chart(table):
    fig = px.bar(
        table,
        x=table['charge_trans_date'],
        y=table['member_count'],
    )

    fig.update_layout(
        title='Daily Member Count',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title="# Members w/Claims",
        yaxis=yaxis_comma,
        # font=font
    )

    return fig


def make_annual_member_chart(table):
    fig = px.bar(
        table,
        x=table['period'],
        y=table['daily_member_sum'],
    )

    fig.update_layout(
        title='Annual Member Count',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title="# Members w/Claims",
        yaxis=yaxis_comma,
        # font=font
    )

    fig.update_xaxes(dtick=2)

    return fig


def make_services_icd_count_chart(table):

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=table['claim_count'],
            y=table['name'],
            orientation='h',
            marker_color=table['color_code']
        )
    )

    fig.update_layout(
        title='Injury_Disease Claim Count',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        yaxis_title="# Claims",
        xaxis=yaxis_comma,
        # font=font
    )

    # fig.update_xaxes(dtick=2)

    return fig

# https://sites.google.com/view/paztronomer/blog/basic/python-colors
def make_services_icd_paid_chart(table):

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=table['claim_paid'],
            y=table['name'],
            orientation='h',
            marker_color=table['color_code']
        )
    )

    fig.update_layout(
        title='Injury_Disease Claims Paid',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        # yaxis_title="",
        # xaxis=yaxis_comma,
        # font=font
    )

    # fig.update_xaxes(dtick=2)

    return fig


def make_services_icd_racing_chart(table):
    dict_keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    periods = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n_frame = {}

    for p, d in zip(periods, dict_keys):
        dataframe = table[(table['period'] == p)]
        dataframe = dataframe.nlargest(n=10, columns=['claim_count_ytd'])
        dataframe = dataframe.sort_values(by=['period', 'claim_count_ytd'])

        n_frame[d] = dataframe

    fig = go.Figure(
        data=[go.Bar(
            x=n_frame['one']['claim_count_ytd'],
            y=n_frame['one']['name'],
            orientation='h',
            text=n_frame['one']['claim_count_ytd'],
            texttemplate='%{text:,.0f}',
            textfont={'size': 18},
            textposition='inside',
            insidetextanchor='middle',
            width=0.8,
            marker={'color': n_frame['one']['color_code']}
        )],
        layout=go.Layout(
            xaxis=dict(range=[0, 8600], autorange=False, title=dict(text='claim_count', font=dict(size=18))),
            yaxis=dict(range=[-0.5, 9.5], autorange=False, tickfont=dict(size=18)),
            title=dict(text='Injury_Disease Category: Period 1', font=dict(size=28), x=0.5, xanchor='center'),
            # Button
            updatemenus=[dict(
                type='buttons',
                buttons=[dict(label='Play',
                              method='animate',
                              args=[None,
                                    {'frame': {'duration': 1000, 'redraw': True},
                                     "transition": {'duration': 250, 'easing': "linear"}}]
                              )],
                x=1.1,
            )]
        ),
        frames=[
            go.Frame(
                data=[
                    go.Bar(x=value['claim_count_ytd'], y=value['name'],
                           orientation='h',
                           text=value['claim_count_ytd'],
                           marker={'color': value['color_code']})
                ],
                layout=go.Layout(
                    xaxis=dict(range=[0, 8600], autorange=False),
                    yaxis=dict(range=[-0.5, 9.5], autorange=False, tickfont=dict(size=18)),
                    title=dict(text='Injury_Disease Category: Period ' + str(value['period'].values[0]),
                               font=dict(size=28))
                )
            )
            for key, value in n_frame.items()
        ]
    )

    return fig


def make_services_specialty_count_chart(table):

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=table['claim_count'],
            y=table['name'],
            orientation='h',
            marker_color=table['color_code']
        )
    )

    fig.update_layout(
        title='Specialty Claim Count',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        # yaxis_title="",
        xaxis=yaxis_comma,
        # font=font
    )

    # fig.update_xaxes(dtick=2)

    return fig


def make_services_specialty_paid_chart(table):

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=table['claim_paid'],
            y=table['name'],
            orientation='h',
            marker_color=table['color_code']
        )
    )

    fig.update_layout(
        title='Specialty Claims Paid',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        # yaxis_title="",
        # xaxis=yaxis_comma,
        # font=font
    )

    # fig.update_xaxes(dtick=2)

    return fig


def make_services_specialty_racing_chart(table):
    dict_keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    periods = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n_frame = {}

    for p, d in zip(periods, dict_keys):
        dataframe = table[(table['period'] == p)]
        dataframe = dataframe.nlargest(n=10, columns=['claim_count_ytd'])
        dataframe = dataframe.sort_values(by=['period', 'claim_count_ytd'])

        n_frame[d] = dataframe

    fig = go.Figure(
        data=[go.Bar(
            x=n_frame['one']['claim_count_ytd'],
            y=n_frame['one']['name'],
            orientation='h',
            text=n_frame['one']['claim_count_ytd'],
            texttemplate='%{text:,.0f}',
            textfont={'size': 18},
            textposition='inside',
            insidetextanchor='middle',
            width=0.8,
            marker={'color': n_frame['one']['color_code']}
        )],
        layout=go.Layout(
            xaxis=dict(range=[0, 8600], autorange=False, title=dict(text='claim_count', font=dict(size=18))),
            yaxis=dict(range=[-0.5, 9.5], autorange=False, tickfont=dict(size=18)),
            title=dict(text='Specialty Category: Period 1', font=dict(size=28), x=0.5, xanchor='center'),
            # Button
            updatemenus=[dict(
                type='buttons',
                buttons=[dict(label='Play',
                              method='animate',
                              args=[None,
                                    {'frame': {'duration': 1000, 'redraw': True},
                                     "transition": {'duration': 250, 'easing': "linear"}}]
                              )],
                x=1.1,
            )]
        ),
        frames=[
            go.Frame(
                data=[
                    go.Bar(x=value['claim_count_ytd'], y=value['name'],
                           orientation='h',
                           text=value['claim_count_ytd'],
                           marker={'color': value['color_code']})
                ],
                layout=go.Layout(
                    xaxis=dict(range=[0, 8600], autorange=False),
                    yaxis=dict(range=[-0.5, 9.5], autorange=False, tickfont=dict(size=18)),
                    title=dict(text='Specialty Category: Period ' + str(value['period'].values[0]),
                               font=dict(size=28))
                )
            )
            for key, value in n_frame.items()
        ]
    )

    return fig


def make_services_facility_count_chart(table):

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=table['claim_count'],
            y=table['name'],
            orientation='h',
            marker_color=table['color_code']
        )
    )

    fig.update_layout(
        title='Facility Claim Count',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        # yaxis_title="",
        xaxis=yaxis_comma,
        # font=font
    )

    # fig.update_xaxes(dtick=2)

    return fig


def make_services_facility_paid_chart(table):

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=table['claim_paid'],
            y=table['name'],
            orientation='h',
            marker_color=table['color_code']
        )
    )

    fig.update_layout(
        title='Facility Claims Paid',
        title_x=0.5,
        title_font=title_font,
        xaxis_title=None,
        # yaxis_title="",
        # xaxis=yaxis_comma,
        # font=font
    )

    # fig.update_xaxes(dtick=2)

    return fig


def make_services_facility_racing_chart(table):
    dict_keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    periods = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n_frame = {}

    for p, d in zip(periods, dict_keys):
        dataframe = table[(table['period'] == p)]
        dataframe = dataframe.nlargest(n=10, columns=['claim_count_ytd'])
        dataframe = dataframe.sort_values(by=['period', 'claim_count_ytd'])

        n_frame[d] = dataframe

    fig = go.Figure(
        data=[go.Bar(
            x=n_frame['one']['claim_count_ytd'],
            y=n_frame['one']['name'],
            orientation='h',
            text=n_frame['one']['claim_count_ytd'],
            texttemplate='%{text:,.0f}',
            textfont={'size': 18},
            textposition='inside',
            insidetextanchor='middle',
            width=0.8,
            marker={'color': n_frame['one']['color_code']}
        )],
        layout=go.Layout(
            xaxis=dict(range=[0, 9400], autorange=False, title=dict(text='claim_count', font=dict(size=18))),
            yaxis=dict(range=[-0.5, 5.5], autorange=False, tickfont=dict(size=18)),
            title=dict(text='Facility Category: Period 1', font=dict(size=28), x=0.5, xanchor='center'),
            # Button
            updatemenus=[dict(
                type='buttons',
                buttons=[dict(label='Play',
                              method='animate',
                              args=[None,
                                    {'frame': {'duration': 1000, 'redraw': True},
                                     "transition": {'duration': 250, 'easing': "linear"}}]
                              )],
                x=1.1,
            )]
        ),
        frames=[
            go.Frame(
                data=[
                    go.Bar(x=value['claim_count_ytd'], y=value['name'],
                           orientation='h',
                           text=value['claim_count_ytd'],
                           marker={'color': value['color_code']})
                ],
                layout=go.Layout(
                    xaxis=dict(range=[0, 9400], autorange=False),
                    yaxis=dict(range=[-0.5, 5.5], autorange=False, tickfont=dict(size=18)),
                    title=dict(text='Facility Category: Period ' + str(value['period'].values[0]),
                               font=dict(size=28))
                )
            )
            for key, value in n_frame.items()
        ]
    )

    return fig
