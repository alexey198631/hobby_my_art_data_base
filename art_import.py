"""
['START', 'DATE', 'DAYS', 'TYPE', 'AWARD', 'LANG', 'TIMES', 'NAME',
       'YEAR', 'FACT_DURATION', 'ACTIVITY', 'DURATION', 'CREATOR', 'WHERE',
       'COUNTRY', 'PTS', 'COMMENTS']
"""

import pandas as pd

art = pd.read_excel('data_files/Days.xlsx', sheet_name='art')
art_test = art.dropna(subset='DATE')