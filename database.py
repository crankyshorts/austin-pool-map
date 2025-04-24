import sqlite3
import requests
import pandas as pd

# Fetch data

url = "https://data.austintexas.gov/Locations-and-Maps/Pool-Map/jfqh-bqzu"
response = requests.get(url)
data = response.json()


# Convert to DataFrame

df = pd.DataFrame(data)

# Save to SQLite

conn = sqlite3.connect("pools.db")
df.to_sql("pools", conn, if_exists="replace", index=False)
conn.close()
