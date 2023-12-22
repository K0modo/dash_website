-- select 
-- 	specialty_id, 
-- 	name, 
-- 	count(specialty_id) as claim_count, 
-- 	sum(charge_paid_ins) as claim_paid, 
-- 	color_code
-- into table v_specialty_summary
-- from t_claims as tc
-- inner join t_claims_paid as tcp
-- on tc.claim_trans = tcp.claim_trans_id
-- inner join t_specialty as tsp
-- on tc.specialty_id = tsp.id
-- group by specialty_id, name, color_code
-- order by specialty_id;

select * from v_specialty_summary;
select * from t_specialty;

select * from v_icd_racing;

-- RACING TABLE

-- with racing_select_statement as (
-- 	select 
-- 		specialty_id,
-- 		name,
-- 		period,
-- 		color_code,
-- 		count(specialty_id) as claim_count
-- 	from t_claims as tc
-- 	inner join t_claims_paid as tcp
-- 	on tc.claim_trans = tcp.claim_trans_id
-- 	inner join t_specialty as tsp
-- 	on tc.specialty_id = tsp.id
-- 	group by specialty_id, name, period, color_code
-- 	order by specialty_id, period
-- )
-- select *, 
-- 	sum(claim_count) over(partition by specialty_id order by period) as claim_count_ytd
-- into table v_specialty_racing
-- from racing_select_statement;

select * from v_specialty_racing;
-- drop table v_specialty_racing;

select max(claim_count_ytd)
from v_specialty_racing;