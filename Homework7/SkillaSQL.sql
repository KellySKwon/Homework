-- SQL Homework using sakila database;
use sakila;

-- 1a. Display the first and last names of all actors from the table `actor`.
describe  actor;
select first_name,last_name from sakila.actor;

/*1b. Display the first and last name of each actor in a single column in upper case letters. 
Name the column `Actor Name`.*/
select 
concat(upper(first_name),' ',upper(last_name)) as 'Actor Name' 
from sakila.actor;

/*2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
What is one query would you use to obtain this information?*/
select actor_id, first_name, last_name from sakila.actor where first_name='Joe';

-- 2b. Find all actors whose last name contain the letters `GEN`:
select * from sakila.actor where last_name like '%gen%';

/*2c. Find all actors whose last names contain the letters `LI`. 
This time, order the rows by last name and first name, in that order:*/
select * from sakila.actor where last_name like '%li%' order by last_name, first_name;

/*2d. Using `IN`, display the `country_id` and `country` columns of the following countries: 
Afghanistan, Bangladesh, and China:
*/
describe sakila.country;
select country_id,country from sakila.country where country in ('Afghanistan','Bangladesh','China');

/*3a. You want to keep a description of each actor. 
You don't think you will be performing queries on a description, 
so create a column in the table `actor` named `description` and use the data type `BLOB` 
(Make sure to research the type `BLOB`, as the difference between it and `VARCHAR` are significant).*/

alter table sakila.actor
add column description blob null after last_update;

/* 3b. Very quickly you realize that entering descriptions for each actor is too much effort. 
Delete the `description` column.*/

alter table sakila.actor
drop column description;

describe sakila.actor;

/*4a. List the last names of actors, as well as how many actors have that last name.*/

select last_name,count(*) as CntLastName from sakila.actor group by last_name;

/*4b. List last names of actors and the number of actors who have that last name, 
but only for names that are shared by at least two actors*/

select last_name,count(*) as CntLastName
from sakila.actor 
group by last_name
having CntLastName>1;

/*4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`. 
Write a query to fix the record.*/

update sakila.actor
set first_name = 'HARPO'
where first_name = 'GROUCHO' and last_name = 'WILLIAMS';

/*4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. 
It turns out that `GROUCHO` was the correct name after all! 
In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.*/
update sakila.actor
set first_name = 'GROUCHO'
where first_name = 'HARPO' and last_name = 'WILLIAMS';

-- check if replaced Harpo
select * from sakila.actor where last_name = 'WILLIAMS';

/*5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
Hint: [https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html]
(https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html)
*/

SHOW CREATE TABLE sakila.address;

/*6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. 
Use the tables `staff` and `address`:*/
describe sakila.address;
describe sakila.staff;

select s.first_name,s.last_name,a.address from sakila.staff s
join sakila.address a on s.address_id = a.address_id;

/* 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. 
Use tables `staff` and `payment`.*/
describe sakila.payment;
select * from sakila.payment limit 10;

select sum(p.amount) as TotalAmount, s.staff_id, s.first_name, s.last_name
from sakila.payment p join sakila.staff s on p.staff_id = s.staff_id
where p.payment_date>= '2005-08-01 00:00:00' and p.payment_date<'2005-09-01 00:00:00'
group by s.staff_id;

/*6c. List each film and the number of actors who are listed for that film. 
Use tables `film_actor` and `film`. Use inner join.*/

select f.title, count(distinct a.actor_id) as CntActors 
from sakila.film f inner join sakila.film_actor a on f.film_id = a.film_id group by f.title; 

/* 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?*/

select f.title, count(i.inventory_id) as Copies from sakila.film f 
join sakila.inventory i on f.film_id = i.film_id where f.title = 'hunchback impossible';

/*6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. 
List the customers alphabetically by last name:*/

select * from payment limit 10;
select * from customer limit 10;

select c.customer_id,c.first_name,c.last_name,sum(amount) as TotalPaid
from sakila.customer c join sakila.payment p on c.customer_id = p.customer_id
group by c.customer_id;

/*7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. 
Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.
*/

select title from sakila.film
where (title like 'k%' or title like 'q%') and 
language_id = (select language_id from sakila.language where name = 'English'); 

/*7b. Use subqueries to display all actors who appear in the film `Alone Trip`.*/

select a.first_name,a.last_name 
from sakila.actor a join sakila.film_actor fa on a.actor_id = fa.actor_id
where fa.film_id in (select film_id from sakila.film where title = 'alone trip');

/* 7c. You want to run an email marketing campaign in Canada, 
for which you will need the names and email addresses of all Canadian customers. 
Use joins to retrieve this information.
	join country_id with city, country (where country = canada)
    join city_id with address
    join address_id with customer*/

select c.customer_id, c.first_name, c.last_name, c.email 
from sakila.customer c
join sakila.address a on c.address_id = a.address_id
join sakila.city ct on a.city_id = ct.city_id
join sakila.country cr on cr.country_id = ct.country_id
where cr.country='canada';

/* 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
Identify all movies categorized as _family_ films.*/

select f.title,c.name as category from sakila.film f
join sakila.film_category fc on f.film_id = fc.film_id
join sakila.category c on c.category_id = fc.category_id
where c.name like 'family';

/* 7e. Display the most frequently rented movies in descending order.*/

select f.title,count(*) as Rentals from sakila.film f
join inventory i on i.film_id = f.film_id
join rental r on r.inventory_id = i.inventory_id
group by f.title
order by f.title desc;

/* 7f. Write a query to display how much business, in dollars, each store brought in.*/

select s.store_id, sum(p.amount) as StoreTotal from sakila.payment p
join sakila.customer c on c.customer_id = p.customer_id 
join sakila.store s on s.store_id = c.customer_id
group by s.store_id;

/* 7g. Write a query to display for each store its store ID, city, and country.*/

select s.store_id,c.city,cc.country from sakila.store s
join sakila.address a on a.address_id = s.address_id
join sakila.city c on c.city_id = a.city_id
join sakila.country cc on cc.country_id = c.country_id;


/* 7h. List the top five genres in gross revenue in descending order. 
(**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)*/

select cat.name as Category, sum(p.amount) as GrossRevenue from category cat
join film_category fm on fm.category_id = cat.category_id
join inventory i on i.film_id = fm.film_id
join rental r on r.inventory_id = i.inventory_id
join payment p on p.rental_id = r.rental_id
group by cat.name
order by GrossRevenue desc limit 5;

/* 8a. In your new role as an executive, you would like to have an easy way of viewing the 
Top five genres by gross revenue. Use the solution from the problem above to create a view. 
If you haven't solved 7h, you can substitute another query to create a view.*/

DROP VIEW IF EXISTS top_five_genres;
CREATE VIEW top_five_genres as (
select cat.name as Category, sum(p.amount) as GrossRevenue from category cat
join film_category fm on fm.category_id = cat.category_id
join inventory i on i.film_id = fm.film_id
join rental r on r.inventory_id = i.inventory_id
join payment p on p.rental_id = r.rental_id
group by cat.name
order by GrossRevenue desc limit 5);

/* 8b. How would you display the view that you created in 8a?*/
select * from top_five_genres;

/* 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.*/
DROP VIEW IF EXISTS top_five_genres;
