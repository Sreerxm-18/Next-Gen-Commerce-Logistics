USE NextGenCommerceLogistics;
GO

/* 1. TOTAL ORDERS */
SELECT 
    COUNT(*) AS total_orders
FROM commerce_logistics;
GO

/* 2. AVERAGE DELIVERY TIME */
SELECT 
    AVG(CAST(delivery_time_days AS FLOAT)) AS avg_delivery_time_days
FROM commerce_logistics;
GO

/* 3. LATE DELIVERY PERCENTAGE */
SELECT 
    AVG(CAST(is_late AS FLOAT)) * 100 AS late_delivery_percentage
FROM commerce_logistics;
GO

/* 4. REVIEW SCORE IMPACT */
SELECT
    CASE 
        WHEN is_late = 1 THEN 'Late Delivery'
        ELSE 'On-Time Delivery'
    END AS delivery_status,
    AVG(CAST(review_score AS FLOAT)) AS avg_review_score
FROM commerce_logistics
GROUP BY is_late;
GO

/* 5. CITY-LEVEL LOGISTICS ISSUES */
SELECT TOP 10
    customer_city,
    AVG(CAST(delivery_delay_days AS FLOAT)) AS avg_delay_days,
    COUNT(*) AS total_orders
FROM commerce_logistics
GROUP BY customer_city
ORDER BY avg_delay_days DESC;
GO

/* 6. PAYMENT PERFORMANCE */
SELECT
    payment_type,
    COUNT(*) AS total_orders,
    SUM(CAST(payment_value AS FLOAT)) AS total_revenue,
    AVG(CAST(payment_value AS FLOAT)) AS avg_order_value
FROM commerce_logistics
GROUP BY payment_type
ORDER BY total_revenue DESC;
GO

/* 7. ON-TIME VS LATE DISTRIBUTION */
SELECT
    CASE 
        WHEN is_late = 1 THEN 'Late'
        ELSE 'On-Time'
    END AS delivery_status,
    COUNT(*) AS order_count
FROM commerce_logistics
GROUP BY is_late;
GO
