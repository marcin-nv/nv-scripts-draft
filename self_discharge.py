# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:12:59 2021

@author: MarcinDolata
"""

import time
import os
from scipy import interpolate
import pandas as pd
import numpy as np

startTime = time.time()

nHeader = 2

cell = ['80-81', '82-83', '84-85', '86-87', '90-91', '92-93', '235-236', '259-260', '300-301', '94-95', '96-97', '98-99']
temp = [40, 40, 40, 40, 40, 40, 40, 40, 40, 25, 25, 25]

#_____________________________________________________________________________
# OCV to SOC function definition (based on)

def get_SOC_from_OCV(ocv_search,OCV_DCH,OCV_CHA,mode):
    
    SOC = [100, 95 ,90 ,80,70,60 ,50 ,40 ,30 ,20 ,10 , 5, 0]
    
    if mode == 0:
        OCV_Mean = np.mean([OCV_DCH,OCV_CHA], axis=0 )
        interpolation_OCV = interpolate.interp1d (OCV_Mean,SOC, kind = 'linear',fill_value='extrapolate')
#        OCV_Mean= np.insert(OCV_Mean,0, 4.195)
        pass
    elif mode == 1:
        interpolation_OCV = interpolate.interp1d (OCV_DCH,SOC, kind = 'linear',fill_value='extrapolate')
    elif mode == 2:
        interpolation_OCV = interpolate.interp1d (OCV_CHA,SOC, kind = 'linear',fill_value='extrapolate')

    return interpolation_OCV(ocv_search)

#_____________________________________________________________________________
# read raw data

datafolder = r'C:\Users\MarcinDolata\Documents'

file_path = [os.path.join(root, name) #filter the raw files in a list
             for root, dirs, files in os.walk(datafolder)
             for name in files
             if name.endswith((".xlsx")) and 'book' in name.lower()]

file_path = sorted(file_path)

OCV_data = pd.read_excel(file_path[0], skiprows=nHeader)
days = OCV_data['diff'].tolist()
del OCV_data['diff'], OCV_data['day']

#_____________________________________________________________________________
# compute SOC from OCV data

for ind in range(len(cell)):
    if temp[ind] == 40:
        OCV_DCH = [4.175, 4.111,4.084,3.992,3.902,3.815,3.699,3.632,3.583,3.505,3.392,3.350,3.216]
        OCV_CHA = [4.172,4.115,4.089,3.999,3.909,3.824,3.705,3.641,3.592,3.529,3.408,3.362,3.206]
    elif temp[ind] == 25:
        OCV_DCH = [4.176, 4.110,4.083,3.991,3.900,3.814,3.695,3.628,3.580,3.504,3.392,3.351,3.217]
        OCV_CHA = [4.172,4.114,4.089,4.000,3.909,3.824,3.703,3.638,3.591,3.531,3.410,3.363,3.209]
    else:
        print('Provide OCV vs SOC characteristics data for temp = ' + temp[ind])
        
    SOC_results = get_SOC_from_OCV(OCV_data[cell],OCV_DCH,OCV_CHA,1)
    SOC_results = pd.DataFrame(np.array(SOC_results), columns=cell)
    
table = pd.concat([OCV_data,SOC_results], axis=1)
#OCV_data.set_index()
#table.columns = ['OCV', 'OCV', 'OCV', 'OCV', 'OCV', 
#                 'OCV', 'OCV', 'OCV', 'OCV', 'OCV',
#                 'OCV', 'OCV', 'OCV', 'OCV', 'OCV',
#                 'OCV', 'OCV', 'OCV', 'OCV', 'OCV',
#                 'OCV', 'OCV', 'OCV', 'OCV']

#_____________________________________________________________________________
# save results in excel sheet

now                     = datetime.now()
dt_string               = now.strftime("%Y%m%d_%H%M%S")
Path(datafolder + '/Output/').mkdir(exist_ok=True) # create folder in datafolder
file_name               = datafolder + '/Output/'+dt_string + '.xlsx'

    
writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
workbook=writer.book
# # Comparison sheet 
Sheetnm = ' Separated Cycling'
worksheet=workbook.add_worksheet(Sheetnm)
writer.sheets[Sheetnm] = worksheet
for idx1 in range(len(rated_capa_results)):
    Cha_cycles = rated_capa_results[idx1][1].loc[rated_capa_results[idx1][1]['C-rate'] == 0.33]
    Dch_cycles = rated_capa_results[idx1][1].loc[rated_capa_results[idx1][1]['C-rate'] == -0.33]
    row       = 1+ (Cha_cycles.shape[0]+2)* idx1 #pyxl counts starts counting at 1,1 xlsxwriter at 0,0
    col       = 1
    Cha_cycles.to_excel(writer,sheet_name=Sheetnm, startrow=row , startcol=col, index_label = rated_capa_results[idx1][0])
    
    row       = 1+ (Dch_cycles.shape[0]+2)* idx1 #pyxl counts starts counting at 1,1 xlsxwriter at 0,0
    col       = 4 + Cha_cycles.shape[1]
    Dch_cycles.to_excel(writer,sheet_name=Sheetnm, startrow=row , startcol=col, index_label = rated_capa_results[idx1][0])

   


writer.save()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))






























