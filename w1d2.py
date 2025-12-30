import json
import pandas as pd

json_file = "pokemon_data.json"


data = pd.read_json(json_file)  # read json file contents and assign to data
data.to_csv('pokemon_data_table.csv')   # convert contents in data to csv