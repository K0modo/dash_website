from dash import html

import dash_bootstrap_components as dbc


def stat_card(children, stat_id):

    return html.Div(
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4(children),
                    html.H3(id=stat_id)
                ], className='text-center text-primary'
            ),
        )
    )


def test_stat_card(stat_label, stat):

    return dbc.Card(
            dbc.CardBody(
                [
                    html.H4(stat_label),
                    html.H3(stat)
                ], className='text-center text-primary'
            ),
        )


def spec_log_radio(radio_id):

    return html.Div(
        dbc.RadioItems(
            id=radio_id,
            options=['CHARGES', 'CHARGES on LOGarithmic Scale'],
            value='CHARGES'
        )
    )


