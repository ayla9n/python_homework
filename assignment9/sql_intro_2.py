'''
Task 5: Read Data into a DataFrame
'''

import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    # Read data into a DataFrame with a JOIN
    df = pd.read_sql_query("""
        SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, 
               products.product_name, products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
    """, conn)

# Print first 5 lines
print(df.head())

# Add total column
df['total'] = df['quantity'] * df['price']
print(df.head())

#Group by product_id
summary = df.groupby('product_id').agg(
    line_item_id=('line_item_id', 'count'),
    total=('total', 'sum'),
    product_name=('product_name', 'first')
)
print(summary.head())

#Sort by product_name
summary = summary.sort_values('product_name')

#Write to CSV
summary.to_csv('order_summary.csv')
print(summary)