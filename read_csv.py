# read_csv


import pandas as pd


link = "/home/marc/PycharmProjects/web scraper/scopus.csv"
csv = pd.read_csv(link)
df = pd.DataFrame(csv)

df.reindex(['Authors', 'Title', 'Year', 'Abstract', 'DOI', 'Link', 'Author Keywords', 'Index Keywords', 'References'])
df2 = df.rename(columns={"Title": "tittel"})

print(df2.columns, df2.shape, df2.info, df2.count)
