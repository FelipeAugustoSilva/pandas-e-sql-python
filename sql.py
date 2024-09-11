import sqlite3

conn = sqlite3.connect('web1.db')

import pandas as pd

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
print(df_data)
df_data.to_sql('data', conn, index_label='index_name')

c = conn.cursor()
c.execute('CREATE TABLE products (product_id, product_name, price)')
conn.commit()