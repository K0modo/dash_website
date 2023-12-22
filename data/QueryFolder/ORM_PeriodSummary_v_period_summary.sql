-- Callback 1 Table


-- with period_summary as 
-- 	(select 
-- 		period, 
-- 		count(charge_trans_date) AS day_count, 
-- 		sum(claims_count) AS claims_period_count,
-- 		round(avg(claims_count)) AS claims_daily_avg,
-- 	 	sum(charges_paid) as claims_period_paid, 
-- 	 	round(avg(charges_paid::float)) as claims_paid_daily_avg
-- 	from v_daily_claims
-- 	group by period
-- 	order by period)
-- select *, 
-- 	sum(claims_period_count) over(order by period rows unbounded preceding) as claims_period_count_cum,
-- 	round(avg(claims_period_count) over(order by period rows unbounded preceding)) as claims_period_average_cum,
-- 	sum(claims_period_paid) over(order by period rows unbounded preceding) as claims_period_paid_cum,
-- 	round(avg(claims_period_paid) over(order by period rows unbounded preceding)) as claims_period_paid_average_cum
-- into table v_period_summary
-- from period_summary;

select * from v_period_summary;
-- drop table v_period_summary;
-- select sum(charge_paid_ins) from t_claims_paid

