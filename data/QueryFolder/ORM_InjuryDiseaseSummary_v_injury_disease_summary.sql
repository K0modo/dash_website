-- select injury_disease_id, 
-- 	name, 
-- 	count(injury_disease_id) as claim_count, 
-- 	sum(charge_paid_ins) as claim_paid, 
-- 	color_code
-- into table v_injury_disease_summary
-- from t_claims as tc
-- inner join t_claims_paid as tcp
-- on tc.claim_trans = tcp.claim_trans_id
-- inner join t_injury_disease as tid
-- on tc.injury_disease_id = tid.id
-- group by injury_disease_id, name, color_code
-- order by injury_disease_id;

-- select * from v_injury_disease_summary;


-- RACING TABLE

-- with racing_select_statement as (
-- 	select 
-- 		injury_disease_id,
-- 		name,
-- 		period,
-- 		color_code,
-- 		count(injury_disease_id) as claim_count
-- 	from t_claims as tc
-- 	inner join t_claims_paid as tcp
-- 	on tc.claim_trans = tcp.claim_trans_id
-- 	inner join t_injury_disease as tid
-- 	on tc.injury_disease_id = tid.id
-- 	group by injury_disease_id, name, period, color_code
-- 	order by injury_disease_id, period
-- )
-- select *, 
-- 	sum(claim_count) over(partition by injury_disease_id order by period) as claim_count_ytd
-- into table v_icd_racing
-- from racing_select_statement;

select * from v_icd_racing;
-- drop table v_icd_racing;
select * from v_injury_disease_summary;

