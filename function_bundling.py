from ast import Break
import pandas as pd
import numpy as np
import configparser
import logging


def get_cfg(cfg_path, cfg_section, request_item):
    config = configparser.ConfigParser()
    config.read_file(open(r'{}'.format(cfg_path)))
    item =  config.get(cfg_section, request_item)
    return item
    
def open_csv (path):
    df = pd.read_csv(path)
    return df

def numeric_formating (dataframe, col_name):
    dataframe[col_name] = pd.to_numeric(dataframe[col_name])
    dataframe[col_name] = dataframe[col_name].astype(float)
    return dataframe[col_name]

def timestamp_formating(dataframe, column_timestamp, pandas_time_key):
    dataframe[column_timestamp] = pd.to_datetime(dataframe[column_timestamp])
    dataframe[column_timestamp] =dataframe[column_timestamp].dt.round(pandas_time_key)
    dataframe[column_timestamp] =dataframe[column_timestamp].dt.tz_localize(None)
    return dataframe

def time_diff_col (dataframe, column_timestamp, mk_column_timediff):
    dataframe[mk_column_timediff] = dataframe[column_timestamp].diff()
    return dataframe

def fill_missing_time (dataframe, column_timestamp, pandas_time_key, mk_interpolation_folder):
    #resampling data
    dataframe = dataframe.set_index(column_timestamp)
    dataframe = dataframe.resample(pandas_time_key).sum()
    dataframe = dataframe.replace(0.0, np.nan)
    #make interpolation column
    dataframe[mk_interpolation_folder] = dataframe.interpolate()
    return dataframe

def summarize_val (dataframe,  value_sign,):
    if value_sign == 'charge' :
        charge =  dataframe[dataframe<0.0].sum()
        return charge
    elif value_sign == 'discharge':
        return dataframe[dataframe> 0.0].sum()

def sum_result_charge(dataframe):
    print (summarize_val(dataframe , value_sign='charge'))
    return summarize_val(dataframe , value_sign='charge')

def sum_result_discharge(dataframe):
    print (summarize_val(dataframe , value_sign='discharge'))
    return summarize_val(dataframe , value_sign='discharge')

def str_val (df, data_status, interpolating_status, charge_val, discharge_val ):
    if data_status == False:
        print('data clean : {}, interpolate : {}\n total charging : {} \n total discharge : {} '.format(data_status, interpolating_status, charge_val, discharge_val))
        return 'data clean : {}, interpolate : {}\n total charging : {} \n total discharge : {} '.format(data_status, interpolating_status, charge_val, discharge_val)
    elif data_status == True:
        print('data clean : {}, interpolate : {}\n total charging : {} \n total discharge : {} '.format(data_status, interpolating_status,  charge_val, discharge_val))
        return 'data clean : {}, interpolate : {}\n total charging : {} \n total discharge : {} '.format(data_status, interpolating_status,  charge_val, discharge_val)

def saving_data_to_csv (dataframe, location_path, save_file_name):
    dataframe.to_csv('{}{}'.format(location_path, save_file_name))

def reruning_script (msg_userinput):
    user_input = input('{}\n'.format(msg_userinput))
    user_input.lower()
    if user_input == 'true':
        print('you re-run script')
    elif user_input == 'false':
        print('closing the script - thank you')
        return False

def logging_error (error_exception):
    logging.basicConfig(filename='error.log',filemode = 'a' , format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(error_exception)
