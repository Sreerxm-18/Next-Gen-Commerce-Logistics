# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# File Path
BASE_PATH = r"G:\Next-Gen Commerce & Logistics\Data\\"

# Load Datasets
customers = pd.read_csv(BASE_PATH + "olist_customers_dataset.csv")
orders = pd.read_csv(BASE_PATH + "olist_orders_dataset.csv")
items = pd.read_csv(BASE_PATH + "olist_order_items_dataset.csv")
payments = pd.read_csv(BASE_PATH + "olist_order_payments_dataset.csv")
reviews = pd.read_csv(BASE_PATH + "olist_order_reviews_dataset.csv")
products = pd.read_csv(BASE_PATH + "olist_products_dataset.csv")

print("All datasets loaded successfully")

# Date Conversion
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

print("Date columns converted")

# Filter Delivered Orders
orders = orders[orders["order_status"] == "delivered"].copy()
print("Delivered orders count:", orders.shape[0])

# Feature Engineering
orders["delivery_time_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.days

orders["delivery_delay_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_estimated_delivery_date"]
).dt.days

orders = orders[orders["delivery_time_days"] >= 0]
orders["delivery_delay_days"] = orders["delivery_delay_days"].fillna(0)

orders["is_late"] = orders["delivery_delay_days"] > 0

print("Delivery metrics created")

# Merge Tables
df = orders.merge(customers, on="customer_id", how="left")
df = df.merge(payments, on="order_id", how="left")
df = df.merge(
    reviews[["order_id", "review_score"]],
    on="order_id",
    how="left"
)

print("Tables merged successfully")

# Save Cleaned Dataset
clean_path = BASE_PATH + "cleaned_olist_commerce_data.csv"
df.to_csv(clean_path, index=False)

print("Cleaned dataset saved")

# Exploratory Data Analysis

# KPI Summary
print("\nKPI Summary")
print("Average Delivery Time (Days):", round(df["delivery_time_days"].mean(), 2))
print("Late Delivery Percentage (%):", round(df["is_late"].mean() * 100, 2))
print("Average Review Score:", round(df["review_score"].mean(), 2))

# Delivery Time Distribution
plt.figure(figsize=(8, 5))
df["delivery_time_days"].hist(bins=30)
plt.title("Delivery Time Distribution (Days)")
plt.xlabel("Days")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()

# Review Score by Delivery Status
review_by_delay = df.groupby("is_late")["review_score"].mean()
print("\nReview Score by Delivery Status")
print(review_by_delay)

# Top Cities by Order Volume
top_cities = df["customer_city"].value_counts().head(10)
print("\nTop 10 Cities by Order Volume")
print(top_cities)

# Cities with Highest Delivery Delay
city_delay = (
    df.groupby("customer_city")["delivery_delay_days"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nCities with Highest Average Delivery Delay")
print(city_delay)

print("\nPython phase completed successfully")
print("Dataset is ready for SQL Server and Power BI")
