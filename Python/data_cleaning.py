# 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np


pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)


# 2. FILE PATH
BASE_PATH = r"G:\Next-Gen Commerce & Logistics\Data\\"


# 3. LOAD DATASETS
customers = pd.read_csv(BASE_PATH + "olist_customers_dataset.csv")
orders = pd.read_csv(BASE_PATH + "olist_orders_dataset.csv")
items = pd.read_csv(BASE_PATH + "olist_order_items_dataset.csv")
payments = pd.read_csv(BASE_PATH + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(BASE_PATH + "olist_order_reviews_dataset.csv")
products = pd.read_csv(BASE_PATH + "olist_products_dataset.csv")

print(" All datasets loaded successfully")


# 4. BASIC DATA UNDERSTANDING
print("\n--- ORDERS INFO ---")
print(orders.info())

print("\n--- ORDERS SAMPLE ---")
print(orders.head())


# 5. CONVERT DATE COLUMNS
date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors='coerce')

print("\n Date columns converted")


# 6. MISSING VALUE CHECK
print("\n--- MISSING VALUES (ORDERS) ---")
print(orders.isnull().sum())


# 7. FILTER VALID ORDERS
orders_delivered = orders[orders['order_status'] == 'delivered'].copy()

print(f"\n Total Orders: {orders.shape[0]}")
print(f" Delivered Orders: {orders_delivered.shape[0]}")


# 8. FEATURE ENGINEERING

# Delivery Time (in days)
orders_delivered['delivery_time_days'] = (
    orders_delivered['order_delivered_customer_date'] -
    orders_delivered['order_purchase_timestamp']
).dt.days

# Estimated vs Actual Delay
orders_delivered['delivery_delay_days'] = (
    orders_delivered['order_delivered_customer_date'] -
    orders_delivered['order_estimated_delivery_date']
).dt.days

print("\n Delivery metrics created")


# 9. HANDLE NEGATIVE / INVALID VALUES
orders_delivered = orders_delivered[
    orders_delivered['delivery_time_days'] >= 0
]

# Replace NaN delay with 0 (delivered on/before estimated date)
orders_delivered['delivery_delay_days'] = orders_delivered['delivery_delay_days'].fillna(0)

print(" Invalid records removed")


# 10. MERGE CORE TABLES

# Orders + Customers
orders_customers = orders_delivered.merge(
    customers,
    on='customer_id',
    how='left'
)

# Orders + Payments
orders_payments = orders_customers.merge(
    payments,
    on='order_id',
    how='left'
)

# Orders + Reviews
final_df = orders_payments.merge(
    reviews[['order_id', 'review_score']],
    on='order_id',
    how='left'
)

print("\n Tables merged successfully")


# 11. FINAL DATASET CHECK
print("\n--- FINAL DATASET INFO ---")
print(final_df.info())

print("\n--- FINAL DATASET SAMPLE ---")
print(final_df.head())


# 12. SAVE CLEANED DATA
final_df.to_csv(
    r"G:\Next-Gen Commerce & Logistics\Data\cleaned_olist_commerce_data.csv",
    index=False
)

print("\n Cleaned dataset saved successfully")

