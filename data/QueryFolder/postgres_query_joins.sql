-- CREATE TABLE basket_a (
--     a INT PRIMARY KEY,
--     fruit_a VARCHAR (100) NOT NULL
-- );

-- CREATE TABLE basket_b (
--     b INT PRIMARY KEY,
--     fruit_b VARCHAR (100) NOT NULL
-- );

-- INSERT INTO basket_a (a, fruit_a)
-- VALUES
--     (1, 'Apple'),
--     (2, 'Orange'),
--     (3, 'Banana'),
--     (4, 'Cucumber');

-- INSERT INTO basket_b (b, fruit_b)
-- VALUES
--     (1, 'Orange'),
--     (2, 'Apple'),
--     (3, 'Watermelon'),
--     (4, 'Pear');


-- select a, fruit_a, b, fruit_b
-- from basket_a
-- inner join basket_b on fruit_a = fruit_b;

-- select a, fruit_a, b, fruit_b
-- from basket_a
-- left join basket_b on fruit_a = fruit_b;

-- select a, fruit_a, b, fruit_b
-- from basket_a
-- left join basket_b on fruit_a = fruit_b
-- where b IS NULL;

-- select customer.customer_id, first_name, last_name, amount, payment_date
-- from customer
-- inner join payment
-- 	on payment.customer_id = customer.customer_id
-- order by payment_date;

-- select customer.customer_id, customer.first_name cfirst, customer.last_name clast, 
-- 		staff.first_name sfirst, staff.last_name slast, amount, payment_date
-- from customer
-- inner join payment
-- 	on payment.customer_id = customer.customer_id
-- inner join staff
-- 	on staff.staff_id = payment.staff_id
-- order by payment_date;

-- -- LEFT JOIN
-- select film.film_id, title, inventory_id
-- from film
-- left join inventory on inventory.film_id = film.film_id
-- where inventory.inventory_id IS NULL
-- order by title;
	

-- select customer_id, sum(amount)
-- from payment
-- group by customer_id
-- order by sum(amount) desc;


-- select first_name || ' ' || last_name full_name, sum(amount) amount
-- from payment
-- inner join customer using (customer_id)
-- group by full_name
-- order by amount desc;


-- GROUP BY MULTIPLE COLUMNS
-- select customer_id, staff_id, sum(amount)
-- from payment
-- group by staff_id, customer_id
-- order by customer_id, staff_id;

-- DATE
-- select date(payment_date ) paid_date, sum(amount) sum
-- from payment
-- group by date(payment_date);


-- HAVING
-- Specifies a search condition for a group or an aggregate.
-- Often used with Group By to filter groups

-- select customer_id, sum(amount)
-- from payment
-- group by customer_id
-- having sum(amount) > 200;


-- UNION
-- Combines the result sets of two or more SELECT statement.
-- The number and order of columns in the select list of both queries must be the same
-- Data types must be compatible.


-- DROP TABLE IF EXISTS top_rated_films;
-- CREATE TABLE top_rated_films(
-- 	title VARCHAR NOT NULL,
-- 	release_year SMALLINT
-- );

-- DROP TABLE IF EXISTS most_popular_films;
-- CREATE TABLE most_popular_films(
-- 	title VARCHAR NOT NULL,
-- 	release_year SMALLINT
-- );

-- INSERT INTO 
--    top_rated_films(title,release_year)
-- VALUES
--    ('The Shawshank Redemption',1994),
--    ('The Godfather',1972),
--    ('12 Angry Men',1957);

-- INSERT INTO 
--    most_popular_films(title,release_year)
-- VALUES
--    ('An American Pickle',2020),
--    ('The Godfather',1972),
--    ('Greyhound',2020);

-- select * from most_popular_films
-- union
-- select * from top_rated_films;

-- select * from most_popular_films
-- intersect
-- select * from top_rated_films;

