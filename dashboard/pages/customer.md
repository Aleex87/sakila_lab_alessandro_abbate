## Top Customers

```sql rental
SELECT
    customer,
    SUM(amount) AS total_amount,
    COUNT(*) AS number_of_rentals
FROM sakila.rental
group by customer_id, customer
order by total_amount desc, number_of_rentals desc
limit 10
;
```

<BarChart
    data={rental}
    title="Top customers in order of how much they have spent"
    x=customer
    y=total_amount
    swapXY= true
/>