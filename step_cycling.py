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
#import numpy as np
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
             if name.endswith((".csv")) and 'step' in name.lower() ]

file_path = sorted(file_path)

#%% Cycling Capacity
cell = 'B2DOE-5'
nHeader = 0
capa_sep = []
capa_ord = []

for idx, file in enumerate(file_path):
    try:
        cellID = re.search(cell + ' (.+)', file).group(1).split()[1]
    except:
        cellID = 'XX'
        
    data, capa_ord_idx = functions.load_data(file,nHeader)
    capa_sep_idx = pd.pivot_table(capa_ord_idx, values='Capacity(Ah)', index=["Total Cycle"], columns=["Type"])
    capa_ord.append([pd.DataFrame([cellID]),capa_ord_idx])
    capa_sep.append([pd.DataFrame([cellID]),capa_sep_idx])
    
#%% Save to excel

Path(datafolder + '/Output_step/').mkdir(exist_ok=True) # create folder in datafolder
file_name               = datafolder + '/Output_step/output_sheet.xlsx'

 
writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
workbook = writer.book


# # Capacity sheet 
Sheetnm = 'Summary in correct order'
worksheet = workbook.add_worksheet(Sheetnm)
writer.sheets[Sheetnm] = worksheet

for idx1 in range(len(capa_ord)):
    capa_ord[idx1][1].to_excel(writer,sheet_name=Sheetnm, startrow=0, startcol=0)

Sheetnm = 'Charge vs Discharge'
worksheet = workbook.add_worksheet(Sheetnm)
writer.sheets[Sheetnm] = worksheet

for idx1 in range(len(capa_ord)):
    print('Marker1: ',idx1)
    capa_sep[idx1][1].to_excel(writer,sheet_name=Sheetnm, startrow=0, startcol=0)

writer.save()


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))



