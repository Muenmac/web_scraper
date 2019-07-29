# scopus.py


from pybliometrics.scopus import ScopusSearch
import pandas as pd
import TikTok


s = ScopusSearch('TITLE-ABS ( energ*  OR  power )  AND  TITLE-ABS ( predict*  OR  forecast*  OR  prognos*  OR  model*'
                 '  OR  consumption  OR  efficiency )  AND  TITLE-ABS ( manufactur*  OR  production )  '
                 'AND  PUBYEAR  >  2008  AND  ( SUBJAREA ( engi )  OR  SUBJAREA ( ener ) )  AND NOT  KEY ( solar )  '
                 'AND NOT  KEY ( wind )  AND NOT  KEY ( photovoltaic )', refresh = False)


# pd.set_option('display.max_columns', None)
df = pd.DataFrame(s.results)

print(df.head(5))
# print(df.loc[:, ['eid', 'doi', 'title', 'subtype', 'affilname', 'authkeywords']])








