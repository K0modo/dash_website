-- FETCH

-- select film_id, title
-- from film
-- order by title
-- offset 5 rows
-- fetch first 5 rows only;


-- CURSORS

-- Encapsulate a query and process each individual row at a time
-- 	Declare a cursor
-- 	Open the cursor
-- 	Fetch rows from the result set into a target
-- 		Fetch statement gets the next row from the cursor and assigns it a target variable
-- 		which could be a record, row variable, or a comma-separated list of variables
-- 	Close the cursor

declare 
	cur_charges cursor for 
		select * 
		from t_claims_paid;
	cur_charges2 cursor (pd integer)for 
		select * 
		from t_claims_paid 
		where period = pd;
	
open cur_charges;
open cur_charges2(pd :=11)

fetch cur_charges into row_charges;
fetch last from row_charges into charge_allowed, deduct_copay;

close cur_charges
close cur_charges2


-- create or replace function get_film_titles(p_year integer)
-- 	returns text 
	
-- language plpgsql
-- as $$
	
-- declare
-- 	titles 		text default '';
-- 	rec_film 	record;
-- 	cur_films 	cursor(p_year integer)
-- 				for select title, release_year
-- 				from film
-- 				where release_year = p_year;
-- begin
-- 	open cur_films(p_year);
	
-- 	loop
-- 		fetch cur_films into rec_film;
-- 		exit when not found;
		
-- 		if rec_film.title like '%ful%' then
-- 			titles := titles || ',' || rec_film.title || ':' || rec_film.release_year;
-- 		end if;
-- 	end loop;
	
-- 	close cur_films;
	
-- 	return titles;
-- end $$;

-- select get_film_titles(2006);







		