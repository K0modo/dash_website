-- PostgreSQL Window Functions
-- https://www.postgresqltutorial.com/postgresql-window-function/

WITH mytable as 
	(SELECT claim_trans, mem_acct_id, specialty_id, name, charge_allowed, period
	FROM t_claims
	INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
	INNER JOIN t_specialty ON t_claims.specialty_id = t_specialty.id)
SELECT specialty_id, name, SUM(charge_allowed) 
FROM mytable 
GROUP BY specialty_id, name 
ORDER BY specialty_id;
