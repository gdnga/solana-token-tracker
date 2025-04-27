import time
from app.db import init_db, store_snapshot
from app.solscan_api import fetch_tokens

def main():
    init_db()
    while True:
        tokens = fetch_tokens()
        store_snapshot(tokens)
        print(f"Snapshot saved. Tokens fetched: {len(tokens)}")
        time.sleep(5)

if __name__ == "__main__":
    main()
