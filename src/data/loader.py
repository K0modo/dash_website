import pandas as pd



df_mem_path = r"C:\Users\jchri\PycharmProjects\dash_website\data\data_members.csv"
df_mem = pd.read_csv(df_mem_path, parse_dates=['charge_trans_date']).sort_values('mem_acct')
df_mem['trans_date'] = df_mem['charge_trans_date'].dt.date
# df[‘Date’]=df[‘Date’].astype(str)  - searched for dcc.Store and Ag Grid
# https://dashaggrid.pythonanywhere.com/rows/row-sorting

for col in ['mem_acct', 'claim_item', 'injury_disease', 'specialty', 'facility_class', 'period']:
    df_mem[col] = df_mem[col].astype('category')


def load_member_data():
    df_mem_dict = df_mem.to_dict('records')
    return df_mem_dict

# LOAD CORPORATE DATA
df_corp_path = r"C:\Users\jchri\PycharmProjects\dash_website\data\data_sept.csv"
df_corp = pd.read_csv(df_corp_path,  parse_dates=['charge_trans_date'])
df_corp['trans_date'] = df_corp['charge_trans_date'].dt.date

for col in ['mem_acct', 'claim_item', 'injury_disease', 'specialty', 'facility_class', 'facility_type', 'period', 'quarter']:
    df_corp[col] = df_corp[col].astype('category')


def load_corporate_data():
    df_corp_dict = df_corp.to_dict('records')
    return df_corp_dict
