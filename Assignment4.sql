SHOW DATABASES;
USE sakila;
#List all customers along with the films they have rented.
SELECT * FROM customer;
SELECT * FROM film;
SELECT * FROM rental;
SELECT * FROM inventory;
select c.customer_id, c.first_name, c.last_name, f.title from customer c join rental r on c.customer_id = r.customer_id
join inventory i
 on r.inventory_id = i.inventory_id
join film f
 on i.film_id = f.film_id;

#List all customers and show their rental count, including those who haven't rented any films.
SELECT * FROM customer;
SELECT * FROM rental;
select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as rental_count from customer c
left join rental r
on c.customer_id = r.customer_id
group by c.customer_id, c.first_name, c.last_name;

#Show all films along with their category. Include films that don't have a category assigned.
SELECT * FROM category;
SELECT * FROM film;
SELECT * FROM rental;
select f.film_id, f.title, c.name as category from film f
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id = c.category_id;
#Show all customers and staff emails from both customer and staff tables using a full outer join (simulate using LEFT + RIGHT + UNION).
SELECT * FROM customer;
SELECT * FROM staff;
SELECT * FROM store;
select c.email as customer_email, s.email as staff_email from customer c
left join staff s on c.store_id = s.store_id union select c.email as customer_email, s.email as staff_email
from customer c
right join staff s
 on c.store_id = s.store_id;
#Find all actors who acted in the film "ACADEMY DINOSAUR".
SELECT * FROM actor;
SELECT * FROM film;
SELECT * FROM film_actor;
select a.actor_id, a.first_name, a.last_name from actor a
join film_actor FA
 on a.actor_id = FA.actor_id
join film f
 on FA.film_id = f.film_id
where f.title = 'ACADEMY DINOSAUR';
#List all stores and the total number of staff members working in each store, even if a store has no staff.
SELECT * FROM store;
SELECT * FROM staff;
select ST.store_id, count(s.staff_id) as total_staff
from store ST
left join staff s
 on ST.store_id = s.store_id
group by ST.store_id;
#List the customers who have rented films more than 5 times. Include their name and total rental count.
SELECT * FROM customer;
SELECT * FROM rental;
select c.customer_id, c.first_name, c.last_name, count(rental_id) as total_rental
from customer c
join rental r
 on c.customer_id = r.customer_id
group by c.customer_id, c.first_name, c.last_name
having total_rental > 5;