import requests
import json

api_key = "CG-hfBEmf4GKtLd83FfP61qwDV9"
coin_name = input("Enter coin name: ")

base_url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin_name}&x_cg_demo_api_key={api_key}"

response = requests.get(base_url)
data = json.loads(response.text)
print(data)