import requests
import json

api_key = "CG-hfBEmf4GKtLd83FfP61qwDV9"     # my API key to access info from the server
coin_name = input("Enter coin name: ")      # a prompt variable that asks for token name to be queried from API

api_url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin_name}&x_cg_demo_api_key={api_key}"

response = requests.get(api_url)            #  gets data from the API using the requests module method
data = json.loads(response.text)    

with open(f"{coin_name}_data.json", "w") as file:   # writes a new file with the token name as title based on entry in the prompt
    json_data = json.dump(data, file)     
print(data)