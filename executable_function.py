from turtle import backward
import function_bundling
import configparser
import time
from os import listdir, remove
from os.path import isfile, join



def run_function(path, col_battery, col_timestamp, col_timediff,col_interpolation, pandas_minutes_key, is_interpolating_data, is_clean_data):
    path_folder = path
    files_folder = [f for f in listdir(path_folder) if isfile(join(path_folder, f))]
    for data in files_folder:
        filepath = '{}\\{}'.format(path_folder, data)
        charge = []
        discharge = []
        df = function_bundling.open_csv(filepath)
        df_numeric_raw = function_bundling.numeric_formating(dataframe=df, col_name=col_battery)  
        # print(df_group_by)
        time.sleep(1)
        if is_clean_data == False  :
            charge.append(function_bundling.sum_result_charge(df_numeric_raw))
            discharge.append(function_bundling.sum_result_discharge(df_numeric_raw))
            string_val = function_bundling.str_val(df = df , data_status=is_clean_data, interpolating_status= is_interpolating_data, charge_val=charge, discharge_val=discharge)
            # print(string_val)

        if is_clean_data == True :
            df_timestamp_clean = function_bundling.timestamp_formating(dataframe= df, column_timestamp= col_timestamp, pandas_time_key=pandas_minutes_key)
            df_timediff = function_bundling.time_diff_col(dataframe=df, column_timestamp=col_timestamp, mk_column_timediff=col_timediff)
            df_fill_missing_time = function_bundling.fill_missing_time(dataframe=df, column_timestamp=col_timestamp, pandas_time_key=pandas_minutes_key, mk_interpolation_folder=col_interpolation)
            # df_timestamp_clean = function_bundling.timestamp_formating(dataframe= df, column_timestamp= col_timestamp, pandas_time_key=pandas_minutes_key)
            if is_interpolating_data == True:
                df_numeric_clean = function_bundling.numeric_formating(dataframe=df_fill_missing_time, col_name=col_interpolation)
                charge.append(function_bundling.sum_result_charge(df_numeric_clean))
                discharge.append(function_bundling.sum_result_discharge(df_numeric_clean))
                string_val = function_bundling.str_val(df = df , data_status=is_clean_data, interpolating_status= is_interpolating_data,charge_val=charge, discharge_val=discharge )
            elif is_interpolating_data == False:
                charge.append(function_bundling.sum_result_charge(df_numeric_raw))
                discharge.append(function_bundling.sum_result_discharge(df_numeric_raw))
                string_val = function_bundling.str_val(df = df , data_status=is_clean_data, interpolating_status= is_interpolating_data, charge_val=charge, discharge_val=discharge )
                
            return df_fill_missing_time