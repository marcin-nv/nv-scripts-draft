# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:50:14 2021

@author: MarcinDolata
"""


import pandas as pd

def load_data(fileName, nHeaderLines, RPT_check):
    
    data = pd.read_csv(fileName, skiprows=nHeaderLines)
    table = pd.pivot_table(data, values=['Capacity(Ah)'], index=['Type', 'Total Cycle']).drop('Rest')
    table = table.sort_values(['Total Cycle', 'Type'], ascending=[True, True])
    if RPT_check == True:
        table = table.iloc[:-5]
    
    return (data, table)