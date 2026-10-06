SHOW DATABASES;
USE sakila;
SHOW Tables;
SELECT * From film;
SELECT * FROM customer WHERE first_name LIKE 'J%' AND active;
SELECT * FROM film Where title Like'%ACTION%' OR description LIKE'%WAR%';
SELECT * FROM customer WHERE first_name LIKE'%a' AND last_name NOT LIKE'SMITH';
SELECT * FROM film WHERE rental_rate>3 AND replacement_cost Is NOT Null;
SELECT store_id,COUNT(customer_id) FROM customer WHERE active=1 group by store_id;
SELECT DISTINCT rating FROM film;
SELECT * From film;
select rental_duration,count(*) as Tfilm  from film GROUP BY rental_duration HAVING AVG(length)>100;
SELECT * From rental;
#List payment dates and total amount paid per date, but only include days where more than 100 payments were made.
SELECT * from payment;
SELECT DATE(payment_date) as d,SUM(amount) as PPD from payment GROUP BY DATE(payment_date) Having COUNT(*)>100 ORDER BY payment_date;
SELECT * from film where rating  LIKE'G' OR rating LIKE'PG' ORDER BY rental_rate DESC;
 #Count how many films exist for each length where the film title starts with 'T' and the count is more than 5.
SELECT length,count(film_id) as t FROM film WHERE title LIKE 'T%' GROUP BY length HAVING count(film_id) >=1;
SELECT * FROM film_actor;
#List all actors who have appeared in more than 10 films.
SELECT actor_id,COUNT(film_id) as t from film_actor GROUP BY actor_id HAVING t>10;
#Find the top 5 films with the highest rental rates and longest lengths combined, ordering by rental rate first and length second.
SELECT * FROM film;
#Find the top 5 films with the highest rental rates and longest lengths combined, ordering by rental rate first and length second.
SELECT title,rental_rate,length as movie FROM film ORDER BY rental_rate DESC , length DESC Limit 5;
SELECT * From rental;
#Show all customers along with the total number of rentals they have made, ordered from most to least rentals.
SELECT customer_id,COUNT(customer_id) as C FROM rental GROUP BY customer_id ORDER BY COUNT(customer_id)DESC;
#List the film titles that have never been rented.
SELECT title FROM film WHERE rental_duration IS NULL;


