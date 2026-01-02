import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-LK7QOGB9\SQLEXPRESS;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sys.databases")
print("Connection successful")

conn.close()
