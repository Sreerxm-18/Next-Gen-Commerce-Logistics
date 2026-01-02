import pandas as pd
from sqlalchemy import create_engine
import urllib

# Load cleaned dataset
df = pd.read_csv(
    r"G:\Next-Gen Commerce & Logistics\Data\cleaned_olist_commerce_data.csv"
)

# Select only columns that exist in SQL table
df_sql = df[
    [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "delivery_time_days",
        "delivery_delay_days",
        "is_late",
        "payment_type",
        "payment_value",
        "review_score",
        "customer_city",
        "customer_state"
    ]
]

# SQL Server connection
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-LK7QOGB9\\SQLEXPRESS;"
    "DATABASE=NextGenCommerceLogistics;"
    "Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Insert data
df_sql.to_sql(
    name="commerce_logistics",
    con=engine,
    if_exists="append",
    index=False
)

print("Data inserted into SQL Server successfully")
