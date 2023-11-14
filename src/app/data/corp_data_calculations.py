

class CorporateCalculations:
    def __init__(self, dataframe):
        self.corp_table = dataframe

    def claims_by_period(self):
        group_data = self.corp_table.groupby('period', as_index=False).agg(CLAIMS=('claim_id', 'count')).sort_values('period')
        return group_data

    def claims_volume_ytd(self):
        group_data = self.corp_table.groupby('period', as_index=False).agg(CLAIMS=('claim_id', 'count')).sort_values('period')
        group_data['YTD_CUM'] = group_data['CLAIMS'].cumsum()
        group_data['MO_AVE'] = (group_data['YTD_CUM'] / (group_data['period']).astype(float)).astype(int)

        return group_data

    def claims_volume_period(self):
        group_data = self.corp_table.groupby('trans_date', as_index=False).agg(CLAIMS_DAILY=('claim_id', 'count'))

        return group_data

    def claims_member_period(self):
        group_data = self.corp_table.pivot_table(index='mem_acct', columns='period', values='claim_id', aggfunc='count')

        return group_data

    def charges_member_period(self):
        group_data = self.corp_table.pivot_table(index='mem_acct', columns='period', values='charge_allowed', aggfunc='sum')

        return group_data

    def claims_member_quarter(self):
        group_data = self.corp_table.pivot_table(values='claim_id', index='mem_acct', aggfunc='count', columns='quarter').reset_index()

        return group_data

    def claims_charges_ytd(self):
        group_data = (self.corp_table.groupby('period', as_index=False)
                      .agg(CHARGES=('charge_allowed', 'sum'), CHARGE_AVE=('charge_allowed', 'mean'))
                      .sort_values('period'))
        group_data['YTD_CUM'] = group_data['CHARGES'].cumsum()
        group_data['3_MONTH_AVE'] = round(group_data['CHARGES'].rolling(3).mean().fillna(0)).astype(int)

        return group_data

    def claims_charges_period(self):
        group_data = self.corp_table.groupby('trans_date', as_index=False).agg(CLAIM_CHARGE_AVE=('charge_allowed', 'mean'))

        return group_data






