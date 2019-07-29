# scopus.py


from pybliometrics.scopus import ScopusSearch
import pandas as pd
from pytictoc import TicToc

t = TicToc()

t.tic()
s = ScopusSearch('FIRSTAUTH(thiede s.) AND PUBYEAR AFT 2008 AND AUTHKEY(energ*)', refresh = True)

t.toc('Query took ')

t.tic()

pd.set_option('display.max_columns', None)

df = pd.DataFrame(s.results)

t.toc('Creating DataFrame took ')

print(df.head())
