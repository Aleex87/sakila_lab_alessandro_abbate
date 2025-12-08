---
title: Rental Analysis
---

# 🎬 Rental Analysis

This page explores rental activity across stores, customers, and cities.  
These insights help identify where demand is highest and how rentals evolve over time.

---

## 📌 Rental Activity Overview

```sql rentals_overview
SELECT 
    COUNT(*) AS total_rentals,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(DISTINCT store_id) AS stores_involved
FROM sakila.rental;
```

---

# Top 5 Cityes by number of rentals

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
