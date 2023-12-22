-- PL/pgSQL is procedural programming language for datbase system
-- Extend functionality of database server by creating server objects with complex logic
-- Designed:
-- 	Create user-defined functions, stored procedures and triggers
-- 	Extend SQL by adding control structures such as if, case, and loop
-- 	Inherit all user-defined functions, operators and types


-----------------------------
-- DECLARING VARIABLES

do
$$
declare
	claims_count integer;
begin
	select count(*) into claims_count
	from t_claims;
	raise notice 'The number of claims is: %', claims_count;
end;
$$;


-- create function find_member_by_acct(
-- 	acct int
-- ) returns t_claims
-- language sql
-- as
-- $$
-- 	select * from t_claims where mem_acct_id = acct;
-- $$;
	
	
-- do $$
-- <<first_block>>
-- declare
-- 	mem_count integer :=0;
-- begin
-- 	select count(*)
-- 	into mem_count
-- 	from t_member;
-- 	raise notice 'The number of members is %', mem_count;
-- end first_block $$;


-- do $$
-- declare
-- 	counter integer := 1;
-- 	member_acct integer := 239176;
-- 	charge numeric(11,2) := 245.91;
-- begin
-- 	raise notice '% % has been paid % usd',
-- 		counter,
-- 			member_acct,
-- 			charge;
-- end $$;

-- do $$
-- declare
-- 	created_at time :=now();
-- begin
-- 	raise notice '%', created_at;
-- 	perform pg_sleep(10);
-- 	raise notice '%', created_at;
-- end $$;


-- DECLARING VARIABLES USING datatype FROM TABLE
-- do $$
-- declare
-- 	member_acct t_claims.mem_acct_id%type;
-- begin
-- 	select mem_acct_id
-- 	from t_claims
-- 	into member_acct
-- 	where claim_id = 8117310;
	
-- 	raise notice 'The Member for claim_id 8117310 is : % ', member_acct;
-- end; $$

-- do $$
-- <<outer_block>>
-- declare
-- 	counter integer :=0;
-- begin
-- 	counter := counter + 1;
-- 	raise notice 'The current value of the counter is %', counter;
	
-- 	declare
-- 		counter integer := 0;
-- 	begin
-- 		counter := counter + 10;
-- 		raise notice 'Counter for subblock is %', counter;
-- 		raise notice 'Counter for outer block is %', outer_block.counter;
-- 	end;
	
-- 	raise notice 'Counter in outer block is %', counter;
	
-- end outer_block $$;

-- END OF VARIABLES --

-----------------------------
-- SELECT INTO

-- Select into assigns data to a variable
-- Can use join, group by and having

-- do $$
-- declare 
-- 	claim_count integer;
-- begin
-- 	select count(DISTINCT(claim_id))
-- 	into claim_count
-- 	from t_claims;
	
-- 	raise notice 'The number of claims is %', claim_count;
-- end $$;

-- END OF SELECT INTO  --

-----------------------------
-- ROW TYPES or ROW VARIABLE

-- Row variable stores the whole row of a result set returned
-- Use the dot(.) to access a field in the row.


-- do $$
-- declare
-- 	selected_claim t_claims%rowtype;
-- begin
-- 	select *
-- 	from t_claims
-- 	into selected_claim
-- 	where claim_trans = 1;
	
-- 	raise notice 'The claim id and item is % % ',
-- 		selected_claim.claim_id,
-- 		selected_claim.claim_item;
		
-- end  $$;		
		
-- END OF ROW TYPES  --

-----------------------------
-- RECORD TYPES

-- Similar to row type.
-- A record can hold only one row of a result set

-- do $$
-- declare
-- 	rec record;
-- begin
-- 	select claim_id, claim_item, mem_acct_id
-- 	into rec
-- 	from t_claims
-- 	where claim_trans = 1;
	
-- 	raise notice 'Claim_id % Claim_item % %', rec.claim_id, rec.claim_item, rec.mem_acct_id;
-- end $$;


-- do $$
-- declare
-- 	rec record;
-- begin
-- 	for rec in select claim_id, claim_item, mem_acct_id
-- 		from t_claims
-- 		where mem_acct_id = 239176
-- 		order by mem_acct_id
-- 	loop
-- 		raise notice '% % %', rec.claim_id, rec.claim_item, rec.mem_acct_id;
-- 	end loop;
-- end $$;


-- END OF RECORD TYPES  --

-----------------------------
-- IF STATEMENTS

-- If condition is True or False


-- do $$
-- declare
-- 	selected_claim t_claims%rowtype;
-- 	input_claim_id t_claims.claim_id%type :=8117310;
-- begin
-- 	select * from t_claims
-- 	into selected_claim
-- 	where claim_id = input_claim_id;
	
-- 	if not found then
-- 		raise notice 'The % claim could not be found', input_claim_id;
-- 	else
-- 		raise notice 'The claim specialty_id is %', selected_claim.specialty_id;
-- 	end if;
-- end $$;


-- END OF IF STATEMENTS  --

-----------------------------
-- CREATE FUNCTIONS


-- Find claims for member
-- Find total charge for member
-- Find total deduct


-- Calling a user-defined function
-- 	Positional notation
-- 	Named notation
-- 	Mixed notation


-- create function get_charge_count(charge_from int, charge_to int)
-- returns int
-- language plpgsql
-- as
-- $$
-- declare
-- 	claim_count integer;
-- begin
-- 	select count(*)
-- 	into claim_count
-- 	from t_claims_paid
-- 	where charge_allowed between charge_from and charge_to;
	
-- 	return claim_count;
-- end $$;

-- FUNCTION CALL
-- select get_charge_count(1000, 10000);
---------------------------


-- OUT FUNCTION
-- create or replace function get_member_stat(
-- 			out max_charge int,
-- 			out max_copay int,
-- 			out average_charge numeric)
-- language plpgsql
-- as $$
-- begin
-- 	select 	max(charge_allowed), 
-- 			max(deduct_copay), 
-- 			avg(charge_allowed)::numeric(9,1)
-- 	into 	max_charge, 
-- 			max_copay, 
-- 			average_charge
-- 	from t_claims_paid;
-- end $$;

-- CALL FUNCTION
-- SELECT get_member_stat();
-- SELECT * FROM get_member_stat();


-- TABLE FUNCTION
-- create or replace function get_pd_info(
-- 	pd bigint
-- )
-- 	returns table (
-- 		charge_allowed_ bigint,
-- 		deduct_copay_ bigint,
-- 		period_ bigint
-- 	)
-- language plpgsql
-- as $$
-- begin
-- 	return query
-- 		select 
			-- charge_allowed, 
			-- deduct_copay, 
			-- period
-- 		from t_claims_paid
-- 		where period = pd;
-- end $$;

-- SELECT * FROM get_pd_info(11);


-- END OF CREATE FUNCTIONS  --

-----------------------------



