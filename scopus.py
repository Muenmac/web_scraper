# scopus.py


from pybliometrics.scopus import ScopusSearch
import pandas as pd
from pytictoc import TicToc

# Initialize TicToc for performance measures
t = TicToc()


def execute_search(name):
    """Execute a search on Scopus using Scopus Query Language and print brief results"""
    t.tic()
    s = ScopusSearch('TITLE-ABS ( energ*  OR  power  OR  load )  AND  '
                     'TITLE-ABS ( predict*  OR  forecast*  OR  prognos*  OR  model*  OR  consumption  OR  efficiency ) '
                     'AND  TITLE-ABS ( manufactur*  OR  production )  AND  PUBYEAR  >  2000  AND  SUBJAREA ( engi )  '
                     'OR  SUBJAREA ( ener )  AND  KEY ( energ* )  AND  ( KEY ( predic* )  OR  KEY ( forecast* )  '
                     'OR  KEY ( prognos* ) )  AND NOT  KEY ( solar* )  AND NOT  KEY ( wind* )  '
                     'AND NOT  KEY ( photovoltaic* )  AND NOT  KEY ( bio* )  AND NOT  KEY ( *hydro* )  '
                     'AND NOT  KEY ( *gas* )')

    query_results = pd.DataFrame(s.results)
    # print(query_results.shape())

    # Select name for pickle data
    # name = 'query_results_LCE2020_test'
    query_results.to_pickle('./Scopus_dumps' + name + '.pkl')
    t.toc('Query and Saving DataFrame took ')
