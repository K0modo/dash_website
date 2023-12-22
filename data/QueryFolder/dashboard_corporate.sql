-- Callback 1 Table

-- with period_summary as 
-- 	(select 
-- 		period, 
-- 		count(charge_trans_date) AS day_count, 
-- 		sum(count) AS sum_claims,
-- 		round(avg(count)) AS daily_avg
-- 	from v_daily_claims
-- 	group by period
-- 	order by period)
-- select *, 
-- 	sum(sum_claims) over(order by period rows unbounded preceding) as cum_count,
-- 	round(avg(sum_claims) over(order by period rows unbounded preceding)) as cum_average,
-- 	round(avg(period_summary.daily_avg::numeric) over(order by period rows between 3 preceding and 0 following)) as "_3_MoAve"
-- into table v_period_summary
-- from period_summary;

-- select * from v_period_summary;


-- SELECT mem_acct_id, COUNT(claim_item), SUM(charge_allowed), ROUND(AVG(charge_allowed)) AVG, MAX(charge_allowed)
-- INTO TABLE v_member_annual_stats
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- GROUP BY mem_acct_id
-- ORDER BY mem_acct_id;

-- select * from v_member_annual_stats;

-- select period, mem_acct_id, count(claim_item) as claims_member, sum(charge_allowed) as charges_member
-- into table v_member_period_stats
-- from t_claims
-- inner join t_claims_paid on t_claims.claim_trans = t_claims_paid.claim_trans_id
-- group by period, mem_acct_id
-- order by period;

-- select * from v_member_period_stats;

-- select period, 
-- 	count(distinct(mem_acct_id)) as count_members, 
-- 	sum(charges_member) sum_period, 
-- 	round(avg(charges_member)) as average_member_charge
-- from v_member_period_stats
-- group by period;






