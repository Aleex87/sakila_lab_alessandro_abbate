---
title: Rental Analysis
---

# Rental Analysis

This page explores rental activity across stores, customers, and cities.  
These insights help identify where demand is highest and how rentals evolve over time.

---

## Rental Activity Overview

```sql rentals_overview
SELECT 
    COUNT(*) AS total_rentals,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(DISTINCT store_id) AS stores_involved
FROM sakila.rental;
```

---

## Top 5 Cityes by number of rentals

```sql top_cityes
SELECT 
    ci.city,
    COUNT(*) AS rental_count
FROM sakila.rental r
JOIN sakila.address a ON r.customer_id = a.address_id
JOIN sakila.city ci ON a.city_id = ci.city_id
GROUP BY ci.city
ORDER BY rental_count DESC
LIMIT 5;
```
<BarChart 
    data={top_cityes}
    title="Top 5 Cities by Rentals"
    x="city"
    y="rental_count"
/>


---


## Whic store have more rental?


```sql rentals_per_store
SELECT 
    s.store_id,
    COUNT(*) AS rental_count
FROM sakila.rental r
LEFT JOIN sakila.inventory i ON r.inventory_id = i.inventory_id
LEFT JOIN sakila.store s ON i.store_id = s.store_id
GROUP BY s.store_id
ORDER BY rental_count DESC;
```

<BarChart
    title="Rentals per Store"
    data={rentals_per_store}
    x="store_id"
    y="rental_count"
/>

--- 

## Montly Rental Trend 


```sql montly_rental
SELECT 
    DATE_TRUNC('month', rental_date) AS month,
    COUNT(*) AS rentals
FROM sakila.rental
WHERE rental_date BETWEEN '2005-05-01' AND '2006-02-28'
GROUP BY month
ORDER BY month;
```

<LineChart 
    title="Monthly Rentals "
    data={montly_rental}
    x="month"
    y="rentals"
/>

## Customer & Rental Activity Overview
This page shows the total number of customers in the database and confirms that there are two active stores. We identify the cities with the highest film-rental activity and determine which store has rented out the most films. The analysis also highlights that the database contains limited non-zero entries for rental counts; however, based on the available data, rental activity peaks in the months of July and August.