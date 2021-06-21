# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:12:59 2021

@author: MarcinDolata
"""

import time
import os
from scipy import interpolate
#to call interp1d
#from scipy.interpolate import interp1d
#if abo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

startTime = time.time()

cell = ['80-81', '82-83', '84-85', '86-87', '90-91', '92-93', '235-236', '259-260', '300-301', '94-95', '96-97', '98-99']
temp = [40, 40, 40, 40, 40, 40, 40, 40, 40, 25, 25, 25]

#_____________________________________________________________________________
# OCV to SOC function definition (based on Simon's function)

def get_SOC_from_OCV(ocv_search,ind,mode):
    print(OCV_data[cell[ind]])
    SOC = [100, 95, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 0]
    if temp[ind] == 40:
        OCV_DCH = [4.175,4.111,4.084,3.992,3.902,3.815,3.699,3.632,3.583,3.505,3.392,3.350,3.216]
        OCV_CHA = [4.172,4.115,4.089,3.999,3.909,3.824,3.705,3.641,3.592,3.529,3.408,3.362,3.206]
    elif temp[ind] == 25:
        OCV_DCH = [4.176,4.110,4.083,3.991,3.900,3.814,3.695,3.628,3.580,3.504,3.392,3.351,3.217]
        OCV_CHA = [4.172,4.114,4.089,4.000,3.909,3.824,3.703,3.638,3.591,3.531,3.410,3.363,3.209]
    else:
        print('Provide OCV vs SOC characteristics data for temp = ' + str(temp[ind]))
        
    if mode == 0:
        OCV_Mean = np.mean([OCV_DCH,OCV_CHA], axis=0 )
        interpolation_OCV = interpolate.interp1d (OCV_Mean,SOC)
#        OCV_Mean= np.insert(OCV_Mean,0, 4.195)
    elif mode == 1:
        interpolation_OCV = interpolate.interp1d (OCV_DCH,SOC)
    elif mode == 2:
        interpolation_OCV = interpolate.interp1d (OCV_CHA,SOC)
        
    return interpolation_OCV(ocv_search)

#_____________________________________________________________________________
# read raw data

datafolder = r'C:\Users\MarcinDolata\Documents'

file_path = [os.path.join(root, name) #filter the raw files in a list
             for root, dirs, files in os.walk(datafolder)
             for name in files
             if name.endswith((".xlsx")) and 'proposal' in name.lower()]

file_path = sorted(file_path)
OCV_data = pd.read_excel(file_path[0], sheet_name=0, skiprows=3) #horizontal layout (original proposal)
# OCV_data = pd.read_excel(file_path[0], sheet_name=1, skiprows=0) #verlical layout (reviewed by Camille)

#_____________________________________________________________________________
# create dataframe for results

SOC_results = pd.DataFrame()
#SOC_results = pd.DataFrame(columns = [cell, ['OCV']*len(cell)])
SOC_results['date'] = OCV_data['date']
SOC_results['day'] = OCV_data['day']

#del OCV_data['date'], OCV_data['day']

#_____________________________________________________________________________
# compute SOC from OCV data

for ind in range(len(cell)):

    SOC_results[cell[ind]] = get_SOC_from_OCV(OCV_data[cell[ind]],ind,1)


#_____________________________________________________________________________
# plots in 'Plots' pane

colors = ['darkgreen', 'mediumseagreen', 'mediumaquamarine']

fig, axs = plt.subplots(2, 2)

col = 0
for cell in ['80-81', '82-83', '84-85']:
    axs[0, 0].plot(SOC_results['day'], SOC_results[cell], color=colors[col], marker='o', linewidth=1, markersize=2, label=cell)
    col += 1
axs[0, 0].set_title('40oC, 80% SOC', y=1.0, pad=-10, fontsize = 8)

col = 0
for cell in ['86-87', '90-91', '92-93']:
    axs[0, 1].plot(SOC_results['day'], SOC_results[cell], color=colors[col], marker='o', linewidth=1, markersize=2, label=cell)
    col += 1
axs[0, 1].set_title('40oC, 50% SOC', y=1.0, pad=-10, fontsize = 8)

col = 0
for cell in ['235-236', '259-260', '300-301']:
    axs[1, 0].plot(SOC_results['day'], SOC_results[cell], color=colors[col], marker='o', linewidth=1, markersize=2, label=cell)
    col += 1
axs[1, 0].set_title('40oC, 29% SOC', y=1.0, pad=-10, fontsize = 8)

col = 0
for cell in ['94-95', '96-97', '98-99']:
    axs[1, 1].plot(SOC_results['day'], SOC_results[cell], color=colors[col], marker='o', linewidth=1, markersize=2, label=cell)
    col += 1
axs[1, 1].set_title('25oC, 80% SOC', y=1.0, pad=-10, fontsize = 8)

#plt.plot(days, SOC_results[cell[3:6]], marker='o')
# plt.plot(days, SOC_results[cell[0:3]], marker='o')
# plt.show()

fig.tight_layout()

for ax in axs.flat:
    ax.set_xlabel('time (days)', fontsize=6)
    ax.set_ylabel('SOC (%)', fontsize=6)
    ax.tick_params(axis="x", labelsize=6)
    ax.tick_params(axis="y", labelsize=6)
    

#_____________________________________________________________________________
# save results in excel sheet


file_name               = datafolder + '/SOC_results_self-discharge_draft.xlsx'

    
writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
workbook=writer.book

Sheetnm = 'SOC_results'
worksheet=workbook.add_worksheet(Sheetnm)
writer.sheets[Sheetnm] = worksheet

SOC_results.to_excel(writer,sheet_name=Sheetnm, startrow=0 , startcol=0,
#                     index_label = rated_capa_results[idx1][0]
                     )

writer.save()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))






























