select * from t_facility;

-- select 
-- 	facility_id,
-- 	name,
-- 	count(facility_id) as claim_count,
-- 	sum(charge_paid_ins) as claim_paid,
-- 	color_code
-- into table v_facility_summary
-- from t_claims as tc
-- inner join t_claims_paid as tcp
-- on tc.claim_trans = tcp.claim_trans_id
-- inner join t_facility as tfac
-- on tc.facility_id = tfac.id
-- group by facility_id, name, color_code
-- order by facility_id;


-- RACING TABLE

-- with racing_select_statement as (
-- 	select 
-- 		facility_id,
-- 		name,
-- 		period,
-- 		color_code,
-- 		count(facility_id) as claim_count
-- 	from t_claims as tc
-- 	inner join t_claims_paid as tcp
-- 	on tc.claim_trans = tcp.claim_trans_id
-- 	inner join t_facility as tfac
-- 	on tc.facility_id = tfac.id
-- 	group by facility_id, name, period, color_code
-- 	order by facility_id, period
-- )
-- select *, 
-- 	sum(claim_count) over(partition by facility_id order by period) as claim_count_ytd
-- into table v_facility_racing
-- from racing_select_statement;

select * from v_facility_summary;
select * from v_specialty_summary;
select * from v_facility_racing;

