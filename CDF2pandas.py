import cdflib
import pandas as pd
import numpy as np
import os


vars = ['Epoch', 'YR', 'Day', 'HR', 'Rot#', 'IMF', 'PLS', 'IMF_PTS', 'PLS_PTS', 'ABS_B', 'F', 'THETA_AV', 'PHI_AV', 'BX_GSE', 'BY_GSE', 'BZ_GSE', 'BY_GSM', 'BZ_GSM', 'SIGMA-ABS_B', 'SIGMA-B', 'SIGMA-Bx', 'SIGMA-By', 'SIGMA-Bz', 'T', 'N', 'V', 'PHI-V', 'THETA-V', 'Ratio', 'Pressure', 'SIGMA-T', 'SIGMA-N', 'SIGMA-V', 'SIGMA-PHI-V', 'SIGMA-THETA-V', 'SIGMA-ratio', 'E', 'Beta', 'Mach_num', 'Mgs_mach_num', 'PR-FLX_1', 'PR-FLX_2', 'PR-FLX_4', 'PR-FLX_10', 'PR-FLX_30', 'PR-FLX_60', 'MFLX', 'R', 'F10_INDEX', 'KP', 'DST', 'AE', 'AP_INDEX', 'AL_INDEX', 'AU_INDEX', 'PC_N_INDEX', 'Solar_Lyman_alpha', 'Proton_QI']


#Init a data list:
data_list = []

#Loop over all the files in the data folder:
for file in os.listdir('data/'):
    #Check if the file is a csv file:
    if file.endswith('.cdf'):
        #Read the csv file:
        cdf_file = cdflib.CDF("data/"+file)
        data = {}
        for var in vars:
            data[var] = cdf_file.varget(var)
        spec_data = pd.DataFrame(data)
        data_list.append(spec_data)

#Make a dataframe from the data list:
dataf = pd.concat(data_list, axis=0, ignore_index=True)

dataf.to_csv('data/dataset_1993_2023.csv')


columns_for_regression_task = ['BX_GSE', 'BY_GSE', 'BZ_GSE', 'KP']
datafreg1h = dataf[columns_for_regression_task]
datafreg1h.loc[:, 'KP'] = datafreg1h['KP'] / 10

num_rows, num_columns = datafreg1h.shape

datafreg = pd.DataFrame(columns=columns_for_regression_task)

datafreg = datafreg1h.groupby(datafreg1h.index // 3).mean().reset_index(drop=True)

datafreg.to_csv('data/dataset_2013_2023_KP.csv')