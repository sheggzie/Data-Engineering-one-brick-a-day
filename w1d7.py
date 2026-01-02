import pandas as pd

data = pd.read_json("bitcoin_data.json")
flip = data.to_csv("bitcoin_data.csv")

df = pd.DataFrame(data)

token_symbol = df["symbol"]
print(token_symbol)