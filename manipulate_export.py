# manipulate export.py


import pandas as pd
import numpy as np

try:
    res_np = np.load('/home/marc/PycharmProjects/web scraper/Scopus_dumps/query_results_LCE2020.pkl', allow_pickle=True)
    res_pd = pd.read_pickle('/home/marc/PycharmProjects/web scraper/Scopus_dumps/query_results_LCE2020.pkl')
except:
    print("Reading data failed")


res_np.head()






