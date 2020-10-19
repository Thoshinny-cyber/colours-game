import pandas as pd
import sqlite3

conn = sqlite3.connect('Data.db')
df=pd.read_sql_query("SELECT * from credentials", conn)

print(df.head())

conn.close()
