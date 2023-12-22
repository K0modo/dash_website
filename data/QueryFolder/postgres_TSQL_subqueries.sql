
select charge_trans_date, period, count(distinct(mem_acct_id))
from t_claims
inner join t_claims_paid
on t_claims.claim_trans = t_claims_paid.claim_trans_id
group by charge_trans_date, period
order by charge_trans_date;

-- select period, avg(count)
-- from 

-- SESSION 6 OBJECTIVE 7 SUBQUERIES
-- select * from v_daily_member;
-- select * from v_daily_claims;
-- select * from v_member_summary;


select period, count(distinct(mem_acct_id))
from t_claims as c
inner join t_claims_paid as p
on c.claim_trans = p.claim_trans_id
group by period
order by period;

-- select * 
-- from v_test_claims as c
-- inner join v_test_paid as p
-- on c.claim_trans = p.claim_trans_id
-- where period = 1
-- order by charge_trans_date, claim_trans
-- ;

-- select * 
-- from v_test_claims as c
-- where claim_trans not in
-- 	(select claim_trans_id from v_test_paid where period = 2)
-- order by mem_acct_id
-- ;

-- select * 
-- from v_test_claims as c
-- inner join v_test_paid as p
-- on c.claim_trans = p.claim_trans_id
-- where period = 2
-- order by charge_trans_date;

-- select * from v_test_paid
-- where period = 2
-- order by charge_trans_date;

-- select * 
-- from v_test_claims as c
-- inner join (select * from v_test_paid
-- 			where period = 2
-- 			order by charge_trans_date) as p
-- on c.claim_trans = p.claim_trans_id
-- ;

-- select *
-- from v_test_paid
-- where period = 2
-- order by charge_trans_date
-- ;

-- select mem_acct_id, count(mem_acct_id)
-- from v_test_claims as c
-- inner join v_test_paid as p
-- on c.claim_trans = p.claim_trans_id
-- where period = 2
-- group by mem_acct_id
-- ;

-- select count(mem_acct_id)
-- from v_test_claims;

select mem_acct, count(mem_acct_id)
from t_member as m
inner join v_test_claims as c
on m.mem_acct = c.mem_acct_id
group by mem_acct
;

select * , (select count(mem_acct_id)
			from v_test_claims as c
		   	where m.mem_acct = c.mem_acct_id) as NumTrans
from t_member as m;


