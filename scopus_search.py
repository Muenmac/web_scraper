# scopus_search.py


from pybliometrics.scopus import ScopusSearch
import pandas as pd
from pytictoc import TicToc

# Initialize TicToc for performance measures
t = TicToc()
query = ('TITLE-ABS ( energ*  OR  power  OR  load )  AND  '
                     'TITLE-ABS ( predict*  OR  forecast*  OR  prognos*  OR  model*  OR  consumption  OR  efficiency ) '
                     'AND  TITLE-ABS ( manufactur*  OR  production )  AND  PUBYEAR  >  2000  AND  SUBJAREA ( engi )  '
                     'OR  SUBJAREA ( ener )  AND  KEY ( energ* )  AND  ( KEY ( predic* )  OR  KEY ( forecast* )  '
                     'OR  KEY ( prognos* ) )  AND NOT  KEY ( solar* )  AND NOT  KEY ( wind* )  '
                     'AND NOT  KEY ( photovoltaic* )  AND NOT  KEY ( bio* )  AND NOT  KEY ( *hydro* )  '
                     'AND NOT  KEY ( *gas* )')

def execute_search(dump_name, query):
    """Execute a search on Scopus using Scopus Query Language and print brief results"""
    t.tic()
    res = ScopusSearch(query)

    query_res = pd.DataFrame(res.results)

    # Select name for pickle data
    query_res.to_pickle('./Scopus_dumps/' + dump_name + '.pkl')
    t.toc('Query and saving DataFrame took ')


def load_pickle(res_pickle):
    """Reload pickled data and manipulate search results, res_pickle = Name of pickle data in Scopus_dumps folder"""
    results = pd.read_pickle('./Scopus_dumps/'+res_pickle)
    # print(results.head(), results.info())

