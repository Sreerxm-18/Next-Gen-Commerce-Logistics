/* USE master;
GO */

/* CREATE DATABASE NextGenCommerceLogistics;
GO */

USE NextGenCommerceLogistics;
GO

CREATE TABLE commerce_logistics (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(20),

    order_purchase_timestamp DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME,

    delivery_time_days INT,
    delivery_delay_days INT,
    is_late BIT,

    payment_type VARCHAR(30),
    payment_value FLOAT,

    review_score INT,

    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
);
GO
