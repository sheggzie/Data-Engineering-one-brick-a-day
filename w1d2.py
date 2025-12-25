import requests
import json

base_url = "https://pokeapi.co/api/v2/pokemon"

def get_pokemon_info():
    response = requests.get(base_url)

    response_json = json.loads(response.text)
    
    with open("pokemon_data", "w") as file:
        data = json.dump(response_json, file)
    print(data)
     
get_pokemon_info()