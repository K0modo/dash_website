

-- ALTER TABLE t_specialty
-- RENAME COLUMN specialty_name TO name;

-- ALTER TABLE t_facility
-- RENAME COLUMN facility_name TO name;

-- ALTER TABLE t_injury_disease
-- RENAME COLUMN injury_disease_name TO name;






-- JOIN

-- SELECT mem_acct, period, sum(charge_allowed)
-- FROM t_claims_paid
-- INNER JOIN t_claims ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- GROUP BY period, mem_acct
-- ORDER BY period


-- DATE

-- SELECT DATE(charge_trans_date) Date, SUM(charge_allowed), COUNT(charge_allowed), AVG(charge_allowed)
-- FROM t_claims_paid
-- GROUP BY DATE(charge_trans_date)
-- ORDER BY DATE(charge_trans_date)


-- HAVING

-- SELECT period, SUM(charge_allowed), COUNT(charge_allowed), ROUND(AVG(charge_allowed))
-- FROM t_claims_paid
-- GROUP BY period
-- HAVING ROUND(AVG(charge_allowed)) > 500 OR period = 4
-- ORDER BY period


-- UNION

-- (
-- 	SELECT mem_acct, COUNT(mem_acct)
-- 	FROM t_claims
-- 	GROUP BY mem_acct
-- 	ORDER BY COUNT(mem_acct) DESC
-- 	LIMIT 20
-- )
-- UNION
-- (
-- 	SELECT mem_acct, SUM(charge_allowed)
-- 	FROM t_claims
-- 	INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- 	GROUP BY mem_acct
-- 	ORDER BY SUM(charge_allowed) DESC
-- 	LIMIT 20
-- )
-- ORDER BY mem_acct


-- GROUPING SETS

-- SELECT charge_trans_date, period, COUNT(charge_trans_date)
-- FROM t_claims_paid
-- GROUP BY charge_trans_date, period

-- UNION ALL

-- SELECT charge_trans_date, NULL, COUNT(charge_trans_date)
-- FROM t_claims_paid
-- GROUP BY charge_trans_date

-- UNION ALL

-- SELECT NULL, period, COUNT(charge_trans_date)
-- FROM t_claims_paid
-- GROUP BY period

-- UNION ALL

-- SELECT NULL, NULL, COUNT(charge_trans_date)
-- FROM t_claims_paid


-- GROUPING SETS

-- SELECT period, charge_trans_date, COUNT(charge_trans_date)
-- FROM t_claims_paid
-- GROUP BY
-- 	GROUPING SETS(
-- 		(period, charge_trans_date),
-- 		(period),
-- 		()
-- 	)
-- ORDER BY period, charge_trans_date


-- -- GROUPING FUNCTION () WITH HAVING

-- SELECT
-- 	GROUPING(period) grouping_period,
-- 	GROUPING(period, charge_trans_date) grouping_date,
-- 	period,
-- 	charge_trans_date,
-- 	COUNT(charge_trans_date)
-- FROM t_claims_paid
-- GROUP BY
-- 	GROUPING SETS(
-- 			(period, charge_trans_date),
-- 			(period),
-- 			()
-- 		)
-- HAVING GROUPING(period) = 1
-- ORDER BY period, charge_trans_date


-- ROLLUP

-- member
-- claim
-- claim_item

-- SELECT period, charge_trans_date, COUNT(charge_trans_date)
-- FROM t_claims_paid
-- GROUP BY ROLLUP (period, charge_trans_date)
-- ORDER BY period, charge_trans_date

-- SELECT facility_id, facility_name, injury_disease_id, COUNT(facility_id)
-- FROM t_claims
-- INNER JOIN t_facility ON t_claims.facility_id = t_facility.id
-- GROUP BY 
-- 	facility_name, 
-- 	ROLLUP (facility_id, injury_disease_id)
-- ORDER BY facility_id, COUNT(facility_id)


-- ROLLUP WITH DATES

-- SELECT 
-- 	EXTRACT(YEAR FROM charge_trans_date) y,
-- 	EXTRACT(MONTH FROM charge_trans_date) m,
-- 	EXTRACT(DAY FROM charge_trans_date) d,
-- 	COUNT(pay_trans)
-- FROM 
-- 	t_claims_paid
-- GROUP BY
-- 	ROLLUP (
-- 		EXTRACT(YEAR FROM charge_trans_date),
-- 		EXTRACT(MONTH FROM charge_trans_date),
-- 		EXTRACT(DAY FROM charge_trans_date)		
-- 	)
-- ORDER BY EXTRACT(YEAR FROM charge_trans_date), EXTRACT(MONTH FROM charge_trans_date), EXTRACT(DAY FROM charge_trans_date)	
	


-- SUBQUERIES

-- SELECT AVG(charge_allowed)
-- FROM t_claims_paid

-- SELECT claim_item, claim_id, charge_allowed
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- WHERE charge_allowed > (
-- 	SELECT AVG(charge_allowed) 
-- 	FROM t_claims_paid
-- )
-- ORDER BY charge_allowed DESC



-- SELECT DISTINCT mem_acct
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- WHERE period BETWEEN 8 AND 10

-- INSERT INTO v_period_claims (period, day_count, sum_count)
-- VALUES (14, 25, 2000)
-- RETURNING *


-- ADD COLUMN
-- ALTER TABLE t_facility
-- ADD COLUMN category VARCHAR
-- INSERT INTO t_facility(category)
-- VALUES  (3),(3),(3),(3),(3),(3)
-- RETURNING *;

-- DELETE FROM t_facility
-- WHERE category = '3';




-- SELECT mem_acct, COUNT(claim_item), SUM(charge_allowed), ROUND(AVG(charge_allowed)) AVG, MAX(charge_allowed)
-- INTO TABLE t_member_stats
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- GROUP BY mem_acct
-- ORDER BY mem_acct

-- SELECT period, COUNT(DISTINCT charge_trans_date) days, COUNT(pay_trans)count_trans, 
-- 	SUM(charge_allowed) sum_charges, ROUND(AVG(charge_allowed)) avg_charge, MAX(charge_allowed) max_charge
-- INTO TABLE ts_period_stats
-- FROM t_claims_paid
-- GROUP BY period
-- ORDER BY period



-- SELECT mem_acct, specialty_id, charge_allowed
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- WHERE period = 12
-- ORDER BY mem_acct;

-- SELECT *
-- FROM t_claims
-- WHERE claim_trans in
-- 	(SELECT claim_trans_id FROM t_claims_paid WHERE period = 1)
-- ORDER BY mem_acct;

-- SELECT mem_acct, specialty_id
-- FROM t_claims
-- WHERE claim_trans in 
-- 	(SELECT claim_trans_id FROM t_claims_paid WHERE period = 12)
-- ORDER BY mem_acct;

-- SELECT * FROM ts_member_stats;

-- SELECT mem_acct, count,
-- 	rank() over( order by count desc) as therank
-- FROM ts_member_stats
-- ORDER BY therank;

--  SELECT * FROM ts_member_stats
 
 
 
--  FUNCTIONS


 CREATE OR REPLACE FUNCTION getMember(acct int)
 	RETURNS TABLE (
	 	mem_acct_ bigint,
		count_ bigint,
	 	sum_ numeric,
	 	avg_ numeric,
	 	max_ bigint 
 	)
 	LANGUAGE plpgsql
 AS $$
 BEGIN
 	RETURN QUERY
	 	SELECT *
		FROM ts_member_stats
		WHERE mem_acct = acct ;
 END;
 $$;
 
 
 SELECT * FROM getMember(12611);