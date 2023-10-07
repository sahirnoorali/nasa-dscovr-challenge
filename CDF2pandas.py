import cdflib
import pandas as pd


cdf_file = cdflib.CDF('data/omni2_h0_mrg1hr_20230101_v01.cdf')
vars = ['Epoch', 'YR', 'Day', 'HR', 'Rot#', 'IMF', 'PLS', 'IMF_PTS', 'PLS_PTS', 'ABS_B', 'F', 'THETA_AV', 'PHI_AV', 'BX_GSE', 'BY_GSE', 'BZ_GSE', 'BY_GSM', 'BZ_GSM', 'SIGMA-ABS_B', 'SIGMA-B', 'SIGMA-Bx', 'SIGMA-By', 'SIGMA-Bz', 'T', 'N', 'V', 'PHI-V', 'THETA-V', 'Ratio', 'Pressure', 'SIGMA-T', 'SIGMA-N', 'SIGMA-V', 'SIGMA-PHI-V', 'SIGMA-THETA-V', 'SIGMA-ratio', 'E', 'Beta', 'Mach_num', 'Mgs_mach_num', 'PR-FLX_1', 'PR-FLX_2', 'PR-FLX_4', 'PR-FLX_10', 'PR-FLX_30', 'PR-FLX_60', 'MFLX', 'R', 'F10_INDEX', 'KP', 'DST', 'AE', 'AP_INDEX', 'AL_INDEX', 'AU_INDEX', 'PC_N_INDEX', 'Solar_Lyman_alpha', 'Proton_QI']

data = {}

for var in vars:
    data[var] = cdf_file.varget(var)

dataf = pd.DataFrame(data)