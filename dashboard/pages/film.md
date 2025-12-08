---
title: Film Analysis
---

# 🎥 Film Analysis

This page explores the film dataset from the Sakila database.  
Below you will find a few metadata yhey  the tabel film holds in. 

---

## 📌 Sample of Films

```sql films_sample
SELECT film_id, title, release_year, rating, length, rental_rate
FROM sakila.film
LIMIT 10;
```
---

Now we can look at which film categories are in this database and how many film hold every category.

---
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


# Now we can look at the film rating and how many film there are in each reating type:

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
   
