# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:57:38 2021

@author: SimonHeid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:46:28 2020

@author: simonheid
"""

import time
import re
import os
import getDataPNE as PNE
import pandas as pd
import numpy as np
import datetime
from datetime import date, datetime
#import openpyxl as xl
import xlsxwriter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

startTime = time.time()   #timing script 

V_COL='Voltage(V)'
I_COL='Current(A)'
Q_COL='Capacity(Ah)'
E_COL='wattHour(Wh)'
P_COL='Power(W)'
DATETIME_COL='TotTime(H:M:S)'
TIME_H_COL='Time(h)'
STEP_NO_COL='StepNo'
STEP_TYPE_COL='Type'
CYCLE_NO_COL='TotCycle'
DATA_CODE_COL='Code'
POWER_COL='Power(W)'
STEPTIME_COL = 'StepTime(H:M:S)'
CODE_COL = 'Code'
Diff_step = 'Steptime_DIFF'
nHeader = 0

# #  ===============================================================================


datafolder = r'C:\Users\MarcinDolata\Documents\Davids cycling'

#datafolder= r'C:/Users/MarioBecker/northvolt.com/Validation - Documents/07_Customer Validation/05. Porsche/03. Raw Data/02. B2DOE/B2DOE 6/01. Cycling/01. CSL/B2DOE-6 241-242'

# datafolder= r'/Users/simonheid/OneDrive - northvolt.com/Master/02 Standards/09 Data Analysis/00 Data/202010 -10 degC Rated Capa'

file_path = [os.path.join(root, name) #filter the raw files in a list
             for root, dirs, files in os.walk(datafolder)
             for name in files
             if name.endswith((".csv")) and 'summary' not in name.lower() and 'step' not in name.lower() ]


file_path = sorted(file_path)

file_path_summary = [os.path.join(root, name) #filter the raw files in a list
             for root, dirs, files in os.walk(datafolder)
             for name in files
             if name.endswith((".csv")) and 'summary' in name.lower() ]              

file_path_summary = sorted(file_path_summary)

# =============================================================================
# Cycling Capacity
# =============================================================================

rated_capa_results =[]
single_file =[]
list_datapoints =[]
v0_allCells =[]
list_df_dcir=[]
list_datapoints =[]


for idx, file in enumerate(file_path):
    
    data, table = PNE.postproc_data(file,nHeader)
    # PNE.plotVIT(data)   # to plot the raw data
    # fix - find a better way to insert input parameters
    Ah = 113
    C_rate_cycling = 0.05
    
    idx_Ah = table[abs(table[('Current(A)','max')]).between(0.95*(C_rate_cycling*Ah),1.05*(C_rate_cycling*Ah))].index

    try:
        # fix - why are we introducing cell design name here? can't we extract it 
        cellID = re.search('B1S2 (.+)', file).group(1).split()[0]
    except:
        cellID = 'XX'
        # fix - print warning that desired cell name was not found in file name
        print('Warning:\ncellID = \'XX\'\nProvided cellID not found in the file:\n\t' + file + '.\n\n')
        
    
#%% =============================================================================
# Rated Capacity Calculation
# ===============================================================================

    C_rate_sum  =[]
    E_sum=[]
    Q_sum           =[]
    V_step_start    =[]
    V_step_end      =[]
    Duration_sum    =[]
    Temp_start0     =[]
    Temp_start1     =[]
    Temp_start2     =[]
    Temp_heatup0    =[]
    Temp_heatup1    =[]
    Temp_heatup2    =[]
    E_rateC =[]
    t_rateC = []
    V_rateC = []
    I_rateC = []
    Q_rateC = []
    Qend_rateC  = []
    Eend_rateC =[]
    T_rateC = []
    V0_rateC = []
    V0 = pd.DataFrame()
    Vend_rateC =[]
    V_start_cc      = []
    V_end_cc        = []
    V_start_cv      = []
    V_end_cv        = []
    T_avg_cha       =[]
    T_avg_dch       =[]
    Q_cc_max        =[]
    Q_cv_max        =[]
    Q_cha    =[]
    Q_dch   =[]
    I_cc_avg        =[]
    I_cc_end    =[]
    I_cv_start  =[]
    I_cv_end    =[]
    E_cc_max        =[]
    E_cv_max        =[]
    E_dch       =[]
    


        
    for i in np.arange(idx_Ah.size): #create array with size of idx_I to go through idx_I

        #%% =============================================================================
        # IF clauses to find the correct Discharge Pulses to analyse 
        # ===============================================================================
        conditions = [(data[CYCLE_NO_COL] == idx_Ah[i][0])
                        & (data[STEP_NO_COL] == idx_Ah[i][1])]
        
        #%% =============================================================================
        # Filter the whole raw data to the one step which shall be analyzed and filter the most relevant values out (time, Voltage, Current, Ah, Wh,T)
        # ===============================================================================
        time_step = np.array(data[TIME_H_COL][np.where(conditions)[1]].reset_index(drop=True)).T*3600
        time_step = np.round(time_step - time_step[0],1)
        V_step = np.round(data[V_COL][np.where(conditions)[1]].reset_index(drop=True),4)
        I_step = data[I_COL][np.where(conditions)[1]].reset_index(drop=True)
        Q_step  = data[Q_COL][np.where(conditions)[1]].reset_index(drop=True)
        TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
        T_step = [ data[col][np.where(conditions)[1]].reset_index(drop=True).values for col in TEMP_COLS]
        E_step = data[E_COL][np.where(conditions)[1]].reset_index(drop=True)
        
        # if min(T_step [0]) < 40:    # to check if cycling is happening at the right temperature, optional
        #     continue
        
        #%% =============================================================================
        # CC - CV distinction
        # ===============================================================================
        
        cc_I_avg = np.mean (I_step[1:1000]) #determine cc charge current
        if np.average(I_step) > 0:
            bool_CC = I_step.between(cc_I_avg*0.995,cc_I_avg*1.005)
        else:
            bool_CC = I_step.between(cc_I_avg*1.005,cc_I_avg*0.995)
        bool_CC [0] = True # first value is the ramp up and normally not at the cc 
        bool_CV = np.invert(bool_CC)
        
        I_cc = I_step[np.where(bool_CC)[0]].reset_index(drop=True)
        I_cv = I_step[np.where(bool_CV)[0]].reset_index(drop=True)
        Q_cc = Q_step[np.where(bool_CC)[0]].reset_index(drop=True)
        Q_cv = Q_step[np.where(bool_CV)[0]].reset_index(drop=True)
        E_cc = E_step[np.where(bool_CC)[0]].reset_index(drop=True)
        E_cv = E_step[np.where(bool_CV)[0]].reset_index(drop=True)
        V_cc = V_step[np.where(bool_CC)[0]].reset_index(drop=True)
        V_cv = V_step[np.where(bool_CV)[0]].reset_index(drop=True)
        
        
        V_start_cc.append(V_cc[0])
        V_end_cc.append(V_cc[-1:].values)
        if V_cv.empty:
            V_start_cv.append(0)
            V_end_cv.append(0)
            Q_cv_max.append(0)
            I_cv_start.append(0)
            E_cv_max.append(0)
            I_cv_end.append(0)
        else:
            V_start_cv.append(V_cv[0])
            V_end_cv.append(V_cv[-1:].values)
            Q_cv_max.append(np.max(Q_cv) - np.max(Q_cc))
            I_cv_start.append(I_cv [0])
            E_cv_max.append(np.max(E_cv) - np.max(E_cc))
            I_cv_end.append(I_cv [-1:].values[0])
        
        T_avg_cha.append(np.mean(T_step[2]))
        Q_cc_max.append(np.max(Q_cc))   
        I_cc_avg.append(cc_I_avg)
        I_cc_end.append(I_cc [-1:].values[0])


        E_cc_max.append(np.max(E_cc))
        
        #%% =============================================================================
        # Summary results
        # ===============================================================================
        V0 = V_step[np.where(time_step==0)[0][0]]
        V0_rateC.append(V0)
        Vend_rateC.append( V_step[np.where(time_step==time_step.max())[0][0]])
        C_rate_sum.append(round(cc_I_avg/Ah,2))
        E_sum.append(max(E_step))
        Q_sum.append(max(Q_step))
        V_step_start.append(V_step[np.where(time_step==0)[0][0]])
        V_step_end.append(V_step[np.where(time_step==time_step.max())[0][0]])
        Duration_sum.append(time_step.max())

        Temp_start0.append(T_step[0][0])
        Temp_heatup0.append(T_step[0][-1]-T_step[0][0])
        Temp_start1.append(T_step[1][0])
        Temp_heatup1.append(T_step[1][-1]-T_step[1][0])
        Temp_start2.append(T_step[2][0])
        Temp_heatup2.append(T_step[2][-1]-T_step[2][0])
            
    df = pd.DataFrame({'C-rate': C_rate_sum,'Ah':Q_sum,'Wh':E_sum,'V Start':V_step_start,'V End':V_step_end,'Duration':Duration_sum,'Start T A':Temp_start0, 'Delta T A':Temp_heatup0,
                       'Start T Cat':Temp_start1, 'Delta T Cat':Temp_heatup1, 'Start T L':Temp_start2, 'Max T L':Temp_heatup2})
        
    
    # df2 = pd.DataFrame({'C-rate': C_rate_sum, 'V':V_rateC,'Ah':Q_rateC,'Wh': E_rateC})
    df_cc_cv = pd.DataFrame({'Cap CC':Q_cc_max,'Ah CV':Q_cv_max, 'Wh CC':E_cc_max,'Wh CV':E_cv_max, 'Avg A CC':I_cc_avg,'A CCend':I_cc_end,'A CVStart': I_cv_start,'A CVEnd ':I_cv_end})
    df1 = pd.concat ([df, df_cc_cv],axis=1)
    rated_capa_results.append([cellID,df1])
# list_datapoints.append([cellID,df2])
    
    
# =============================================================================
# Summarize only relevant data for RPT comparison
# =============================================================================

# add summarized data in special sheet in Excel
# =============================================================================
# Write into excel file    
# =============================================================================


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
    Cha_cycles = rated_capa_results[idx1][1].loc[rated_capa_results[idx1][1]['C-rate'] == 0.2]
    Dch_cycles = rated_capa_results[idx1][1].loc[rated_capa_results[idx1][1]['C-rate'] == -0.33]
    row       = 1+ (Cha_cycles.shape[0]+2)* idx1 #pyxl counts starts counting at 1,1 xlsxwriter at 0,0
    col       = 1
    Cha_cycles.to_excel(writer,sheet_name=Sheetnm, startrow=row , startcol=col, index_label = rated_capa_results[idx1][0])
    
    row       = 1+ (Dch_cycles.shape[0]+2)* idx1 #pyxl counts starts counting at 1,1 xlsxwriter at 0,0
    col       = 4 + Cha_cycles.shape[1]
    Dch_cycles.to_excel(writer,sheet_name=Sheetnm, startrow=row , startcol=col, index_label = rated_capa_results[idx1][0])


# # Capacity sheet 
Sheetnm = 'Summary in correct order'
worksheet=workbook.add_worksheet(Sheetnm)
writer.sheets[Sheetnm] = worksheet
for idx1 in range(len(rated_capa_results)):
    row       = 1+ (rated_capa_results[idx1][1].shape[0]+2)* idx1 #pyxl counts starts counting at 1,1 xlsxwriter at 0,0
    col       = 1
    rated_capa_results[idx1][1].to_excel(writer,sheet_name=Sheetnm, startrow=row , startcol=col, index_label = rated_capa_results[idx1][0])
    

writer.save()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))




