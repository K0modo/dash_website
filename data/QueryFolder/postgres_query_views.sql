-- PostgreSQL Views
-- https://www.postgresqltutorial.com/postgresql-views/managing-postgresql-views/

-- View is a stored query.
-- Can be accessed as a virtual table


-- SELECT mem_acct_id, COUNT(claim_item), SUM(charge_allowed), ROUND(AVG(charge_allowed)) AVG, MAX(charge_allowed)
-- INTO TABLE pd_member_stats
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- GROUP BY mem_acct_id
-- ORDER BY mem_acct_id;




-- SELECT period, COUNT(DISTINCT charge_trans_date) days, COUNT(pay_trans)count_trans, 
-- 	SUM(charge_allowed) sum_charges, ROUND(AVG(charge_allowed)) avg_charge, MAX(charge_allowed) max_charge
-- -- INTO TABLE pd_period_stats
-- FROM t_claims_paid
-- GROUP BY period
-- ORDER BY period;


-- SELECT specialty_id, COUNT(claim_trans)
-- FROM t_claims
-- GROUP BY specialty_id;

-- SELECT facility_id, COUNT(claim_trans)
-- FROM t_claims
-- GROUP BY facility_id;

-- SELECT injury_disease_id, COUNT(claim_trans)
-- FROM t_claims
-- GROUP BY injury_disease_id;



-- WITH MyTable as (
-- 	SELECT mem_acct, specialty_id, COUNT(mem_acct_id) as memcount
-- 	FROM t_member
-- 	INNER JOIN t_claims on t_member.mem_acct = t_claims.mem_acct_id
-- 	GROUP BY mem_acct, specialty_id),
-- PeriodTable as
-- 	(SELECT * FROM t_specialty WHERE id = 202 )
-- SELECT * FROM MyTable
-- LEFT JOIN PeriodTable ON MyTable.specialty_id = PeriodTable.id
-- WHERE memcount > 100
-- ORDER BY mem_acct;




-- select * from pd_member_stats;
-- select * from v_daily_claims;
-- select * from v_period_claims;


-- create view v_period_summary AS



-- create or replace function get_claims_daily_ave(pd int)
-- returns numeric
-- language plpgsql
-- as
-- $$
-- declare
-- 	d_ave numeric;
-- begin
-- 	select daily_ave
-- 	into d_ave
-- 	from v_period_summary 
-- 	where period = pd;
	
-- 	return d_ave;	
-- end
-- $$;
	
-- select get_claims_daily_ave(12)


