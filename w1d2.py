import json
import pandas as pd

json_file = "pokemon_data.json"


data = pd.read_json(json_file)  # read json file contents and assign to data
data.to_csv('pokemon_data_table.csv')   # convert contents in data to csv

# function to remove empty columns from csv file 
def clean_csv():
    df = pd.read_csv('pokemon_data_table.csv')
    df.drop(columns=['count', 'previous'], inplace=True) # drop/remove two columns as named in the array

    df.to_csv("pokemon_data_table_cleaned.csv", index=False) # rewrite cleaned csv to new file
        
clean_csv()
