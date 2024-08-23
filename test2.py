import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt
import seaborn as sns

import os
urldata = pd.read_csv("static/dataset/urldata.csv")
urldata.head()
#Removing the unnamed columns as it is not necesary.
#urldata = urldata.drop('Unnamed: 0',axis=1)
urldata.head()

urldata.shape
urldata.isnull().sum()
from urllib.parse import urlparse
import os.path
#Length of URL
urldata['url_length'] = urldata['url'].apply(lambda i: len(str(i)))
#Hostname Length
urldata['hostname_length'] = urldata['url'].apply(lambda i: len(urlparse(i).netloc))
#Path Length
urldata['path_length'] = urldata['url'].apply(lambda i: len(urlparse(i).path))
#First Directory Length
def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

urldata['fd_length'] = urldata['url'].apply(lambda i: fd_length(i))
dat=urldata.head(10)
print(dat)
