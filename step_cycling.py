# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:32:42 2021

@author: MarcinDolata
"""

import tkinter as tk
from tkinter import filedialog
import time
import re
import os
import functions
import pandas as pd
import numpy as np
#import datetime
#from datetime import date, datetime
#import openpyxl as xl
#import xlsxwriter
#import matplotlib
#import matplotlib.pyplot as plt
#import numpy as np
from pathlib import Path

#%%

#datafolder = r'C:\Users\MarcinDolata\Documents\analysis_cycling\B2DOE\step2'

root= tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
datafolder=filedialog.askdirectory()

startTime = time.time()   #timing script 

print(f'Analizing files in: {datafolder}')

file_path = [os.path.join(root, name) #filter 'STEP' raw files
             for root, dirs, files in os.walk(datafolder)
             for name in files
             if name.endswith((".csv")) and 'step' in name.lower() and 't45' in name.lower() ]

file_path = sorted(file_path)

#%% Cycling Capacity
cell = 'B2DOE-0'
nHeader = 0
capa_sep = []
capa_ord = []
cellIDs = []
cy = []
cy_beg = []
for idx, file in enumerate(file_path):
    try:
        parsed_file_name = cellID = re.search(cell + '(.+)', re.search('Slim'+'(.+)', file).group()).group().split()
        cellID = parsed_file_name[1]
        cy_new = parsed_file_name[len(parsed_file_name) - 2]
        if 'cy' in cy_new.lower():
            cy_new = cy_new[2:]
        cy_beg_new = cy_new.split('-')[0]
    except:
        cellID = 'XX'
    
    cellIDs.append(parsed_file_name[1])
    cy.append(cy_new)
    cy_beg.append(cy_beg_new)
# RPT check - if RPT in

    if 'rpt' in file.lower(): RPT = True
    else: RPT = False

# Exception - interrupted test - RPT in file name but not done
    if '200-239' in file.lower(): RPT = False
# End of exception

    # print('RPT: ',RPT)
    data, capa_ord_idx = functions.load_data(file,nHeader,RPT)
    capa_sep_idx = pd.pivot_table(capa_ord_idx, values='Capacity(Ah)', index=["Total Cycle"], columns=["Type"])
    capa_sep_idx['File'] = cy_new
    capa_ord.append([pd.DataFrame([cellID]),capa_ord_idx])
    capa_sep.append([pd.DataFrame([cellID]),capa_sep_idx])
    
# capa_sep_all = pd.DataFrame(columns=[
#                             capa_sep[0][1].index.name,
#                             capa_sep[0][1].columns.values[0],
#                             capa_sep[0][1].columns.values[1],
#                             ])

capa_sep_all = capa_sep[0][1]
for file_idx in range (1,len(capa_sep)):
    capa_sep_all = capa_sep_all.append(capa_sep[file_idx][1], ignore_index = True)
capa_sep_all.index = np.arange(1,len(capa_sep_all)+1)

# Replace partial SOC capacity values with zeros
for ind in capa_sep_all:
    capa_sep_all.loc[capa_sep_all.Charge < 60, "Charge"] = None
    
# Add cycle number column
capa_sep_all['Cycle'] = np.arange(1,len(capa_sep_all)+1)

ref_dch_capa = capa_sep_all['Discharge'][1]
ref_cha_capa = capa_sep_all['Charge'][2]
capa_sep_all['Cha capa ret (%)'] = capa_sep_all['Charge'] / ref_cha_capa
capa_sep_all['Dch capa ret (%)'] = capa_sep_all['Discharge'] / ref_dch_capa
capa_sep_all['Efficiency'] = capa_sep_all['Discharge'] / capa_sep_all['Charge']
capa_sep_all = capa_sep_all.reindex(columns = ['File', 'Cycle', 'Charge', 'Cha capa ret (%)', 'Discharge', 'Dch capa ret (%)', 'Efficiency'])
#%% Save to excel

Path(datafolder + '/Output_step/').mkdir(exist_ok=True) # create folder in datafolder
file_name               = datafolder + '/Output_step/output_sheet_'+cellID+'.xlsx'

 
writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
workbook = writer.book


# # Capacity sheet 
# Sheetnm = 'Summary in correct order'
# worksheet = workbook.add_worksheet(Sheetnm)
# writer.sheets[Sheetnm] = worksheet

# for idx1 in range(len(capa_ord)):
#     capa_ord[idx1][1].to_excel(writer,sheet_name=Sheetnm, startrow=0, startcol=0)

# Sheetnm = 'Charge vs Discharge'
# worksheet = workbook.add_worksheet(Sheetnm)
# writer.sheets[Sheetnm] = worksheet

# for idx1 in range(len(capa_ord)):
#     capa_sep[idx1][1].to_excel(writer,sheet_name=Sheetnm, startrow=0, startcol=0)

Sheetnm = 'Charge vs Discharge all'
worksheet = workbook.add_worksheet(Sheetnm)
writer.sheets[Sheetnm] = worksheet

capa_sep_all.to_excel(writer,sheet_name=Sheetnm, startrow=0, startcol=0)

writer.save()


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))



