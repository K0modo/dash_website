-- TABLE: v_member_summary

select * from v_member_summary;
-- drop table v_member_summary;

-- with member_annual as (
-- 	select a.period, a.daily_member_avg, c.mem_count as daily_member_sum
-- 	from period_distinct_avg as a
-- 	inner join period_distinct_count as c
-- 	on a.period = c.period
-- 	order by a.period
-- 	)
-- select *, 
-- 	round(avg(daily_member_sum) over(order by period rows unbounded preceding)) as annual_ytd_avg
-- into table v_member_summary
-- from member_annual
-- ;


-- Table v_member_summary is dependent on the following tables:
-- period_distinct_count
-- period_date_distinct_count
-- period_distinct_avg

-- TABLE: period_distinct_count

select period, count(distinct(mem_acct_id)) as mem_count
into table period_distinct_count
from t_claims as c
inner join t_claims_paid as p
on c.claim_trans = p.claim_trans_id
group by period
order by period;

select * from period_distinct_count;
-- drop table period_distinct_count;


TABLE: period_date_distinct_count

select charge_trans_date, period, count(distinct(mem_acct_id))
into table period_date_distinct_count
from t_claims as c
inner join t_claims_paid as p
on c.claim_trans = p.claim_trans_id
group by charge_trans_date, period
order by charge_trans_date;

select * from period_date_distinct_count;
-- drop table period_date_distinct_count;


-- TABLE: period_distinct_avg

select period, round(avg(count)) as daily_member_avg
into period_distinct_avg
from period_date_distinct_count
group by period
order by period;

select * from period_distinct_avg;
-- drop table period_distinct_avg;

select count(distinct(mem_acct_id))
from t_claims;

select count(distinct(mem_acct_id)) from t_claims;

