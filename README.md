# Solana Token Tracker 🚀

Track the fastest-growing meme coins on Solana blockchain in (almost) real-time.

## How it works:

- Pulls top tokens with more than 100 holders every 5 seconds from Solscan.
- Stores snapshots of holders, price, and market cap into SQLite database.
- Calculates growth over last 5 seconds and last 5 minutes.
- Visualizes fastest-growing tokens in a dashboard.

## Run Locally

1. Clone the project
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Start data collection

```bash
python app/main.py
```

4. Open the dashboard

```bash
streamlit run dashboard.py
```

## Run with Docker

```bash
docker build -t sol-token-tracker .
docker run -it sol-token-tracker
```

## Notes

- Solscan public API has no key needed but respect the rate limits.
- Adjust sleep times if necessary (5 sec for now).
- Future: Add alerts via Telegram or Discord Bot!
