SHOW DATABASES;
USE sakila;
#display all customer details who have made more than 5 payments.
select * from customer where customer_id in (select customer_id from payment group by customer_id having count(payment_id) > 5);
#Find the names of actors who have acted in more than 10 films.
SELECT * FROM actor WHERE actor_id in(select actor_id from film_actor group BY actor_id HAVING COUNT(film_id)>10);
#Find the names of customers who never made a payment.
select * from customer where customer_id NOT in (select customer_id from payment);
#List all films whose rental rate is higher than the average rental rate of all films.
SELECT title FROM film WHERE rental_rate > (select AVG(rental_rate) FROM film);
#List the titles of films that were never rented.
SELECT * FROM film WHERE rental_duration IS NULL;
# Display the customers who rented films in the same month as customer with ID 5.
SELECT* from rental;
SELECT * FROM customer WHERE customer_id in (select customer_id FROM rental WHERE MONTH(rental_date) IN (select month(rental_date) FROM rental WHERE customer_id=5));
#Find all staff members who handled a payment greater than the average payment amount.
SELECT* from payment;
SELECT* from staff;
SELECT first_name,last_name FROM staff WHERE staff_id IN (Select staff_id from payment where amount >(Select Avg(amount) FROM payment));
#Show the title and rental duration of films whose rental duration is greater than the average.
SELECT * FROM film;
SELECT title,rental_duration FROM film GROUP BY title,rental_duration HAVING rental_duration>(select avg(rental_duration) FROM film);
#Find all customers who have the same address as customer with ID 1.
SELECT * FROM customer;
SELECT * FROM customer WHERE address_id = (select address_id FROM customer WHERE customer_id=1);
#List all payments that are greater than the average of all payments.
SELECT * FROM payment;
SELECT * FROM payment WHERE amount>(Select AVG(AMOUNT) FROM payment);
