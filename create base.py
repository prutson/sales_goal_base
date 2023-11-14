import pandas as pd
import sqlite3

# Set the limit date for filtering
limit_date = '2021-05-01'

# Read data from the CSV file
df_csv = pd.read_csv('superstore.csv', sep=';')
df_csv['Sales'] = df_csv['Sales'].str.replace(',', '.', regex=True)

# Remove commas and convert the "Sales" column to float
df_csv['Sales'] = df_csv['Sales'].str.replace(',', '', regex=True).astype(float)

# Convert the "Order Date" column to date format
df_csv['Order Date'] = pd.to_datetime(df_csv['Order Date'], format='%d/%m/%Y')

# Filter rows with dates before "01/05/2021"
df_csv = df_csv[df_csv['Order Date'] < limit_date]

# Create a connection to an in-memory SQLite database
connection = sqlite3.connect(':memory:')

# Load CSV DataFrame data into the SQLite database
df_csv.to_sql('superstore', connection, index=False)

# Read the SQL query from the query.sql file
with open('query.sql', 'r') as file:
    sql_query = file.read()

# Execute the query and load the results into a pandas DataFrame
df_sql = pd.read_sql_query(sql_query, connection)

# Convert the "META" column to float
df_sql['Meta'] = df_sql['Meta'].astype(float)

# Convert date columns to the appropriate format
df_sql['start_date'] = pd.to_datetime(df_sql['start_date'])
df_csv['Order Date'] = pd.to_datetime(df_csv['Order Date'], format='%d/%m/%Y')

# Perform a LEFT JOIN between DataFrames
result_df = pd.merge(df_sql, df_csv, how='left', left_on=['Category', 'Sub-Category', 'start_date'], right_on=['Category', 'Sub-Category', 'Order Date'])

# Remove the "Sub" and "Order Date" columns
result_df = result_df.drop(columns=['Order Date'])

# Rename columns "start_date" to "date" and "Sub-Category" to "product"
result_df = result_df.rename(columns={'start_date': 'Date', 'Sub-Category': 'Product'})

# Display the resulting DataFrame
print(result_df.head())

# Export the DataFrame to a CSV file
result_df.to_csv('resultado.csv', sep=';', index=False)
