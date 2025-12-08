SELECT 
    p.amount,
    p.payment_date,
    r.rental_date,
    r.return_date,
    r.inventory_id,
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer,
    s.store_id,
    a.address,
    a.city_id,
    ci.city,
    co.country
FROM staging.payment p
LEFT JOIN staging.rental r ON p.rental_id = r.rental_id
LEFT JOIN staging.customer c ON c.customer_id = p.customer_id
LEFT JOIN staging.store s ON s.store_id = c.store_id
LEFT JOIN staging.address a ON c.address_id = a.address_id
LEFT JOIN staging.city ci ON a.city_id = ci.city_id
LEFT JOIN staging.country co ON ci.country_id = co.country_id
;
