SHOW DATABASES;
USE sakila;
SHOW TABLES;
SELECT * FROM customer;
SELECT * FROM rental;
SELECT email,COUNT(*) AS EC FROM customer GROUP BY email HAVING COUNT(*)>1;
SELECT * FROM film;
SELECT COUNT(*) FROM film WHERE description LIKE '%A%'OR description LIKE '%a%';
SELECT 
    SUM(LENGTH(description) - LENGTH(REPLACE(LOWER(description), 'a', ''))) AS a_count,
    SUM(LENGTH(description) - LENGTH(REPLACE(LOWER(description), 'e', ''))) AS e_count,
    SUM(LENGTH(description) - LENGTH(REPLACE(LOWER(description), 'i', ''))) AS i_count,
    SUM(LENGTH(description) - LENGTH(REPLACE(LOWER(description), 'o', ''))) AS o_count,
    SUM(LENGTH(description) - LENGTH(REPLACE(LOWER(description), 'u', ''))) AS u_count
FROM film;
#Display the payments made by each customer
 
SELECT * FROM payment;
#Month
Select Customer_id,sum(amount) as total_payment,MONTH(payment_date) as MPay,YEAR(payment_date) as YPay FROM payment Group by Customer_id,MONTH(payment_date),YEAR(payment_date) Order by Customer_id,MPay,YPay;
#YEAR
Select Customer_id,sum(amount) as total_payment,YEAR(payment_date) as YPay FROM payment Group by Customer_id,YEAR(payment_date) Order by Customer_id,YPay;
#WEEK
Select Customer_id,YEAR(payment_date) as YPay, WEEK(payment_date) as WPay,
sum(amount) as total_payment FROM payment
 Group by Customer_id,YEAR(payment_date),WEEK(payment_date)
  Order by Customer_id,YPay,WPay;

SELECT YEAR(payment_date) AS p FROM payment GROUP BY YEAR(payment_date) HAVING p % 400 = 0;
SELECT YEAR(create_date) AS p FROM customer GROUP BY YEAR(create_date) HAVING p % 400 = 0;

SELECT DATEDIFF(
    CONCAT(YEAR(CURDATE()), '-12-31'),
    CURDATE()
) AS days_remaining;

 select payment_date,concat('Q', quarter(payment_date)) as QPAY from payment;