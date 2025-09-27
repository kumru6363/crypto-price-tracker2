import requests

API = "https://api.coingecko.com/api/v3/simple/price"

coins = ["bitcoin", "ethereum", "dogecoin"]
vs = "usd"

params = {
    "ids": ",".join(coins),
    "vs_currencies": vs,
    "include_24hr_change": "true"
}

response = requests.get(API, params=params)
data = response.json()

print(f"\n{'COIN':<12} {vs.upper():>12} {'24h %':>10}")
print("-"*36)
for coin in coins:
    price = data[coin][vs]
    change = data[coin].get(f"{vs}_24h_change", 0)
    print(f"{coin:<12} {price:>12,.2f} {change:>+10.2f}%")
print()
