-- select tid.name, tc.injury_disease_id, tid.color_code, count(tc.injury_disease_id) as claim_count
-- into table v_icd_table
-- from t_claims as tc
-- inner join t_injury_disease as tid
-- on tc.injury_disease_id = tid.id
-- group by tid.name, injury_disease_id, tid.color_code
-- order by injury_disease_id;

select * from v_icd_table;
-- drop table v_icd_table;