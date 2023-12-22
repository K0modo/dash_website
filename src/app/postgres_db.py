# from db_components.db_engine import engine
from .server import db
from models import Claims, ClaimsPaid, InjuryDisease, Specialty, Facility, DailyClaims
from sqlalchemy import delete
import pandas as pd

connection = db.engine.connect()



def create_ORM_objects():
    db.metadata.create_all(connection)


def insert_claims_data():
    df_claim = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\t_claims_data.csv")
    df_claim = df_claim.iloc[:500,:]
    df_claim.to_sql(name='t_claims', con=connection, if_exists='append', index=False)


def insert_claims_paid_data():
    df_claims_paid = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\t_claims_paid_data.csv",
                                 parse_dates=['charge_trans_date'])
    df_claims_paid['charge_trans_date'] = df_claims_paid['charge_trans_date'].dt.date
    df_claims_paid = df_claims_paid.iloc[:500,:]
    df_claims_paid.to_sql(name='t_claims_paid', con=connection, if_exists='append', index=False)


def insert_injury_disease_data():
    df_injury_disease = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\t_injury_disease_h.csv")
    df_injury_disease.to_sql(name='t_injury_disease', con=connection, if_exists='append', index=False)


def insert_specialty_data():
    df_specialty = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\t_specialty_h.csv")
    df_specialty.to_sql(name='t_specialty', con=connection, if_exists='append', index=False)


def insert_facility_data():
    df_facility = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\t_facility_h.csv")
    df_facility.to_sql(name='t_facility', con=connection, if_exists='append', index=False)


def insert_daily_claims_data():
    df_daily_claims = pd.read_csv(r"C:\Users\jchri\PycharmProjects\Database\Postgres\november\v_daily_claims.csv")
    df_daily_claims.to_sql(name='v_daily_claims', con=connection, if_exists='append', index=False)


def delete_table_data(d_table):
    connection.execute(delete(d_table))
    connection.commit()


def postgres_table_data():
    create_tables = input("Do you want to create tables? Y or N  ")
    if create_tables == 'Y':
        answer = input("ARE YOU SURE YOU WANT TO CREATE TABLES? Y or N  ")
        if answer == 'Y':
            create_ORM_objects()
    input_data = input("Do you want to input data into the tables? Y or N  ")
    if input_data == 'Y':
        answer = input("Do you want to input to t_claims? Y or N  ")
        if answer == 'Y':
            delete_table_data(Claims),
            insert_claims_data()
        answer = input("Do you want to input to t_claims_paid? Y or N  ")
        if answer == 'Y':
            delete_table_data(ClaimsPaid),
            insert_claims_paid_data()
        answer = input("Do you want to input to t_injury_disease? Y or N  ")
        if answer == 'Y':
            delete_table_data(InjuryDisease),
            insert_injury_disease_data()
        answer = input("Do you want to input to t_specialty? Y or N  ")
        if answer == 'Y':
            delete_table_data(Specialty),
            insert_specialty_data()
        answer = input("Do you want to input to t_facility? Y or N  ")
        if answer == 'Y':
            delete_table_data(Facility),
            insert_facility_data()
        answer = input("Do you want to input to v_daily_claims? Y or N  ")
        if answer == 'Y':
            delete_table_data(DailyClaims),
            insert_daily_claims_data()


if __name__=='__main__':
    postgres_table_data()