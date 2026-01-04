import pandas as pd

data = pd.read_json("bitcoin_data.json") # reads json data into pandas
flip = data.to_csv("bitcoin_data.csv") # converts json data into CSV file format

df = pd.DataFrame(data) # make a table with rows and column from data

# token_symbol = df["symbol"]

token_id = df.iloc[0,0] # prints bitcoin


print(token_id)