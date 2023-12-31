from src.app.init import create_app

# import warnings
#
# warnings.filterwarnings('ignore')

# dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
#
# app = Dash(__name__, use_pages=True,
#            external_stylesheets=[dbc.themes.LUMEN, dbc_css, dbc.icons.BOOTSTRAP], suppress_callback_exceptions=True,
#            meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])
#
# load_figure_template("LUMEN")
#
# app.layout = dbc.Container([
#     dcc.Store(id=ids.STORE_DATA, data=load_member_data()),
#     # dcc.Store(id=ids.STORE_MEM_TABLE, data=member_dropdown_table()),
#     dcc.Store(id=ids.STORE_MEM_ACCT, data=None),
#     dcc.Store(id=ids.STORE_DATA_FILTER, data=None),
#     dcc.Store(id=ids.STORE_CORP_DATA, data=load_corporate_data()),
#     navigation.render_navbar(),
#     dash.page_container
#
# ])

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    # app.run_server(debug=True)
