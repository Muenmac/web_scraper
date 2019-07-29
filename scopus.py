# scopus.py


from pybliometrics.scopus import ScopusSearch
import pandas as pd


s = ScopusSearch('FIRSTAUTH(thiede, s.)', refresh = True)


pd.set_option('display.max_columns', None)
df = pd.DataFrame(s.results)

print(df.loc[:, ['eid', 'doi', 'title', 'subtype', 'affilname', 'authkeywords']])








