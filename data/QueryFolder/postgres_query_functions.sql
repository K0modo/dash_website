-- WINDOW FUNCTIONS

-- SELECT AVG(charge_allowed)
-- FROM t_claims_paid


-- SELECT specialty_name, ROUND(AVG(charge_allowed))
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- INNER JOIN t_specialty ON t_claims.specialty_id = t_specialty.id
-- GROUP BY specialty_name
-- ORDER BY round DESC

-- SELECT AVG(price)
-- FROM products;

-- SELECT group_name, AVG(price)
-- FROM products
-- INNER JOIN product_groups USING(group_id)
-- GROUP BY group_name;

-- SELECT category, ROUND(AVG(charge_allowed))
-- FROM t_claims
-- INNER JOIN t_claims_paid ON t_claims.claim_trans = t_claims_paid.claim_trans_id
-- INNER JOIN t_specialty ON t_claims.specialty_id = t_specialty.id
-- GROUP BY category;

SELECT name,  ROUND(AVG(charge_allowed))
FROM t_claims_paid
INNER JOIN t_claims ON t_claims_paid.claim_trans_id = t_claims.claim_trans
INNER JOIN t_specialty ON t_claims.specialty_id = t_specialty.id
GROUP BY name;

-- SELECT product_name, price, group_name, AVG(price) OVER (PARTITION BY group_name)
-- FROM products
-- INNER JOIN product_groups USING (group_id);


-- SELECT mem_acct, period, period_count,
-- LAG(period_count, 1) OVER(PARTITION BY mem_acct ORDER BY period) as MyLag
-- -- period_count - LAG(period_count, 1) OVER(PARTITION BY mem_acct ORDER BY period) as MyDiff
-- FROM ts_mem_period_count;


-- SELECT * FROM ts_period_stats;
SELECT period, count_trans, 
LAG(count_trans, 1) OVER(ORDER BY period) as MyLag, 
count_trans - LAG(count_trans, 1) OVER(ORDER BY period) as MyDiff,
ROUND((CAST(count_trans as numeric) - LAG(count_trans, 1) OVER(ORDER BY period)) / count_trans * 100,1) as MyPercent
FROM ts_period_stats;

-- SELECT * FROM ts_mem_period_count ORDER BY mem_acct, period

SELECT mem_acct, period, period_count,
ROUND(CAST(CUME_DIST() over(partition by mem_acct order by period_count) as numeric)*100, 1) as "MyCume_Dist"
FROM ts_mem_period_count;

SELECT mem_acct, period, period_count
FROM ts_mem_period_count;