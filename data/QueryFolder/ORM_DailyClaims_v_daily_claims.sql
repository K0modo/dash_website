select 
	charge_trans_date, 
	period, 
	count(claim_trans_id) as claims_count,
	sum(charge_paid_ins) as charges_paid
into v_daily_claims
from t_claims_paid
group by charge_trans_date, period
order by charge_trans_date, period;

select * from v_daily_claims;
-- drop table v_daily_claims;