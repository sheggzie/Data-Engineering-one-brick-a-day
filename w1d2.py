import json
import pandas as pd

json_file = "pokemon_data.json"

data = pd.read_json(json_file)
data.to_csv('pokemon_data_table.csv')
