
import pandas as pd

dataframe = pd.read_json("static/walletchain.json", orient='values')
#print(dataframe)

for ss in dataframe.values:
    print(ss[1])

