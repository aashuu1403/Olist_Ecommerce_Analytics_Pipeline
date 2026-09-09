import pandas as pd
import sqlite3

# 1. Load all datasets
print("Loading CSV files...")
orders = pd.read_csv('data/olist_orders_dataset.csv')
items = pd.read_csv('data/olist_order_items_dataset.csv')
products = pd.read_csv('data/olist_products_dataset.csv')
translations = pd.read_csv('data/product_category_name_translation.csv')
customers = pd.read_csv('data/olist_customers_dataset.csv')
payments = pd.read_csv('data/olist_order_payments_dataset.csv')
sellers = pd.read_csv('data/olist_sellers_dataset.csv')

# 2. Fix Data Types: Convert string dates to datetime objects
print("Cleaning timestamps...")
date_columns = [
    'order_purchase_timestamp', 'order_approved_at', 
    'order_delivered_carrier_date', 'order_delivered_customer_date', 
    'order_estimated_delivery_date'
]
for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])

# 3. Clean and Merge: Translate product categories to English
print("Translating product categories...")
products = pd.merge(products, translations, on='product_category_name', how='left')
products.drop('product_category_name', axis=1, inplace=True)
products.rename(columns={'product_category_name_english': 'product_category'}, inplace=True)

# 4. Handle Missing Values
orders.dropna(subset=['order_delivered_customer_date'], inplace=True)

# 5. Create the SQL Database
print("Exporting data to SQLite database...")
# This creates a local database file in your project folder
conn = sqlite3.connect('ecommerce_analytics.db')

# Write each dataframe to a separate table in the database
orders.to_sql('orders', conn, if_exists='replace', index=False)
items.to_sql('order_items', conn, if_exists='replace', index=False)
products.to_sql('products', conn, if_exists='replace', index=False)
customers.to_sql('customers', conn, if_exists='replace', index=False)
payments.to_sql('payments', conn, if_exists='replace', index=False)
sellers.to_sql('sellers', conn, if_exists='replace', index=False)

conn.close()
print("\nSuccess! 'ecommerce_analytics.db' has been created in your project folder.")