

class MemberCalculations:

    def __init__(self, dataframe):
        self.mem_table = dataframe

    def annual_charge_calc(self):
        return self.mem_table.charge_allowed.sum()

    def annual_claims_calc(self):
        return self.mem_table.claim_id.nunique()

    def annual_line_items_calc(self):
        return self.mem_table.claim_id.count()

    def charge_by_period(self):
        group_data = self.mem_table.groupby('period', as_index=False)['charge_allowed'].sum().sort_values(
            'period')
        return group_data

    def claims_by_period(self):
        group_data = self.mem_table.groupby('period', as_index=False)['claim_id'].nunique().sort_values(
            'period')
        return group_data

    def charge_by_facility_class(self):
        group_data = self.mem_table.groupby('facility_class', as_index=False)['charge_allowed'].count()
        return group_data

    def count_by_specialty(self):
        group_data = (self.mem_table.groupby('specialty', as_index=False)
                      .agg(SPECIALTY_COUNT=('specialty', 'count'))
                      .sort_values('SPECIALTY_COUNT', ascending=False))

        # Assign "low_count" SPECIALTY (less than 10) to "Other" for data visual purposes
        group_data['cumsum'] = group_data['SPECIALTY_COUNT'].cumsum()
        group_data['portion'] = group_data['cumsum'] / group_data['SPECIALTY_COUNT'].sum()
        group_data['specialty'] = group_data['specialty'].where(group_data['SPECIALTY_COUNT'] > 10, 'Other')
        group_data = group_data.groupby('specialty', as_index=False)['SPECIALTY_COUNT'].sum()

        return group_data

    def charge_by_injury_disease(self):
        group_data = (self.mem_table.groupby('injury_disease', as_index=False)['charge_allowed']
                      .count()
                      .sort_values('charge_allowed', ascending=False))

        return group_data

    def charge_count_spec8(self):
        group_data = (self.mem_table.groupby('specialty', as_index=False)
                      .agg(CHARGES=('charge_allowed', 'sum'), COUNT=('charge_allowed', 'count'),
                           MAX=('charge_allowed', 'max'), AVERAGE=('charge_allowed', 'mean'),
                           DEDUCT_COPAY=('deduct_copay', 'sum'))
                      .nlargest(8, 'COUNT')
                      .sort_values(by='COUNT', ascending=False)
                      )

        return group_data

    def spec_nlargest_list8(self):
        group_data = self.charge_count_spec8().specialty.tolist()

        return group_data

    def spec_filter_to_list8(self):
        group_list = self.spec_nlargest_list8()
        group_data = self.mem_table[self.mem_table.specialty.isin(group_list)]

        return group_data




class GridStats:

    def __init__(self, data_hist):

        self.table = data_hist          #[data_hist['mem_acct'] == self.member]

    def calc_serv_stats(self):
        group_data = (self.table.groupby(['mem_acct', 'specialty'], as_index=False)
                      .agg(CHARGES=('charge_allowed', 'sum'), CLAIMS_COUNT=('charge_allowed', 'count'),
                           MAX=('charge_allowed', 'max'), AVERAGE=('charge_allowed', 'mean'),
                           DEDUCT_COPAY=('deduct_copay', 'sum'))
                      )

        return group_data

    def spec_claim_hist(self):
        group_data = self.table.loc[:, ['specialty', 'trans_date', 'claim_id', 'charge_allowed', 'deduct_copay', 'period']]

        return group_data

