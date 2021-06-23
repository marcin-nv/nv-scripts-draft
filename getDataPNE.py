# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Oct 25 2019, 10:52:18) 
# [Clang 4.0.1 (tags/RELEASE_401/final)]
# Embedded file name: /Users/simonheid/Documents/GitHub/validation-test-scripts/lib/getDataPNE.py
# Compiled at: 2020-06-25 09:47:38
# Size of source mod 2**32: 29028 bytes
"""
Created on Tue Oct  8 11:29:41 2019

@author: Manik Mayur
"""
import pandas as pd, matplotlib as mpl, numpy as np
from scipy import interpolate
import re
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Category20
from bokeh.layouts import gridplot, row
from bokeh.models import Legend, Label
from bokeh.io import export_png
import matplotlib.pyplot as plt

V_COL = 'Voltage(V)'
I_COL = 'Current(A)'
Q_COL = 'Capacity(Ah)'
E_COL = 'wattHour(Wh)'
DATETIME_COL = 'TotTime(H:M:S)'
TIME_H_COL = 'Time(h)'
STEP_NO_COL = 'StepNo'
STEP_TYPE_COL = 'Type'
CYCLE_NO_COL = 'TotCycle'
DATA_CODE_COL = 'Code'
POWER_COL = 'Power(W)'
STEPTIME_COL = 'StepTime(H:M:S)'
CODE_COL = 'Code'
Diff_step = 'Steptime_DIFF'

def date_parser(text):
    pattern = re.compile('(?:(\\d+)m)?\\s?(?:(\\d+)d)?\\s?(\\d+):(\\d+):(\\d+)\\.?(\\d+)?')
    match = list(pattern.search(text).groups())
    time = int(0 if match[0] == None else match[0]) * 30 * 24 + int(0 if match[1] == None else match[1]) * 24 + int(0 if match[2] == None else match[2]) + int(0 if match[3] == None else match[3]) / 60 + int(0 if match[4] == None else match[4]) / 3600 + int(0 if match[5] == None else match[5]) / 360000
    return time

def SOC_Determination_PPESlim_B1(ocv_search,mode):
    # Update with Excel readin for BMW data will come
    
    OCV_DCH = [4.176, 4.110,4.083,3.991,3.900,3.814,3.695,3.628,3.580,3.504,3.392,3.351,3.217]

    OCV_CHA = [4.172,4.114,4.089,4.000,3.909,3.824,3.703,3.638,3.591,3.531,3.410,3.363,3.209]
    SOC = [100, 95 ,90 ,80,70,60 ,50 ,40 ,30 ,20 ,10 , 5, 0]
    
    if mode == 0:
        OCV_Mean = np.mean([OCV_DCH,OCV_CHA], axis=0 )
        interpolation_OCV = interpolate.interp1d (OCV_Mean,SOC, kind = 'linear',fill_value='extrapolate')
        plt.scatter(OCV_Mean,SOC)
        OCV_Mean= np.insert(OCV_Mean,0, 4.195)
        plt.plot(OCV_Mean,interpolation_OCV(OCV_Mean),':')
    elif mode == 1:
        interpolation_OCV = interpolate.interp1d (OCV_DCH,SOC, kind = 'linear',fill_value='extrapolate')
    elif mode == 2:
        interpolation_OCV = interpolate.interp1d (OCV_CHA,SOC, kind = 'linear',fill_value='extrapolate')

    return interpolation_OCV(ocv_search)

def OCV_Determination_PPESlim_B1(soc,mode):
    # Update with Excel readin for BMW data will come
    
    OCV_DCH = [4.176, 4.110,4.083,3.991,3.900,3.814,3.695,3.628,3.580,3.504,3.392,3.351,3.217]

    OCV_CHA = [4.172,4.114,4.089,4.000,3.909,3.824,3.703,3.638,3.591,3.531,3.410,3.363,3.209]
    SOC = [100, 95 ,90 ,80,70,60 ,50 ,40 ,30 ,20 ,10 , 5, 0]
    
    if mode == 0:
        OCV_Mean = np.mean([OCV_DCH,OCV_CHA], axis=0 )
        interpolation_OCV = interpolate.interp1d (SOC,OCV_Mean, kind = 'linear',fill_value='extrapolate')
        plt.scatter(OCV_Mean,SOC)
        OCV_Mean= np.insert(OCV_Mean,0, 4.195)
        plt.plot(OCV_Mean,interpolation_OCV(OCV_Mean),':')
    elif mode == 1:
        interpolation_OCV = interpolate.interp1d (SOC,OCV_DCH, kind = 'linear',fill_value='extrapolate')
    elif mode == 2:
        interpolation_OCV = interpolate.interp1d (SOC,OCV_CHA, kind = 'linear',fill_value='extrapolate')

    return interpolation_OCV(soc)


def SOC_Determination_PPESlim_B1_T40(ocv_search,mode):
    # Update with Excel readin for BMW data will come
    
    OCV_DCH = [4.175, 4.111,4.084,3.992,3.902,3.815,3.699,3.632,3.583,3.505,3.392,3.350,3.216]

    OCV_CHA = [4.172,4.115,4.089,3.999,3.909,3.824,3.705,3.641,3.592,3.529,3.408,3.362,3.206]
    SOC = [100, 95 ,90 ,80,70,60 ,50 ,40 ,30 ,20 ,10 , 5, 0]
    
    if mode == 0:
        OCV_Mean = np.mean([OCV_DCH,OCV_CHA], axis=0 )
        interpolation_OCV = interpolate.interp1d (OCV_Mean,SOC, kind = 'linear',fill_value='extrapolate')
        plt.scatter(OCV_Mean,SOC)
        OCV_Mean= np.insert(OCV_Mean,0, 4.195)
        plt.plot(OCV_Mean,interpolation_OCV(OCV_Mean),':')
    elif mode == 1:
        interpolation_OCV = interpolate.interp1d (OCV_DCH,SOC, kind = 'linear',fill_value='extrapolate')
    elif mode == 2:
        interpolation_OCV = interpolate.interp1d (OCV_CHA,SOC, kind = 'linear',fill_value='extrapolate')

    return interpolation_OCV(ocv_search)

def OCV_Determination_PPESlim_B1_T40(soc,mode):
    # Update with Excel readin for BMW data will come
    
    OCV_DCH = [4.175, 4.111,4.084,3.992,3.902,3.815,3.699,3.632,3.583,3.505,3.392,3.350,3.216]

    OCV_CHA = [4.172,4.115,4.089,3.999,3.909,3.824,3.705,3.641,3.592,3.529,3.408,3.362,3.206]
    SOC = [100, 95 ,90 ,80,70,60 ,50 ,40 ,30 ,20 ,10 , 5, 0]
    
    if mode == 0:
        OCV_Mean = np.mean([OCV_DCH,OCV_CHA], axis=0 )
        interpolation_OCV = interpolate.interp1d (SOC,OCV_Mean, kind = 'linear',fill_value='extrapolate')
        plt.scatter(OCV_Mean,SOC)
        OCV_Mean= np.insert(OCV_Mean,0, 4.195)
        plt.plot(OCV_Mean,interpolation_OCV(OCV_Mean),':')
    elif mode == 1:
        interpolation_OCV = interpolate.interp1d (SOC,OCV_DCH, kind = 'linear',fill_value='extrapolate')
    elif mode == 2:
        interpolation_OCV = interpolate.interp1d (SOC,OCV_CHA, kind = 'linear',fill_value='extrapolate')

    return interpolation_OCV(soc)




def NV_Color():
    greys = ['#4a4a49', '#6e6e6d', '#9b9b9b', '#c4c5c5', '#e2e2e2']
    greens = ['#007844', '#48A26B', '#8CD8A8', '#67b785', '#8cd8a8']
    blues = ['#005FAD', '#4E98D2', '#80C6EC' ]
    black = '#000000'
    yellow = '#ffdd00'
    orange = '#f7a600'
    darkorange = '#ef7c00'
    color_palet = [black, blues[0], greens[0], blues[1], greens[1], blues[2], greens[2], yellow, orange, darkorange, greys[0], greys[1], greys[2], greys[3]]
    return color_palet

#=============================================================================
# Basic Configuration of plots
#==============================================================================
def set_PlotConfig(p):
#Configuration of the plot title, ticks, legendm etc.
    #Title
    
    p.title.text_font_size = '20pt'
    #Legend
    p.legend.title = 'Legend'
    p.legend.location = "top_right"
    p.legend.title_text_font_style = "bold"
    p.legend.click_policy="hide"
    
    #Axis X
    p.xaxis[0].ticker.desired_num_ticks = 15
    p.xaxis.major_tick_line_width = 3
    p.xaxis.axis_label_text_font_size = "10pt"
    p.xaxis.major_label_text_font_size = "11pt"

    #Axis Y
    p.ygrid.minor_grid_line_color = 'grey'
    p.ygrid.minor_grid_line_alpha = 0.2
    p.yaxis[0].ticker.desired_num_ticks = 10    
    p.yaxis.major_tick_line_width = 3
    p.yaxis.axis_label_text_font_size = "12pt"
    p.yaxis.major_label_text_font_size = "12pt"
    
    #Axis ticks
    p.axis.major_tick_out = 10
    p.axis.minor_tick_in = -3
    p.axis.minor_tick_out = 8
    
    return p


def dataIntegrity_Test(data, fileName_summary, nHeaderLines):
    table2 = pd.pivot_table(data, values=[V_COL, I_COL], index=[
     CYCLE_NO_COL, STEP_NO_COL, STEP_TYPE_COL, DATA_CODE_COL],
      aggfunc=max)
    table2 = table2.sort_values(['TotCycle', 'StepNo'], ascending=[True, True])
    data_summary = pd.read_csv(fileName_summary, skiprows=nHeaderLines)
    data_summary_filtered = data_summary[['Current(A)', 'Voltage(V)', 'Total Cycle', 'Step', 'Type', 'Code']]
    table2 = table2[(table2.index.to_frame().iloc[:, 3] != 'Normal')]
    table3 = pd.concat([table2, table2.index.to_frame()], axis=1).reset_index(drop=True)
    data_summary_filtered.columns = table3.columns
    if data_summary_filtered.equals(table3):
        print('Data integrity Test for Summary and Raw data PASSED')
        result = None
    else:
        print('Warning: Data integrity Test for Summary and Raw data FAILED')
        result = pd.concat([data_summary_filtered, table3]).drop_duplicates(keep=False)
    return result


def SameFlow_Check(table0, table1):
    table0_INDEX = table0.index.to_frame().reset_index(drop=True)
    table1_INDEX = table1.index.to_frame().reset_index(drop=True)
    if table1_INDEX.equals(table0_INDEX):
        print('Flow check Passed')
        result = None
    else:
        print('Warning: Flow check Failed')
        result = pd.concat([table0_INDEX, table1_INDEX]).drop_duplicates(keep=False)
    return result


def postproc_data_Power(fileName, nHeaderLines):
    data = pd.read_csv(fileName, skiprows=nHeaderLines)
    data[TIME_H_COL] = [date_parser(dat) for dat in data[DATETIME_COL]]
    TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
    data[STEPTIME_COL] = [date_parser(dat) * 3600 for dat in data[STEPTIME_COL]]
    data['Steptime_DIFF'] = abs(np.diff((data[STEPTIME_COL]), append=0))
    table = pd.pivot_table(data, values=[V_COL, I_COL, TIME_H_COL, Q_COL, Diff_step, POWER_COL, TEMP_COLS[2]], index=[
     CYCLE_NO_COL, STEP_NO_COL, STEP_TYPE_COL, DATA_CODE_COL],
      aggfunc={TIME_H_COL: [min, max], V_COL: [min, max], I_COL: [min, max], Q_COL: [min, max], Diff_step: [min, max], POWER_COL: [min, np.mean, max], TEMP_COLS[2]: [min, np.mean, max]})
    table = table.sort_values(['TotCycle', 'StepNo', ('Time(h)', 'min')], ascending=[True, True, True])
    return (
     data, table)


def date_parser_2(text):
    # split the text by spaces (\s) and (:)
    split_text = re.split("\s|:", text)
    
    if split_text[0] == "":
        days = 0
    else:
        # look for numbers in the days part of the text
        days = re.findall(r"[0-9]+", split_text[0])[0]

    # convert to hours
    days = int(days) * 24
    hours = int(split_text[1])
    minutes = int(split_text[2]) / 60
    seconds = float(split_text[3]) / 3600

    time = days + hours + minutes + seconds

    return time


def postproc_data(fileName, nHeaderLines):
    data = pd.read_csv(fileName, skiprows=nHeaderLines)
    if "Total Time(H:M:S)" in data:
        time_name = "Total Time(H:M:S)"
        # date_format = r"(?:(\d+)m)?\s?(?:(\d+)d)?\s?(\d+):(\d+):(\d+)\.?(\d+)?"
    elif "TotTime(H:M:S)" in data:
        time_name = "TotTime(H:M:S)"
        # date_format = r"(?:(\d+)m)?\s?(?:(\d+)d)?\s?(\d+):(\d+):(\d+)\.?(\d+)?"
    else:
        raise KeyError("Time key not found...")
        
    if STEPTIME_COL in data:
        steptime_name = STEPTIME_COL
        # date_format = r"(?:(\d+)m)?\s?(?:(\d+)d)?\s?(\d+):(\d+):(\d+)\.?(\d+)?"
    elif "Step Time(H:M:S)" in data:
        steptime_name = "Step Time(H:M:S)"
        # date_format = r"(?:(\d+)m)?\s?(?:(\d+)d)?\s?(\d+):(\d+):(\d+)\.?(\d+)?"
    else:
        raise KeyError("Time key not found...")





    data[TIME_H_COL] = [date_parser_2(dat) for dat in data[time_name]]
    #data[TIME_H_COL] = [date_parser(dat) for dat in data[DATETIME_COL]]
    TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
    data['Step Time [s]'] = [date_parser(dat) * 3600 for dat in data[steptime_name]]
    data['Steptime_DIFF'] = abs(np.diff((data['Step Time [s]']), append=0))
    table = pd.pivot_table(data, values=[V_COL, I_COL, TIME_H_COL, Q_COL, Diff_step, TEMP_COLS[2]], index=[
     CYCLE_NO_COL, STEP_NO_COL, STEP_TYPE_COL, DATA_CODE_COL],
      aggfunc={TIME_H_COL: [min, max], V_COL: [min, max], I_COL: [min, max], Q_COL: [min, max], Diff_step: [min, max], TEMP_COLS[2]: [min, np.mean, max]})
    table = table.sort_values(['TotCycle', 'StepNo', ('Time(h)', 'min')], ascending=[True, True, True])
    return (
     data, table)


def postproc_data_Swelling(fileName, nHeaderLines):
    data = pd.read_csv(fileName, skiprows=nHeaderLines)
    data[TIME_H_COL] = [date_parser(dat) for dat in data[DATETIME_COL]]
    TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
    data[STEPTIME_COL] = [date_parser(dat) * 3600 for dat in data[STEPTIME_COL]]
    data['Steptime_DIFF'] = abs(np.diff((data[STEPTIME_COL]), append=0))
    table = pd.pivot_table(data, values=[V_COL, I_COL, TIME_H_COL, Q_COL, Diff_step, TEMP_COLS[2], 'Pressure1', 'Thickness'], index=[
     CYCLE_NO_COL, STEP_NO_COL, STEP_TYPE_COL, DATA_CODE_COL],
      aggfunc={TIME_H_COL: [min, max], V_COL: [min, max], I_COL: [min, np.mean, max], Q_COL: [min, max], Diff_step: [min, max], TEMP_COLS[2]: [min, np.mean, max], 'Pressure1': [min, max], 'Thickness': [min, max]})
    table = table.sort_values(['TotCycle', 'StepNo', ('Time(h)', 'min')], ascending=[True, True, True])
    return (
     data, table)

def get_DCIR_varI_RPT(data, table, timing):

    idx_I = table[table[('Steptime_DIFF', 'max')].between(max(timing)*0.8, max(timing)+0.1)].index
    dt_DCIR = timing
    dcir_data = pd.DataFrame()
    TEMP_COLS           = [col for col in data.columns if 'AuxTemperature' in col]
    T_global           = [data[col].reset_index(drop=True).values for col in TEMP_COLS]

    for i in np.arange(idx_I.size):
        conditions = [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                      & (data[STEP_NO_COL] == idx_I[i][1]) 
                      & (data[STEP_TYPE_COL] == idx_I[i][2])]
        time = np.array(data[TIME_H_COL][np.where(conditions)[1]].reset_index(drop=True)).T * 3600
        time = np.round(time - time[0], 1)
        sampling = round(np.average(np.diff(time)), 1)
        T_M = pd.DataFrame()
        T_C = pd.DataFrame()
        T_A = pd.DataFrame()
        if not time.max() > max(timing):
            if sampling > 1:
                continue
            else:
                V           = data[V_COL][np.where(conditions)[1]].reset_index(drop=True)
                I           = data[I_COL][np.where(conditions)[1]].reset_index(drop=True)
                Q           = data[Q_COL][np.where(conditions)[1]].reset_index(drop=True)
                P           = data[POWER_COL][np.where(conditions)[1]].reset_index(drop=True)
                TEMP_COLS   = [col for col in data.columns if 'AuxTemperature' in col]
                T           = [data[col][np.where(conditions)[1]].reset_index(drop=True).values for col in TEMP_COLS]

                V0          = V[np.where(time == 0)[0][0]]
                
                V_str   = pd.DataFrame(['V' +str(t) for t in dt_DCIR[(dt_DCIR <= time.max())]])
                try:
                    Vt      = pd.DataFrame([V[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                except:
                    test = 0
                I_str   = pd.DataFrame(['Current' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                It      = pd.DataFrame([I[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                dcir_str= pd.DataFrame(['DC-IR' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                dcir    = pd.DataFrame([((V[np.where(time == t)[0][0]] - V0) * 1000 / I[np.where(time == t)[0][0]]) for t in dt_DCIR[np.logical_and(dt_DCIR <= time.max(),dt_DCIR >0)]])
                dcir    = pd.concat([pd.DataFrame([0]),dcir], axis=0).reset_index(drop=True)
                P_str   = pd.DataFrame(['Power' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Pt      = pd.DataFrame([P[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Q_str   = pd.DataFrame(['Capacity' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Qt      = pd.DataFrame([Q[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_A_str = pd.DataFrame(['Temp Anode' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_A     = pd.DataFrame([T[0][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_C_str = pd.DataFrame(['Temp Cathode' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_C     = pd.DataFrame([T[1][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_M_str = pd.DataFrame(['Temp Middle' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_M     = pd.DataFrame([T[2][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                
                # ---------------------------------------
                # Calculate voltage and temperature 1h and 5min before DCIR
                # ---------------------------------------
                t_xminbeforePulse = 0.5
                t_30minbeforePulse = (np.array(data[TIME_H_COL][np.where(conditions)[1]])[0]-t_xminbeforePulse)
                conditions_time_30minbeforDCIR     = [data[TIME_H_COL].between(t_30minbeforePulse-1/60/60,t_30minbeforePulse+1/60/60)]
                V_1h_beforeDCIR                 =  np.mean(pd.DataFrame(data[V_COL][np.where(conditions_time_30minbeforDCIR )[1]]))
                T_A_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[0][np.where(conditions_time_30minbeforDCIR )[1]]))
                T_C_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[1][np.where(conditions_time_30minbeforDCIR )[1]]))
                T_M_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[2][np.where(conditions_time_30minbeforDCIR )[1]]))
                I_1h_beforeDCIR                 =  np.mean(pd.DataFrame(data[I_COL][np.where(conditions_time_30minbeforDCIR )[1]]))
    
    
                t_10minbeforePulse                   = (np.array(data[TIME_H_COL][np.where(conditions)[1]])[0]-10/60)
                conditions_time_10minbeforDCIR       = [data[TIME_H_COL].between(t_10minbeforePulse-1/60/60,t_10minbeforePulse+1/60/60)]
                V_5min_beforeDCIR                   =  np.mean( pd.DataFrame(data[V_COL][np.where(conditions_time_10minbeforDCIR)[1]]))
                I_5min_beforeDCIR                   = np.mean( pd.DataFrame(data[I_COL][np.where(conditions_time_10minbeforDCIR)[1]]))
                
                
                V_str_break     = pd.DataFrame (['V-'+str(t_xminbeforePulse*3600), 'V-600'])
                V_str           = pd.concat ([V_str_break, V_str]).reset_index(drop = True)
                Vt              = pd.concat ([V_1h_beforeDCIR,V_5min_beforeDCIR, Vt]).reset_index(drop = True)
                Filler          = pd.DataFrame([np.nan]).transpose()
                Filler          = pd.concat ([Filler, Filler]).reset_index(drop = True)
                I_str           = pd.concat ([pd.DataFrame(['Current','Current']), I_str]).reset_index(drop = True)
                It              = pd.concat ([I_1h_beforeDCIR,I_5min_beforeDCIR, It]).reset_index(drop = True)
                dcir_str        = pd.concat ([Filler, dcir_str]).reset_index(drop = True)
                dcir            = pd.concat ([Filler, dcir]).reset_index(drop = True)
                P_str           = pd.concat ([Filler, P_str]).reset_index(drop = True)
                Pt              = pd.concat ([Filler, Pt]).reset_index(drop = True)
                Q_str           = pd.concat ([Filler, Q_str]).reset_index(drop = True)
                Qt              = pd.concat ([Filler, Qt]).reset_index(drop = True)
                T_A_str         = pd.concat ([pd.DataFrame(['Temp Anode','Temp Anode']), T_A_str]).reset_index(drop = True)
                T_A             = pd.concat ([T_A_1h_beforeDCIR,pd.DataFrame([0]), T_A]).reset_index(drop = True)
                T_C_str         = pd.concat ([pd.DataFrame(['Temp Cathode','Temp Cathode']), T_C_str]).reset_index(drop = True)
                T_C             = pd.concat ([T_C_1h_beforeDCIR,pd.DataFrame([0]), T_C]).reset_index(drop = True)
                T_M_str         = pd.concat ([pd.DataFrame(['Temp Middle','Temp Middle']), T_M_str]).reset_index(drop = True)
                T_M             = pd.concat ([T_M_1h_beforeDCIR,pd.DataFrame([0]), T_M]).reset_index(drop = True)
                    
                
                # ---------------------------------------
                # Calculate DCIR with continuous DCIR method
                # ---------------------------------------
                
                conditions_time_breakafterDCIR                 =  [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                                                            & (data[STEP_NO_COL] == (idx_I[i][1])+1)]                # select rest after dcir pulse
                time_rest_afterDCIR                         =  np.array(data[TIME_H_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)).T * 3600
                time_rest_afterDCIR                         =  np.round(time_rest_afterDCIR  -time_rest_afterDCIR [0], 1)
                V_rest_afterDCIR                            =  data[V_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)
                I_rest_afterDCIR                            =  data[I_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)
                
                T_A_afterDCIR                               =  T_global[0][np.where(conditions_time_breakafterDCIR )[1]]
                T_C_afterDCIR                               =  T_global[1][np.where(conditions_time_breakafterDCIR )[1]]
                T_M_afterDCIR                               =  T_global[2][np.where(conditions_time_breakafterDCIR )[1]]
                
                time_resttime_afterDCIR                     =   max(time_rest_afterDCIR)
                time_beforeENDofRest_afterDCIR              =  time_resttime_afterDCIR - (1*60)
                
                if time_beforeENDofRest_afterDCIR < 0:
                    time_beforeENDofRest_afterDCIR          = time_resttime_afterDCIR - 0.5*(1*60)
                    if time_beforeENDofRest_afterDCIR < 0:
                        time_beforeENDofRest_afterDCIR          = time_resttime_afterDCIR - 0.25*(1*60)
    
                V_10min_beforeENDofRest_afterDCIR           =  pd.DataFrame([V_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                I_10min_beforeENDofRest_afterDCIR           =  pd.DataFrame([I_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                I_endofRest_afterDCIR                       =  pd.DataFrame([I_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_resttime_afterDCIR)[0][0]]])
                T_A_EndRest_afterDCIR                       =  pd.DataFrame([T_A_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                T_C_EndRest_afterDCIR                       =  pd.DataFrame([T_C_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                T_M_EndRest_afterDCIR                       =  pd.DataFrame([T_M_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                V_EndRest_afterDCIR                         =  V_rest_afterDCIR[-1:]
                T_A_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_A_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR  )[0][0]]])
                T_C_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_C_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                T_M_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_M_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                
                dcir_cont = (Vt.iloc[-1].values[0] - V_EndRest_afterDCIR )*1000 /  It.iloc[-1].values[0] 
                
                
                V_str_break_after   = pd.DataFrame (['V+' +str(time_beforeENDofRest_afterDCIR), 'V+' + str(time_resttime_afterDCIR)])
                V_str               = pd.concat ([V_str,V_str_break_after]).reset_index(drop = True)
                Vt                  = pd.concat ([Vt,V_10min_beforeENDofRest_afterDCIR  , V_EndRest_afterDCIR]).reset_index(drop = True)
                Filler_1x           = pd.DataFrame([np.nan]).transpose()
                Filler              = pd.concat ([Filler_1x, Filler_1x]).reset_index(drop = True)
                I_str               = pd.concat ([I_str,pd.DataFrame(['Current','Current']) ]).reset_index(drop = True)
                It                  = pd.concat ([It,I_10min_beforeENDofRest_afterDCIR , I_endofRest_afterDCIR]).reset_index(drop = True)
                dcir_str            = pd.concat ([dcir_str, pd.DataFrame(['DCIR','DCIR V2'])]).reset_index(drop = True)
                dcir                = pd.concat ([dcir, Filler_1x, dcir_cont]).reset_index(drop = True)
                P_str               = pd.concat ([P_str, Filler ]).reset_index(drop = True)
                Pt                  = pd.concat ([Pt, Filler]).reset_index(drop = True)
                Q_str               = pd.concat ([Q_str, Filler]).reset_index(drop = True)
                Qt                  = pd.concat ([ Qt,Filler]).reset_index(drop = True)
                T_A_str             = pd.concat ([T_A_str, pd.DataFrame(['Temp Anode','Temp Anode'])]).reset_index(drop = True)
                T_A                 = pd.concat ([ T_A,T_A_10min_beforeENDofRest_afterDCIR,T_A_EndRest_afterDCIR ]).reset_index(drop = True)
                T_C_str             = pd.concat ([ T_C_str, pd.DataFrame(['Temp Cathode', 'Temp Cathode'])]).reset_index(drop = True)
                T_C                 = pd.concat ([T_C,T_C_10min_beforeENDofRest_afterDCIR,T_C_EndRest_afterDCIR ]).reset_index(drop = True)
                T_M_str             = pd.concat ([ T_M_str, pd.DataFrame(['Temp Middle', 'Temp Middle'])]).reset_index(drop = True)
                T_M                 = pd.concat ([T_M,T_M_10min_beforeENDofRest_afterDCIR,T_M_EndRest_afterDCIR]).reset_index(drop = True)
                
                
                # Divider_str =  pd.DataFrame(['-------' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                # dcir_pulse = pd.concat([V_str, Vt, I_str, It , dcir_str, round(dcir,3), P_str, Pt, T_A_str, T_A, T_C_str, T_C, T_M_str, T_M,Divider_str], axis= 1).transpose()
                dcir_pulse = pd.concat([V_str, Vt, I_str, It , dcir_str, round(dcir,3), P_str, Pt, Q_str, Qt, T_A_str, T_A, T_C_str, T_C, T_M_str, T_M], axis= 1).transpose()
                # V0_DCIR.append(V0)
                dcir_data = pd.concat([dcir_data, dcir_pulse], axis=0)

    return dcir_data.reset_index(drop=True)

def get_DCIR_varI(data, table, timing):

    idx_I = table[table[('Steptime_DIFF', 'max')].between(max(timing)*0.8, max(timing)+0.1)].index
    dt_DCIR = timing
    dcir_data = pd.DataFrame()
    TEMP_COLS           = [col for col in data.columns if 'AuxTemperature' in col]
    T_global           = [data[col].reset_index(drop=True).values for col in TEMP_COLS]

    for i in np.arange(idx_I.size):
        conditions = [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                      & (data[STEP_NO_COL] == idx_I[i][1]) 
                      & (data[STEP_TYPE_COL] == idx_I[i][2])]
        time = np.array(data[TIME_H_COL][np.where(conditions)[1]].reset_index(drop=True)).T * 3600
        time = np.round(time - time[0], 1)
        sampling = round(np.average(np.diff(time)), 1)
        T_M = pd.DataFrame()
        T_C = pd.DataFrame()
        T_A = pd.DataFrame()
        if not time.max() > max(timing):
            if sampling > 1:
                continue
            else:
                V           = data[V_COL][np.where(conditions)[1]].reset_index(drop=True)
                I           = data[I_COL][np.where(conditions)[1]].reset_index(drop=True)
                Q           = data[Q_COL][np.where(conditions)[1]].reset_index(drop=True)
                P           = data[POWER_COL][np.where(conditions)[1]].reset_index(drop=True)
                TEMP_COLS   = [col for col in data.columns if 'AuxTemperature' in col]
                T           = [data[col][np.where(conditions)[1]].reset_index(drop=True).values for col in TEMP_COLS]

                V0          = V[np.where(time == 0)[0][0]]
                
                V_str   = pd.DataFrame(['V' +str(t) for t in dt_DCIR[(dt_DCIR <= time.max())]])
                try:
                    Vt      = pd.DataFrame([V[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                except:
                    test = 0
                I_str   = pd.DataFrame(['Current' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                It      = pd.DataFrame([I[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                dcir_str= pd.DataFrame(['DC-IR' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                dcir    = pd.DataFrame([((V[np.where(time == t)[0][0]] - V0) * 1000 / I[np.where(time == t)[0][0]]) for t in dt_DCIR[np.logical_and(dt_DCIR <= time.max(),dt_DCIR >0)]])
                dcir    = pd.concat([pd.DataFrame([0]),dcir], axis=0).reset_index(drop=True)
                P_str   = pd.DataFrame(['Power' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Pt      = pd.DataFrame([P[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Q_str   = pd.DataFrame(['Capacity' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Qt      = pd.DataFrame([Q[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_A_str = pd.DataFrame(['Temp Anode' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_A     = pd.DataFrame([T[0][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_C_str = pd.DataFrame(['Temp Cathode' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_C     = pd.DataFrame([T[1][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_M_str = pd.DataFrame(['Temp Middle' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_M     = pd.DataFrame([T[2][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                
                # ---------------------------------------
                # Calculate voltage and temperature 1h and 5min before DCIR
                # ---------------------------------------
                t_1hbeforePulse = (np.array(data[TIME_H_COL][np.where(conditions)[1]])[0]-1)
                conditions_time_1hbeforDCIR     = [data[TIME_H_COL].between(t_1hbeforePulse-1/60/60,t_1hbeforePulse+1/60/60)]
                V_1h_beforeDCIR                 =  np.mean(pd.DataFrame(data[V_COL][np.where(conditions_time_1hbeforDCIR)[1]]))
                T_A_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[0][np.where(conditions_time_1hbeforDCIR)[1]]))
                T_C_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[1][np.where(conditions_time_1hbeforDCIR)[1]]))
                T_M_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[2][np.where(conditions_time_1hbeforDCIR)[1]]))
                I_1h_beforeDCIR                 =  np.mean(pd.DataFrame(data[I_COL][np.where(conditions_time_1hbeforDCIR)[1]]))
    
                t_5minbeforePulse                   = (np.array(data[TIME_H_COL][np.where(conditions)[1]])[0]-10/60)
                conditions_time_5minbeforDCIR       = [data[TIME_H_COL].between(t_5minbeforePulse-1/60/60,t_5minbeforePulse+1/60/60)]
                V_5min_beforeDCIR                   =  np.mean( pd.DataFrame(data[V_COL][np.where(conditions_time_5minbeforDCIR)[1]]))
                I_5min_beforeDCIR                   = np.mean( pd.DataFrame(data[I_COL][np.where(conditions_time_5minbeforDCIR)[1]]))
                
                
                V_str_break     = pd.DataFrame (['V-3600', 'V-600'])
                V_str           = pd.concat ([V_str_break, V_str]).reset_index(drop = True)
                Vt              = pd.concat ([V_1h_beforeDCIR,V_5min_beforeDCIR, Vt]).reset_index(drop = True)
                Filler          = pd.DataFrame([0]).transpose()
                Filler          = pd.concat ([Filler, Filler]).reset_index(drop = True)
                I_str           = pd.concat ([Filler, I_str]).reset_index(drop = True)
                It              = pd.concat ([I_1h_beforeDCIR,I_5min_beforeDCIR, It]).reset_index(drop = True)
                dcir_str        = pd.concat ([Filler, dcir_str]).reset_index(drop = True)
                dcir            = pd.concat ([Filler, dcir]).reset_index(drop = True)
                P_str           = pd.concat ([Filler, P_str]).reset_index(drop = True)
                Pt              = pd.concat ([Filler, Pt]).reset_index(drop = True)
                Q_str           = pd.concat ([Filler, Q_str]).reset_index(drop = True)
                Qt              = pd.concat ([Filler, Qt]).reset_index(drop = True)
                T_A_str         = pd.concat ([Filler, T_A_str]).reset_index(drop = True)
                T_A             = pd.concat ([T_A_1h_beforeDCIR,pd.DataFrame([0]), T_A]).reset_index(drop = True)
                T_C_str         = pd.concat ([Filler, T_C_str]).reset_index(drop = True)
                T_C             = pd.concat ([T_C_1h_beforeDCIR,pd.DataFrame([0]), T_C]).reset_index(drop = True)
                T_M_str         = pd.concat ([Filler, T_M_str]).reset_index(drop = True)
                T_M             = pd.concat ([T_M_1h_beforeDCIR,pd.DataFrame([0]), T_M]).reset_index(drop = True)
                    
                
                # ---------------------------------------
                # Calculate DCIR with continuous DCIR method
                # ---------------------------------------
                
                conditions_time_breakafterDCIR                 =  [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                                                            & (data[STEP_NO_COL] == (idx_I[i][1])+1)]                # select rest after dcir pulse
                time_rest_afterDCIR                         =  np.array(data[TIME_H_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)).T * 3600
                time_rest_afterDCIR                         =  np.round(time_rest_afterDCIR  -time_rest_afterDCIR [0], 1)
                V_rest_afterDCIR                            =  data[V_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)
                I_rest_afterDCIR                            =  data[I_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)
                
                T_A_afterDCIR                               =  T_global[0][np.where(conditions_time_breakafterDCIR )[1]]
                T_C_afterDCIR                               =  T_global[1][np.where(conditions_time_breakafterDCIR )[1]]
                T_M_afterDCIR                               =  T_global[2][np.where(conditions_time_breakafterDCIR )[1]]
                
                time_resttime_afterDCIR                     =   max(time_rest_afterDCIR)
                time_beforeENDofRest_afterDCIR              =  time_resttime_afterDCIR - (10*60)
                
                if time_beforeENDofRest_afterDCIR < 0:
                    time_beforeENDofRest_afterDCIR          = time_resttime_afterDCIR - 0.5*(10*60)
                    if time_beforeENDofRest_afterDCIR < 0:
                        time_beforeENDofRest_afterDCIR          = time_resttime_afterDCIR - 0.25*(10*60)
    
                V_10min_beforeENDofRest_afterDCIR           =  np.round(pd.DataFrame(  [V_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]  ]),4)
                I_10min_beforeENDofRest_afterDCIR           =  pd.DataFrame([I_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                I_endofRest_afterDCIR                       =  pd.DataFrame([I_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_resttime_afterDCIR)[0][0]]])
                T_A_EndRest_afterDCIR                       =  pd.DataFrame([T_A_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                T_C_EndRest_afterDCIR                       =  pd.DataFrame([T_C_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                T_M_EndRest_afterDCIR                       =  pd.DataFrame([T_M_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                V_EndRest_afterDCIR                         =  V_rest_afterDCIR[-1:]
                T_A_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_A_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR  )[0][0]]])
                T_C_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_C_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                T_M_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_M_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                
                dcir_cont = (Vt.iloc[-1].values[0] - V_EndRest_afterDCIR )*1000 /  It.iloc[-1].values[0] 
                
                
                V_str_break_after   = pd.DataFrame (['V+' +str(time_beforeENDofRest_afterDCIR), 'V+' + str(time_resttime_afterDCIR)])
                V_str               = pd.concat ([V_str,V_str_break_after]).reset_index(drop = True)
                Vt                  = pd.concat ([Vt,V_10min_beforeENDofRest_afterDCIR  , V_EndRest_afterDCIR]).reset_index(drop = True)
                Filler_1x           = pd.DataFrame([0]).transpose()
                Filler              = pd.concat ([Filler_1x, Filler_1x]).reset_index(drop = True)
                I_str               = pd.concat ([I_str,Filler ]).reset_index(drop = True)
                It                  = pd.concat ([It,I_10min_beforeENDofRest_afterDCIR , I_endofRest_afterDCIR]).reset_index(drop = True)
                dcir_str            = pd.concat ([dcir_str, Filler]).reset_index(drop = True)
                dcir                = pd.concat ([dcir, Filler_1x, dcir_cont]).reset_index(drop = True)
                P_str               = pd.concat ([P_str, Filler ]).reset_index(drop = True)
                Pt                  = pd.concat ([Pt, Filler]).reset_index(drop = True)
                T_A_str             = pd.concat ([T_A_str, Filler]).reset_index(drop = True)
                T_A                 = pd.concat ([ T_A,T_A_10min_beforeENDofRest_afterDCIR,T_A_EndRest_afterDCIR ]).reset_index(drop = True)
                T_C_str             = pd.concat ([Filler, T_C_str]).reset_index(drop = True)
                T_C                 = pd.concat ([T_C,T_C_10min_beforeENDofRest_afterDCIR,T_C_EndRest_afterDCIR ]).reset_index(drop = True)
                T_M_str             = pd.concat ([Filler, T_M_str]).reset_index(drop = True)
                T_M                 = pd.concat ([T_M,T_M_10min_beforeENDofRest_afterDCIR,T_M_EndRest_afterDCIR]).reset_index(drop = True)
                
                
                # Divider_str =  pd.DataFrame(['-------' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                # dcir_pulse = pd.concat([V_str, Vt, I_str, It , dcir_str, round(dcir,3), P_str, Pt, T_A_str, T_A, T_C_str, T_C, T_M_str, T_M,Divider_str], axis= 1).transpose()
                dcir_pulse = pd.concat([V_str, Vt, I_str, It , dcir_str, round(dcir,3), P_str, Pt, Q_str, Qt, T_A_str, T_A, T_C_str, T_C, T_M_str, T_M], axis= 1).transpose()
                # V0_DCIR.append(V0)
                dcir_data = pd.concat([dcir_data, dcir_pulse], axis=0)

    return dcir_data.reset_index(drop=True)

def get_contDCIR(data, table):

    idx_I = table[table[('Steptime_DIFF', 'max')]==7200].index
    dcir_data = pd.DataFrame()
    TEMP_COLS           = [col for col in data.columns if 'AuxTemperature' in col]
    T_global           = [data[col].reset_index(drop=True).values for col in TEMP_COLS]

    for i in np.arange(idx_I.size):
        conditions = [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                      & (data[STEP_NO_COL] == (idx_I[i][1]-1))]
        try:
            time = np.array(data[TIME_H_COL][np.where(conditions)[1]].reset_index(drop=True)).T * 3600
            time = np.round(time - time[0], 1)
        except:
            continue
        dt_DCIR = np.array([0, 0.2, 1, 10, 18, 30, round(max(time),1)])
        sampling = round(np.average(np.diff(time[0:100])), 1)
        T_M = pd.DataFrame()
        T_C = pd.DataFrame()
        T_A = pd.DataFrame()
        Q           = data[Q_COL][np.where(conditions)[1]].reset_index(drop=True)
        if abs(max(Q)) < 0.07*113:
            if sampling > 0.1:
                continue
            else:
                V           = data[V_COL][np.where(conditions)[1]].reset_index(drop=True)
                I           = data[I_COL][np.where(conditions)[1]].reset_index(drop=True)

                P           = data[POWER_COL][np.where(conditions)[1]].reset_index(drop=True)
                TEMP_COLS   = [col for col in data.columns if 'AuxTemperature' in col]
                T           = [data[col][np.where(conditions)[1]].reset_index(drop=True).values for col in TEMP_COLS]

                V0          = V[np.where(time == 0)[0][0]]
                
                V_str   = pd.DataFrame(['V' +str(t) for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Vt      = pd.DataFrame([round(V[np.where(time == t)[0][0]],4) for t in dt_DCIR[(dt_DCIR <= time.max())]])
                I_str   = pd.DataFrame(['Current' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                It      = pd.DataFrame([I[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                dcir_str= pd.DataFrame(['DC-IR' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                dcir    = pd.DataFrame([((V[np.where(time == t)[0][0]] - V0) * 1000 / I[np.where(time == t)[0][0]]) for t in dt_DCIR[np.logical_and(dt_DCIR <= time.max(),dt_DCIR >0)]])
                dcir    = pd.concat([pd.DataFrame([0]),dcir], axis=0).reset_index(drop=True)
                P_str   = pd.DataFrame(['Power' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                Pt      = pd.DataFrame([P[np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_A_str = pd.DataFrame(['Temp Anode' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_A     = pd.DataFrame([T[0][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_C_str = pd.DataFrame(['Temp Cathode' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_C     = pd.DataFrame([T[1][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_M_str = pd.DataFrame(['Temp Middle' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                T_M     = pd.DataFrame([T[2][np.where(time == t)[0][0]] for t in dt_DCIR[(dt_DCIR <= time.max())]])
                
                # ---------------------------------------
                # Calculate voltage and temperature 1h and 5min before DCIR
                # ---------------------------------------
                t_1hbeforePulse = (np.array(data[TIME_H_COL][np.where(conditions)[1]])[0]-1)
                conditions_time_1hbeforDCIR     = [data[TIME_H_COL].between(t_1hbeforePulse-1/60/60,t_1hbeforePulse+1/60/60)]
                V_1h_beforeDCIR                 =  np.mean(pd.DataFrame(data[V_COL][np.where(conditions_time_1hbeforDCIR)[1]]))
                T_A_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[0][np.where(conditions_time_1hbeforDCIR)[1]]))
                T_C_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[1][np.where(conditions_time_1hbeforDCIR)[1]]))
                T_M_1h_beforeDCIR               =  np.mean(pd.DataFrame(T_global[2][np.where(conditions_time_1hbeforDCIR)[1]]))
                I_1h_beforeDCIR                 =  np.mean(pd.DataFrame(data[I_COL][np.where(conditions_time_1hbeforDCIR)[1]]))
    
                t_5minbeforePulse                   = (np.array(data[TIME_H_COL][np.where(conditions)[1]])[0]-10/60)
                conditions_time_5minbeforDCIR       = [data[TIME_H_COL].between(t_5minbeforePulse-1/60/60,t_5minbeforePulse+1/60/60)]
                V_5min_beforeDCIR                   =  np.mean( pd.DataFrame(data[V_COL][np.where(conditions_time_5minbeforDCIR)[1]]))
                I_5min_beforeDCIR                   = np.mean( pd.DataFrame(data[I_COL][np.where(conditions_time_5minbeforDCIR)[1]]))
                
                
                V_str_break     = pd.DataFrame (['V-3600', 'V-600'])
                V_str           = pd.concat ([V_str_break, V_str]).reset_index(drop = True)
                Vt              = pd.concat ([V_1h_beforeDCIR,V_5min_beforeDCIR, Vt]).reset_index(drop = True)
                Filler          = pd.DataFrame([0]).transpose()
                Filler          = pd.concat ([Filler, Filler]).reset_index(drop = True)
                I_str           = pd.concat ([Filler, I_str]).reset_index(drop = True)
                It              = pd.concat ([I_1h_beforeDCIR,I_5min_beforeDCIR, It]).reset_index(drop = True)
                dcir_str        = pd.concat ([Filler, dcir_str]).reset_index(drop = True)
                dcir            = pd.concat ([Filler, dcir]).reset_index(drop = True)
                P_str           = pd.concat ([Filler, P_str]).reset_index(drop = True)
                Pt              = pd.concat ([Filler, Pt]).reset_index(drop = True)
                T_A_str         = pd.concat ([Filler, T_A_str]).reset_index(drop = True)
                T_A             = pd.concat ([T_A_1h_beforeDCIR,pd.DataFrame([0]), T_A]).reset_index(drop = True)
                T_C_str         = pd.concat ([Filler, T_C_str]).reset_index(drop = True)
                T_C             = pd.concat ([T_C_1h_beforeDCIR,pd.DataFrame([0]), T_C]).reset_index(drop = True)
                T_M_str         = pd.concat ([Filler, T_M_str]).reset_index(drop = True)
                T_M             = pd.concat ([T_M_1h_beforeDCIR,pd.DataFrame([0]), T_M]).reset_index(drop = True)
                
                # ---------------------------------------
                # Calculate DCIR with continuous DCIR method
                # ---------------------------------------
                
                

                conditions_time_breakafterDCIR                 =  [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                                                            & (data[STEP_NO_COL] == (idx_I[i][1]))
                                                            & (data[STEP_TYPE_COL] == idx_I[i][2])]
                time_rest_afterDCIR                         =  np.array(data[TIME_H_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)).T * 3600
                time_rest_afterDCIR                         =  np.round(time_rest_afterDCIR  -time_rest_afterDCIR [0], 1)
                V_rest_afterDCIR                            =  data[V_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)
                I_rest_afterDCIR                            =  data[I_COL][np.where(conditions_time_breakafterDCIR )[1]].reset_index(drop=True)
                
                T_A_afterDCIR                               =  T_global[0][np.where(conditions_time_breakafterDCIR )[1]]
                T_C_afterDCIR                               =  T_global[1][np.where(conditions_time_breakafterDCIR )[1]]
                T_M_afterDCIR                               =  T_global[2][np.where(conditions_time_breakafterDCIR )[1]]
                
                time_resttime_afterDCIR                     =   max(time_rest_afterDCIR)
                time_beforeENDofRest_afterDCIR              =  time_resttime_afterDCIR - (10*60)
    
                V_10min_beforeENDofRest_afterDCIR           =  np.round(pd.DataFrame(  [V_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]  ]),4)
                I_10min_beforeENDofRest_afterDCIR           =  pd.DataFrame([I_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                I_endofRest_afterDCIR                       =  pd.DataFrame([I_rest_afterDCIR[np.where(time_rest_afterDCIR  == time_resttime_afterDCIR)[0][0]]])
                T_A_EndRest_afterDCIR                       =  pd.DataFrame([T_A_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                T_C_EndRest_afterDCIR                       =  pd.DataFrame([T_C_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                T_M_EndRest_afterDCIR                       =  pd.DataFrame([T_M_afterDCIR   [np.where(time_rest_afterDCIR  == time_resttime_afterDCIR )[0][0]]])
                V_EndRest_afterDCIR                         =  V_rest_afterDCIR[-1:]
                T_A_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_A_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR  )[0][0]]])
                T_C_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_C_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                T_M_10min_beforeENDofRest_afterDCIR         =  pd.DataFrame([T_M_afterDCIR[np.where(time_rest_afterDCIR  == time_beforeENDofRest_afterDCIR)[0][0]]])
                
                dcir_cont = (Vt.iloc[-1].values[0] - V_EndRest_afterDCIR )*1000 /  It.iloc[-1].values[0] 
                
                
                V_str_break_after   = pd.DataFrame (['V+' +str(time_beforeENDofRest_afterDCIR), 'V+' + str(time_resttime_afterDCIR)])
                V_str               = pd.concat ([V_str,V_str_break_after]).reset_index(drop = True)
                Vt                  = pd.concat ([Vt,V_10min_beforeENDofRest_afterDCIR  , V_EndRest_afterDCIR]).reset_index(drop = True)
                Filler_1x           = pd.DataFrame([0]).transpose()
                Filler              = pd.concat ([Filler_1x, Filler_1x]).reset_index(drop = True)
                I_str               = pd.concat ([I_str,Filler ]).reset_index(drop = True)
                It                  = pd.concat ([It,I_10min_beforeENDofRest_afterDCIR , I_endofRest_afterDCIR]).reset_index(drop = True)
                dcir_str            = pd.concat ([dcir_str, Filler]).reset_index(drop = True)
                dcir                = pd.concat ([dcir, Filler_1x, dcir_cont]).reset_index(drop = True)
                P_str               = pd.concat ([P_str, Filler ]).reset_index(drop = True)
                Pt                  = pd.concat ([Pt, Filler]).reset_index(drop = True)
                T_A_str             = pd.concat ([T_A_str, Filler]).reset_index(drop = True)
                T_A                 = pd.concat ([ T_A,T_A_10min_beforeENDofRest_afterDCIR,T_A_EndRest_afterDCIR ]).reset_index(drop = True)
                T_C_str             = pd.concat ([Filler, T_C_str]).reset_index(drop = True)
                T_C                 = pd.concat ([T_C,T_C_10min_beforeENDofRest_afterDCIR,T_C_EndRest_afterDCIR ]).reset_index(drop = True)
                T_M_str             = pd.concat ([Filler, T_M_str]).reset_index(drop = True)
                T_M                 = pd.concat ([T_M,T_M_10min_beforeENDofRest_afterDCIR,T_M_EndRest_afterDCIR]).reset_index(drop = True)
                
                
                # Divider_str =  pd.DataFrame(['-------' for t in dt_DCIR[(dt_DCIR <= time.max())]])
                # dcir_pulse = pd.concat([V_str, Vt, I_str, It , dcir_str, round(dcir,3), P_str, Pt, T_A_str, T_A, T_C_str, T_C, T_M_str, T_M,Divider_str], axis= 1).transpose()
                dcir_pulse = pd.concat([V_str, round(Vt,4), I_str, It , dcir_str, round(dcir,4), P_str, Pt, T_A_str, round(T_A,1), T_C_str,round(T_C,1), T_M_str, round(T_M,1)], axis= 1).transpose()
                # V0_DCIR.append(V0)
                dcir_data = pd.concat([dcir_data, dcir_pulse], axis=0)

    return dcir_data.reset_index(drop=True)

def get_DCIR_allCells(data, table, I, timing):
    if I > 0:
        idx_I = table[table[('Current(A)', 'max')].between(I * 0.98, I * 1.02)].index
    else:
        idx_I = table[table[('Current(A)', 'max')].between(I * 1.02, I * 0.98)].index
    dt_DCIR = timing
    t_DCIR = []
    V_DCIR = []
    I_DCIR = []
    Q_DCIR = []
    T_DCIR = []
    V0_DCIR = []
    OCV_delta = []
    dcir_data = pd.DataFrame()
    V0 = pd.DataFrame()
    OCV_delta_compensation =[]
    OCV_slope = []
    for i in np.arange(idx_I.size):
        conditions = [(data[CYCLE_NO_COL] == idx_I[i][0]) 
                      & (data[STEP_NO_COL] == idx_I[i][1]) 
                      & (data[STEP_TYPE_COL] == idx_I[i][2])]
        time = np.array(data[TIME_H_COL][np.where(conditions)[1]].reset_index(drop=True)).T * 3600
        time = np.round(time - time[0], 1)
        sampling = round(np.average(np.diff(time)), 1)
        if not time.max() > 35:
            if sampling > 0.15:
                continue
            else:
                V = data[V_COL][np.where(conditions)[1]].reset_index(drop=True)
                I = data[I_COL][np.where(conditions)[1]].reset_index(drop=True)
                Q = data[Q_COL][np.where(conditions)[1]].reset_index(drop=True)
                TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
                T = [data[col][np.where(conditions)[1]].reset_index(drop=True).values for col in TEMP_COLS]
                t_DCIR.append(time)
                V_DCIR.append(np.array(V).T)
                I_DCIR.append(np.array(I).T)
                Q_DCIR.append(np.array(Q).T)
                T_DCIR.append(np.array(T).T)
                V0 = V[np.where(time == 0)[0][0]]
                dcir = [(V[np.where(time == t)[0][0]], (V[np.where(time == t)[0][0]] - V0) * 1000 / I[np.where(time == t)[0][0]]) for t in dt_DCIR[(dt_DCIR <= time.max())]]
                V0_DCIR.append(V0)
                # dcir_data = pd.concat([dcir_data, pd.DataFrame({f"{V0} V": [i[1] for i in dcir]}, index=(dt_DCIR[(dt_DCIR <= time.max())]))], axis=1)
                dcir_data = pd.concat([dcir_data, pd.DataFrame({f"{V0}": [i[1] for i in dcir]}, index=(dt_DCIR[(dt_DCIR <= time.max())]))], axis=1)

                
                # Calculation of the ocv after compensation for comparison
                index_table = table.index
                int_index_Pulse = index_table.get_indexer([idx_I[i]])[0]
                int_index_afterCompensation =int_index_Pulse +1 # needs to be adjusted so it works properly
                
                #check when the rest started
                if table.iloc[int_index_Pulse-6,:].name[2] == 'Rest' and table.iloc[int_index_Pulse-4,:].name[2] == 'Rest':
                    relax_start_index = int_index_Pulse -6
                    idx_break3= table.iloc[relax_start_index,:].name
                    
                elif table.iloc[int_index_Pulse-4,:].name[2] == 'Rest' and table.iloc[int_index_Pulse-2,:].name[2]== 'Rest':
                    relax_start_index = int_index_Pulse -4
                elif table.iloc[int_index_Pulse-2,:].name[2]== 'Rest':
                    relax_start_index = int_index_Pulse -2
                    
                    
                
                
                if relax_start_index - int_index_Pulse == -2:
                    idx_break3 = table.iloc[relax_start_index,:].name
                    conditions_break3 = [(data[CYCLE_NO_COL] == idx_break3[0]) 
                      & (data[STEP_NO_COL] == idx_break3[1]) 
                      & (data[STEP_TYPE_COL] == idx_break3[2])]
                    conditions_break2 = np.zeros((len(conditions_break3),1),dtype=bool)
                    conditions_break1 = np.zeros((len(conditions_break3),1),dtype=bool)
                elif relax_start_index - int_index_Pulse == -4:
                    idx_break2 = table.iloc[relax_start_index,:].name
                    conditions_break2 = [(data[CYCLE_NO_COL] == idx_break2[0]) 
                      & (data[STEP_NO_COL] == idx_break2[1]) 
                      & (data[STEP_TYPE_COL] == idx_break2[2])]
                    idx_break3 = table.iloc[relax_start_index+2,:].name
                    conditions_break3 = [(data[CYCLE_NO_COL] == idx_break3[0]) 
                      & (data[STEP_NO_COL] == idx_break3[1]) 
                      & (data[STEP_TYPE_COL] == idx_break3[2])]
                    conditions_break1 = np.zeros((len(conditions_break3),1),dtype=bool)
                elif relax_start_index - int_index_Pulse == -6:
                    idx_break1 = table.iloc[relax_start_index,:].name
                    conditions_break1 = [(data[CYCLE_NO_COL] == idx_break1[0]) 
                      & (data[STEP_NO_COL] == idx_break1[1]) 
                      & (data[STEP_TYPE_COL] == idx_break1[2])]
                    idx_break2 = table.iloc[relax_start_index+2,:].name
                    conditions_break2 = [(data[CYCLE_NO_COL] == idx_break2[0]) 
                      & (data[STEP_NO_COL] == idx_break2[1]) 
                      & (data[STEP_TYPE_COL] == idx_break2[2])]
                    idx_break3 = table.iloc[relax_start_index+4,:].name
                    conditions_break3 = [(data[CYCLE_NO_COL] == idx_break3[0]) 
                      & (data[STEP_NO_COL] == idx_break3[1]) 
                      & (data[STEP_TYPE_COL] == idx_break3[2])]
                    
                conditions_rel = (np.array(conditions_break3)) | (np.array(conditions_break2)) | (np.array(conditions_break1))
                
                # conditions_rel = [
                #     (data[CYCLE_NO_COL] == idx_I[i][0]) & (data[STEP_NO_COL] == idx_I[i][1] - 1) & (data[STEP_TYPE_COL] == 'Rest')]
                # time_rel = np.array(data[TIME_H_COL].iloc[np.where(conditions)[0][0].reset_index(drop=True)).T * 3600
                time_rel = np.array(data[TIME_H_COL][np.where(conditions_rel)[1]].reset_index(drop=True)).T * 3600
                time_rel = np.round(time_rel - time_rel[0], 1)
                V_rel = np.round(data[V_COL][np.where(conditions_rel)[1]].reset_index(drop=True), 4)
                t_wait_ocv = 60
                t_wait_slope = 1*60
                try:
                    OCV_delta.append(OCV_relax_Chec(V_rel, time_rel, t_wait_ocv))
                    OCV_slope.append(OCV_relax_slope_Chec(V_rel, time_rel, t_wait_slope))
                except:
                        OCV_delta.append(np.nan)
                        OCV_slope.append(np.nan)
                    
                
                ocv_aftercompensation = table.iloc[int_index_afterCompensation,11]
                OCV_delta_compensation.append(round(abs(ocv_aftercompensation-V0),4))
    
                
                #WRITE FUNCTION which finds the step in table (index) so it is only necessary to go 2 indexes down in the table for the next step
    try:
        OCV_comparison = pd.DataFrame ({"DeltaOCV before ("+str(t_wait_ocv)+"s)":OCV_delta, 
                                    "Slope of last " +str(t_wait_slope/60) + "min": OCV_slope, "Delta VO before Pulse & after Compensation": OCV_delta_compensation})
    except:
        OCV_comparison =[]
    dcir_data.index.name = 'Time (s)'
    return (dcir_data, t_DCIR, V_DCIR, I_DCIR, Q_DCIR, T_DCIR, V0_DCIR, OCV_comparison)


def OCV_relax_Chec(voltage, time, delta):
    t1 = time.max() - delta
    t2 = time.max()
    V_relax = round(np.absolute(voltage[(time == t2)].values[0] - voltage[(time == t1)].values[0]),4)
    return V_relax

def OCV_relax_slope_Chec(voltage, time, delta):
    t1 = time.max() - delta
    t2 = time.max()
    V_relax = round(np.absolute(voltage[(time == t2)].values[0] - voltage[(time == t1)].values[0]),4)
    return V_relax/(t2-t1)*60


def plotVIT(data):
    TOOLS = 'crosshair, hover,box_zoom, reset, pan, wheel_zoom, save'
    plot_width = 700
    plot_height = 500
    p1 = figure(title='', x_axis_label='time / h',
       y_axis_label='Voltage / V',
       tools=TOOLS,
       y_range=(2.5, 5),
       plot_width=plot_width,
       plot_height=plot_height)
    p2= figure(title='', x_axis_label='time / h',
      y_axis_label='Current / I',
      tools=TOOLS,
      x_range=(p1.x_range),
      y_range=(-1050, 500),
      plot_width=plot_width,
      plot_height=plot_height)
    p3 = figure(title='', x_axis_label='time / h',
      y_axis_label='Temperature / °C',
      tools=TOOLS,
      x_range=(p1.x_range),
      y_range=(-20, 60),
      plot_width=plot_width,
      plot_height=plot_height)
    
    color = 20
    width = 2
    
    n_data = 5
    
    p1.scatter((data[TIME_H_COL][0::n_data]), (data[V_COL][0::n_data]), line_color=(Category20[color][0]), line_width=width)
    p2.line((data[TIME_H_COL][0::n_data]), (data[V_COL][0::n_data]), line_color=(Category20[color][0]), line_width=width-1)
    p2.scatter((data[TIME_H_COL][0::n_data]), (data[I_COL][0::n_data]), line_color=(Category20[color][0]), line_width=width)
    # p[1].line((data[TIME_H_COL][0::n_data]), (data[I_COL][0::n_data]), line_color=(Category20[color][0]), line_width=width-1)
    TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
    p3.line((data[TIME_H_COL][0::n_data]), (data[TEMP_COLS[0]][0::n_data]), line_color=(Category20[color][0]), line_width=width, legend_label="Anode")
    p3.line((data[TIME_H_COL][0::n_data]), (data[TEMP_COLS[1]][0::n_data]), line_color=(Category20[color][1]), line_width=width, legend_label="Cathode")
    p3.line((data[TIME_H_COL][0::n_data]), (data[TEMP_COLS[2]][0::n_data]), line_color=(Category20[color][2]), line_width=width, legend_label="Lid")
    # p1 = set_PlotConfig (p1)
    # p2 = set_PlotConfig (p2)
    # p3 = set_PlotConfig (p3)
    output_file('Basic Overview.html', title='V I T')
    grid = gridplot([p1,p2,p3], ncols=2)
    show(grid)
    # gridplot(p)
    # show(row(p1,p2,p3))


def plotDCIR(DCIR_Table, timings, I, SOC):
    TOOLS = 'crosshair, hover,box_zoom, reset, pan, wheel_zoom, save'
    plot_width = 700
    plot_height = 500
    p = [figure(title=(a[0]), x_axis_label='SOC / % ', y_axis_label='DCIR / mOhm', tools=TOOLS, x_range=(0,105), y_range=(0,10), plot_width=plot_width, plot_height=plot_height) for a in DCIR_Table]
    color = 20
    width = 2
    for cell in np.arange(len(DCIR_Table)):
        a = 0
        for t in timings:
            # p[cell].line(x=(DCIR_Table[cell][2]), y=(DCIR_Table[cell][1].loc[t, :]), legend_label=(str(t) + ' s'), line_color=(Category20[color][a]), line_width=width)
            # p[cell].scatter(x=(DCIR_Table[cell][2]), y=(DCIR_Table[cell][1].loc[t, :]), size=3, color=(Category20[color][a]))
            p[cell].line(x=SOC, y=(DCIR_Table[cell][1].loc[t, :]), legend_label=(str(t) + ' s'), line_color=(Category20[color][a]), line_width=width)
            p[cell].scatter(x=SOC, y=(DCIR_Table[cell][1].loc[t, :]), size=3, color=(Category20[color][a]))
            a = a + 1

    for i in range(0, len(p)):
        p[i].title.text_font_size = '20pt'
        p[i].legend.title = 'Legend'
        p[i].legend.location = 'top_right'
        p[i].legend.title_text_font_style = 'bold'
        p[i].legend.click_policy = 'hide'
        p[i].xaxis[0].ticker.desired_num_ticks = 10
        p[i].xaxis.major_tick_line_width = 3
        p[i].xaxis.axis_label_text_font_size = '10pt'
        p[i].xaxis.major_label_text_font_size = '11pt'
        p[i].ygrid.minor_grid_line_color = 'grey'
        p[i].ygrid.minor_grid_line_alpha = 0.2
        p[i].yaxis[0].ticker.desired_num_ticks = 10
        p[i].yaxis.major_tick_line_width = 3
        p[i].yaxis.axis_label_text_font_size = '12pt'
        p[i].yaxis.major_label_text_font_size = '12pt'
        p[i].axis.major_tick_out = 10
        p[i].axis.minor_tick_in = -3
        p[i].axis.minor_tick_out = 8

    output_file(('DCIR_Results_' + str(I) + 'A.html'), title=('DCIR ' + str(I) + 'A'))
    grid = gridplot(p, ncols=2)
    show(grid)
    
    plots_folder = '/Users/simonheid/Desktop/Excel/' + 'Plots/'
    for idx, obj in enumerate(p):
        export_png(obj, filename=plots_folder + 'dcir' + str(idx) +'.png')


def plotDCIR_compare(DCIR_Table, timings, I, SOC):
    TOOLS = 'crosshair, hover,box_zoom, reset, pan, wheel_zoom, save'
    plot_width = 700
    plot_height = 500
    p = [figure(title=('R ' + str(a) + 's '), x_axis_label='SOC / %', y_axis_label='DCIR / mOhm', tools=TOOLS, x_range=(0,105), y_range=(0,4), plot_width=plot_width, plot_height=plot_height) for a in timings]
    color = 20
    width = 2
    for idx, obj in enumerate(timings):
        a = 0
        for cell in np.arange(len(DCIR_Table)):
            # p[idx].line(x=(DCIR_Table[cell][2]), y=(DCIR_Table[cell][1].loc[obj, :]), legend_label=(DCIR_Table[cell][0]), line_color=(Category20[color][a]), line_width=width)
            # p[idx].scatter(x=(DCIR_Table[cell][2]), y=(DCIR_Table[cell][1].loc[obj, :]), line_color=(Category20[color][a]), line_width=width)
            p[idx].line(x=(SOC), y=(DCIR_Table[cell][1].loc[obj, :]), legend_label=(DCIR_Table[cell][0]), line_color=(Category20[color][a]), line_width=width)
            p[idx].scatter(x=(SOC), y=(DCIR_Table[cell][1].loc[obj, :]), line_color=(Category20[color][a]), line_width=width)
            a = a + 1

    for i in range(0, len(p)):
        p[i].title.text_font_size = '20pt'
        p[i].legend.title = 'Legend'
        p[i].legend.location = 'top_right'
        p[i].legend.title_text_font_style = 'bold'
        p[i].legend.click_policy = 'hide'
        p[i].xaxis[0].ticker.desired_num_ticks = 10
        p[i].xaxis.major_tick_line_width = 3
        p[i].xaxis.axis_label_text_font_size = '10pt'
        p[i].xaxis.major_label_text_font_size = '11pt'
        p[i].ygrid.minor_grid_line_color = 'grey'
        p[i].ygrid.minor_grid_line_alpha = 0.2
        p[i].yaxis[0].ticker.desired_num_ticks = 10
        p[i].yaxis.major_tick_line_width = 3
        p[i].yaxis.axis_label_text_font_size = '12pt'
        p[i].yaxis.major_label_text_font_size = '12pt'
        p[i].axis.major_tick_out = 10
        p[i].axis.minor_tick_in = -3
        p[i].axis.minor_tick_out = 8

    output_file(('DCIR_Results_' + str(I) + 'A.html'), title=('DCIR ' + str(I) + 'A'))
    grid = gridplot(p, ncols=2)
    show(grid)
    
    plots_folder = '/Users/simonheid/Desktop/Excel/' + 'Plots/'
    for idx, obj in enumerate(p):
        export_png(obj, filename=plots_folder + 'dcir_Compare' + str(idx) +'.png')


def set_filter(data, cycle_no, step_no, avgPts=1, interp=[False, 0, 0, 0]):
    conditions = [
     (data[CYCLE_NO_COL] == cycle_no) & (data[STEP_NO_COL] == step_no)]
    V = data[V_COL][np.where(conditions)[1]].rolling(window=avgPts, min_periods=0, center=True).mean().reset_index(drop=True)
    Q = data[C_COL][np.where(conditions)[1]].reset_index(drop=True)
    dVdQ = pd.Series(0).append((pd.Series(np.diff(V) / np.diff(Q))), ignore_index=True)
    dQdV = pd.Series(0).append((pd.Series(np.diff(Q) / np.diff(V))), ignore_index=True)
    if interp[0] == True:
        V_up = interp[2] if interp[2] != 0 else V.max()
        V_low = interp[3] if interp[3] != 0 else V.min()
        V_interp = pd.Series(np.linspace(V_up, V_low, interp[1]))
        Q_interp = interpolate.interp1d(V, Q, fill_value='extrapolate', bounds_error=False)
        V = V_interp
        Q = Q_interp(V_interp)
        dVdQ = pd.Series(0).append((pd.Series(np.diff(V) / np.diff(Q))), ignore_index=True)
        dQdV = pd.Series(0).append((pd.Series(np.diff(Q) / np.diff(V))), ignore_index=True)
    return (V, Q, dVdQ, dQdV)


def set_filter_I(data, table, I, step):
    idx_I = table[(table[('Current(A)', 'max')].abs().between(I * 0.99, I * 1.01) & (table.index.get_level_values('Type') == step))].index
    if idx_I.empty:
        raise ValueError(f"No matching step found for current: {I}A!")
        return -1
    t = []
    V = []
    I = []
    Q = []
    E = []
    T = []
    TEMP_COLS = [col for col in data.columns if 'AuxTemperature' in col]
    for i in np.arange(idx_I.size):
        conditions = [
         (data[CYCLE_NO_COL] == idx_I[i][0]) & (data[STEP_NO_COL] == idx_I[i][1]) & (data[STEP_TYPE_COL] == idx_I[i][2]) & (data['Code'] == 'Normal')]
        t.append(data[TIME_H_COL][np.where(conditions)[1]].reset_index(drop=True) * 3600)
        V.append(data[V_COL][np.where(conditions)[1]].reset_index(drop=True))
        I.append(data[I_COL][np.where(conditions)[1]].reset_index(drop=True))
        Q.append(data[Q_COL][np.where(conditions)[1]].reset_index(drop=True))
        E.append(data[E_COL][np.where(conditions)[1]].reset_index(drop=True))
        T.append([data[col][np.where(conditions)[1]].reset_index(drop=True).values for col in TEMP_COLS])

    return (t, V, I, Q, E, T)


def set_plot_style():
    mpl.rcParams['figure.figsize'] = (10, 6)
    mpl.rcParams['font.size'] = 16
    mpl.rcParams['savefig.dpi'] = 240


def plotRelax(t, volt, ID, amountCells, n_pulses):
    TOOLS = 'crosshair, hover,box_zoom, reset, pan, wheel_zoom, save'
    plot_width = 600
    plot_height = 500
    color = 20
    width = 2
    p = [figure(title='', x_axis_label='time / s', y_axis_label='Voltage / V', tools=TOOLS, y_range=(3.2,
                                                                                                     4.1), plot_width=plot_width, plot_height=plot_height) for a in range(amountCells)]
    p.append(figure(title='All cells', x_axis_label='time / s',
      y_axis_label='Voltage / V',
      tools=TOOLS,
      y_range=(3.2, 4.1),
      plot_width=plot_width,
      plot_height=(int(plot_height * 1.5))))
    a = 0
    for cell in np.arange(0, len(t), n_pulses):
        p[a].title.text = 'Cell ' + ID[cell]
        p[a].line((t[cell]), (volt[cell]), legend_label='Before 1st Pulse ', line_color=(Category20[color][0]), line_width=width)
        p[a].line((t[(cell + 1)]), (volt[(cell + 1)]), legend_label='Before 2nd Pulse ', line_color=(Category20[color][1]), line_width=width)
        p[a].line((t[(cell + 2)]), (volt[(cell + 2)]), legend_label='Before 3rd Pulse ', line_color=(Category20[color][2]), line_width=width)
        p[a].line((t[(cell + 3)]), (volt[(cell + 3)]), legend_label='Before 4th Pulse ', line_color=(Category20[color][3]), line_width=width)
        p[a].line((t[(cell + 4)]), (volt[(cell + 4)]), legend_label='Before 5th Pulse ', line_color=(Category20[color][4]), line_width=width)
        DeltaV_text = Label(x=1200, y=3.9, text=('Delta V 1st Pulse - last 1min: ' + str(round(volt[cell][(-61)] - volt[cell][(-1)], 3)) + ' V'), text_font_size='8pt')
        p[a].add_layout(DeltaV_text)
        DeltaV1_text = Label(x=1200, y=3.8, text=('Delta V 2nd Pulse - last 1min: ' + str(round(volt[(cell + 1)][(-61)] - volt[(cell + 1)][(-1)], 3)) + ' V'), text_font_size='8pt')
        p[a].add_layout(DeltaV1_text)
        DeltaV1_text = Label(x=1200, y=3.7, text=('Delta V 3th Pulse - last 1min: ' + str(round(volt[(cell + 2)][(-61)] - volt[(cell + 2)][(-1)], 3)) + ' V'), text_font_size='8pt')
        p[a].add_layout(DeltaV1_text)
        DeltaV1_text = Label(x=1200, y=3.6, text=('Delta V 4th Pulse - last 1min: ' + str(round(volt[(cell + 3)][(-61)] - volt[(cell + 3)][(-1)], 3)) + ' V'), text_font_size='8pt')
        p[a].add_layout(DeltaV1_text)
        DeltaV1_text = Label(x=1200, y=3.5, text=('Delta V 5th Pulse - last 1min: ' + str(round(volt[(cell + 4)][(-61)] - volt[(cell + 4)][(-1)], 3)) + ' V'), text_font_size='8pt')
        p[a].add_layout(DeltaV1_text)
        a = a + 1

    for i in range(0, len(p)):
        p[i].title.text_font_size = '20pt'
        p[i].legend.title = 'Legend'
        p[i].legend.location = 'bottom_left'
        p[i].legend.title_text_font_style = 'bold'
        p[i].legend.click_policy = 'hide'
        p[i].xaxis[0].ticker.desired_num_ticks = 10
        p[i].xaxis.major_tick_line_width = 3
        p[i].xaxis.axis_label_text_font_size = '8pt'
        p[i].xaxis.major_label_text_font_size = '9pt'
        p[i].ygrid.minor_grid_line_color = 'grey'
        p[i].ygrid.minor_grid_line_alpha = 0.2
        p[i].yaxis[0].ticker.desired_num_ticks = 10
        p[i].yaxis.major_tick_line_width = 3
        p[i].yaxis.axis_label_text_font_size = '12pt'
        p[i].yaxis.major_label_text_font_size = '12pt'
        p[i].axis.major_tick_out = 10
        p[i].axis.minor_tick_in = -3
        p[i].axis.minor_tick_out = 8

    output_file('PowerPulses_Relaxation analysis.html', title='PowerPulses ')
    grid = gridplot(p, ncols=3)
    show(grid)


def get_average(X1, Y1, X2, Y2):
    Y_interp = np.linspace(min(Y1.max(), Y2.max()), min(Y1.min(), Y2.min()), 1000)
    X1_interp = interpolate.interp1d(Y1, X1, fill_value='extrapolate', bounds_error=False)
    X2_interp = interpolate.interp1d(Y2, X2, fill_value='extrapolate', bounds_error=False)
    meanX = [np.mean([X1_interp(y), X2_interp(y)]) for y in Y_interp]
    dYdX = pd.Series(0).append((pd.Series(np.diff(Y_interp) / np.diff(meanX))), ignore_index=True)
    dXdY = pd.Series(0).append((pd.Series(np.diff(meanX) / np.diff(Y_interp))), ignore_index=True)
    return (
     Y_interp, meanX, dYdX, dXdY)


def get_Doe_name_EV32B1(string):
    if len(string) > 4:
        string1 = string[:3]
    else:
        string1 = string
    D = {'B24':'DDOE 1',  
         'B17':'DDOE 2', 
         'B16':'DDOE 3_1', 
         'B15':'DDOE 4_1', 
         'B14':'DDOE 5_2', 
         'B18':'DDOE 6_1', 
         'B19':'DDOE 4_2', 
         'B21':'DDOE 3_2_nonVD', 
         'B22':'DDOE 3_2VD', 
         'B23':'mDOE 1', 
         'B25':'mDOE 2 VD',
         
         'B32':'mDOE 3 VD',
         'B28':'mDOE 4 VD',
         'B30':'mDOE 5 VD',
         'B31':'mDOE 6 VD',
         
         'B26':'mDOE 7 VD',
         'B27':'mDOE 8 VD',
         'B29':'mDOE 9 VD',
         'B33':'mDOE 10 HP-ENC',
         'B34':'mDOE 10 VD-ENC',
         'B35':'mDOE 10 HP Capchecm'}
    result = D.get(string1)
    if result == None:
        result = string
    return result

def get_Doe_name_EV32B1_BMW(string):
    if len(string) > 4:
        string1 = string[:3]
    else:
        string1 = string
    D = {'B24':'SOE 1',  
         'B17':'SOE 2', 
         'B16':'SOE 3', 
         'B15':'SOE 4', 
         'B14':'SOE 5', 
         'B18':'SOE 6', 
         'B19':'SOE 4_2', 
         'B21':'SOE 3_2_nonVD', 
         'B22':'SOE 3_2VD', 
         
         'B23':'Setting design 1', 
         'B25':'Setting design 2',
         
         'B32':'Chemistry DoE 1',
         'B28':'Chemistry DoE 2',
         'B30':'Chemistry DoE 3',
         'B31':'Chemistry DoE 4',
         
         'B26':'Material SoE 1',
         'B27':'Material SoE 2',
         'B29':'Material SoE 3',
         'B33':'Material SoE 4_0 HP-ENC',
         'B34':'Material SoE 4_1 VD-ENC',
         'B35':'Material SoE 4_2 Capchem'}
    result = D.get(string1)
    if result == None:
        result = string
    return result
# okay decompiling /Users/marcus/Downloads/getDataPNE.cpython-37.pyc
