import whois
from datetime import datetime, timezone
import math
import pandas as pd
import numpy as np
from pyquery import PyQuery
from requests import get

csv_path = 'static/dataset/dataseturl.csv'

# Load into DataFrame
df_raw = pd.read_csv(csv_path, header=None, usecols=[0])
df_raw.drop([0], inplace=True)

# Random Sampling
rnd_state = np.random.randint(1000)
df = df_raw.sample(n=100, random_state=rnd_state,ignore_index=True)
df.head()

# Extract Columns & Create Blank DataFrame (Feature Extraction)
cols = UrlFeatureExtract("").run().keys()
df_feat = pd.DataFrame(columns = cols)

# Extract Features
t = []

df_flat = df.to_numpy().flatten()
for i in df_flat:
  temp = UrlFeatureExtract(i).run()
  t.append(temp)

    
df_feat=df_feat.append(t)
df_feat = df_feat.join(df[0])
df_feat.rename(columns={0:'urls'}, inplace=True)
dat=df_feat.head()

print(dat)
