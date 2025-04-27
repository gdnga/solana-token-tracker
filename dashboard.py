import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

DB_NAME = 'tokens.db'

st.title("🚀 Fastest Growing Solana Meme Coins")

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

now = datetime.utcnow()

# Get tokens snapshots from last 5 minutes
time_limit = now - timedelta(minutes=5)

query = '''
SELECT token_address, token_name, MAX(holders) as max_holders, MIN(holders) as min_holders,
       MAX(price_usdt) as max_price, MIN(price_usdt) as min_price,
       MAX(market_cap) as max_marketcap, MIN(market_cap) as min_marketcap
FROM tokens
WHERE timestamp > ?
GROUP BY token_address, token_name
HAVING max_holders - min_holders > 0
ORDER BY (max_holders - min_holders) DESC
LIMIT 20
'''

df = pd.read_sql_query(query, conn, params=(time_limit,))
conn.close()

if df.empty:
    st.write("No growing tokens detected yet. 🚀")
else:
    df['holder_growth'] = df['max_holders'] - df['min_holders']
    df['price_change_$'] = df['max_price'] - df['min_price']
    df['marketcap_change_$'] = df['max_marketcap'] - df['min_marketcap']

    st.dataframe(df[['token_name', 'holder_growth', 'price_change_$', 'marketcap_change_$']])
