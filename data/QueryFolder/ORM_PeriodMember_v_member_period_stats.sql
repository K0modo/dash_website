select 
	period,
	mem_acct_id,
	count(claim_trans) as claims_member,
	sum(charge_paid_ins) as charges_member
into table v_member_period_stats
from t_claims
inner join t_claims_paid
on t_claims.claim_trans = t_claims_paid.claim_trans_id
group by period, mem_acct_id
order by period, mem_acct_id;

select * from v_member_period_stats;
-- drop table v_member_period_stats;


-- select * , (
-- 	select period, avg(member_count) from v_daily_member
-- 	group by period order by period
-- )
-- inner join v_member_summary
-- on 


from v_member_summary;