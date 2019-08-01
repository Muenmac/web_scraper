# read_csv


import pandas as pd


link = "/home/marc/PycharmProjects/web scraper/scopus.csv"
csv = pd.read_csv(link)
df = pd.DataFrame(csv)


df.reindex(['Authors', 'Title', 'Year', 'Abstract', 'DOI', 'Link', 'Author Keywords', 'Index Keywords', 'References'])



