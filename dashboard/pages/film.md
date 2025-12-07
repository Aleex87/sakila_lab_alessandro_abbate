---
title: Film Analysis
---

# 🎥 Film Analysis

This page explores the film dataset from the Sakila database.  
Below you will find summary information, category distributions, and sample data.

---

## 📌 Sample of Films

```sql films_sample
SELECT film_id, title, release_year, rating, length, rental_rate
FROM sakila.film
LIMIT 10;
```

```sql film_category 
    SELECT 
        c.name AS category,
        COUNT (*) AS film_count
    FROM category c
    JOIN film_category fc ON c.category_id = fc. category_id
    GROUP BY c.name 
    ORDER BY film_count DESC;
```
