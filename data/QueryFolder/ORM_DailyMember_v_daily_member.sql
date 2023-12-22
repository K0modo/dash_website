select 
	charge_trans_date, 
	period, 
	count(distinct(mem_acct_id)) as member_count	
into v_daily_member
from t_claims_paid
inner join t_claims
on t_claims_paid.claim_trans_id = t_claims.claim_trans
group by charge_trans_date, period
order by charge_trans_date;

select * from v_daily_member;
-- drop table v_daily_member;




