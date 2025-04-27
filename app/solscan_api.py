import requests

def fetch_tokens():
    url = "https://public-api.solscan.io/token/list?sortBy=holder&direction=desc&limit=200"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers).json()
    return [token for token in response['data'] if token['holder'] > 100]
