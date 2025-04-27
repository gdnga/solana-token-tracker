import sqlite3
from datetime import datetime

DB_NAME = 'tokens.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY,
            token_address TEXT,
            token_name TEXT,
            holders INTEGER,
            market_cap REAL,
            price_usdt REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_snapshot(tokens):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.utcnow()

    for token in tokens:
        c.execute('''
            INSERT INTO tokens (token_address, token_name, holders, market_cap, price_usdt, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (token['address'], token['tokenName'], token['holder'], token.get('marketCap', 0), token.get('priceUsdt', 0), now))

    conn.commit()
    conn.close()
