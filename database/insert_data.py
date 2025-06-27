import pandas as pd
import mysql.connector

# Load the Excel file
file_path = input("Enter the path to your Excel file (e.g., .\\data\\HINDALCO_1D.xlsx): ")
df = pd.read_excel(file_path)
print("Columns found in your file:", df.columns.tolist())

# Ask user to map columns
datetime_col = input("Which column is datetime? ")
open_col = input("Which column is open? ")
high_col = input("Which column is high? ")
low_col = input("Which column is low? ")
close_col = input("Which column is close? ")
volume_col = input("Which column is volume? ")

df = df.rename(columns={
    datetime_col: 'datetime',
    open_col: 'open',
    high_col: 'high',
    low_col: 'low',
    close_col: 'close',
    volume_col: 'volume'
})

db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',  
    password='Jaspreet-123',
    database='sma_trading'
)
cursor = db.cursor()

truncate = input("Do you want to clear the existing data in the table first, Jaspreet? (y/n): ")
if truncate.lower() == 'y':
    cursor.execute("TRUNCATE TABLE stock_data")

insert_query = """
INSERT INTO stock_data (datetime, open, high, low, close, volume)
VALUES (%s, %s, %s, %s, %s, %s)
"""

data = df[['datetime', 'open', 'high', 'low', 'close', 'volume']].values.tolist()
cursor.executemany(insert_query, data)
db.commit()

print("Data inserted into MySQL successfully!")

cursor.close()
db.close()