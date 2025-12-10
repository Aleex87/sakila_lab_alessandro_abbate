## Film Analysis

This page explores the film dataset from the Sakila database.  
Below you will find a few metadata that the tabel film holds in. 

---

## Sample of Films

```sql films_sample
SELECT film_id, title, release_year, rating, length, rental_rate
FROM sakila.film
LIMIT 10;
```
---

## We can also examine the film categories included in the database and determine how many films belong to each category.

```sql film_category 
SELECT 
    c.name AS category,
    COUNT(*) AS film_count
FROM sakila.category c
JOIN sakila.film_category fc 
    ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY film_count DESC;
```
---
<BarChart 
   data={film_category}
   title="Type of category present in the database"
   x=category
   y=film_count
   swapXY
   />


## Now we can look at the film ratings and see how many films fall into each rating category.

```sql reating
SELECT rating, COUNT(*) AS number_of_film
FROM sakila.film
GROUP BY rating
ORDER BY number_of_film DESC;

```
<BarChart 
   data={reating}
   title="Type of reating present in the database and how many film per rating"
   x=rating
   y=number_of_film
   />
   
The Sakila dataset provides a rich collection of film-related attributes, including titles, lengths, rental costs, and production years. Analysis of the dataset shows that Sports films emerge as the most frequently rented genre, indicating a strong customer preference for this category.