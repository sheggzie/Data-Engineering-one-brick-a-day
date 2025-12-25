# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "Umbreon"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print("Name", pokemon_info["name"].capitalize())
#     print("ID", pokemon_info["id"])
#     print("Height", pokemon_info["height"])
#     print("Weight", pokemon_info["weight"])


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