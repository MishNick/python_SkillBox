SELECT
    o.order_no,
    c.full_name AS customer_name,
    m.full_name AS seller_name
FROM "order" o
JOIN customer c ON o.customer_id = c.customer_id
JOIN manager m ON o.manager_id = m.manager_id
WHERE c.city <> m.city;
