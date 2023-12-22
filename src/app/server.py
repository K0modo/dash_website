from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from db_components.url_test2 import url_object
import pandas as pd
from sqlalchemy import URL
import warnings


url_object = URL.create(
    "postgresql",
    username='postgres',
    # password='N)rmandy1',
    host='localhost',
    database='test2'
)

class Config(object):
    SQLALCHEMY_DATABASE_URI = url_object
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()


def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)
    db.init_app(server)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)

    # with server.app_context():

        # df = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\t_claims_paid_data.csv")
        # df.to_sql('t_claims_paid', con=db.engine, if_exists='replace')
        # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
        # df.to_sql('gapminder2007', con=db.engine, if_exists='replace')

    from .dashboard import create_dashapp
    dash_app = create_dashapp(server)
    return dash_app
