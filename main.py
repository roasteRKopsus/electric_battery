from sqlalchemy import func
from sympy import fu
import executable_function
import function_bundling
import os

#config for path
cfg_raw_file_path = function_bundling.get_cfg('config_file.cfg', 'SECTION_PATH', 'raw_data_path')
cfg_save_file_path = function_bundling.get_cfg('config_file.cfg', 'SECTION_PATH', 'save_data_path')
cfg_save_name = function_bundling.get_cfg('config_file.cfg', 'SECTION_PATH', 'save_file_name')

#config for column name 
cfg_column_battery_power = function_bundling.get_cfg('config_file.cfg', 'SECTION_COLUMN_NAME', 'column_battery_power')
cfg_column_timestamp = function_bundling.get_cfg('config_file.cfg', 'SECTION_COLUMN_NAME', 'column_timestamp')
cfg_column_timediff = function_bundling.get_cfg('config_file.cfg', 'SECTION_COLUMN_NAME', 'column_timediff')
cfg_column_interpolation = function_bundling.get_cfg('config_file.cfg', 'SECTION_COLUMN_NAME', 'column_interpolation')

#config for pandas key
cfg_pandas_minutes_key = function_bundling.get_cfg('config_file.cfg', 'SECTION_KEY_PANDAS', 'minutes')

#config for error handling message
cfg_wrong_input_val = function_bundling.get_cfg('config_file.cfg', 'SECTION_ERROR_MSG', 'wrong_input')
cfg_close_script = function_bundling.get_cfg('config_file.cfg', 'SECTION_ERROR_MSG', 'close_script')

#config for info message 
cfg_rerun_script_info = function_bundling.get_cfg('config_file.cfg', 'SECTION_INFO_MSG', 'rerun_script')
cfg_file_not_save_info = function_bundling.get_cfg('config_file.cfg', 'SECTION_INFO_MSG', 'file_not_save_info')

#config userinput info
cfg_clean_data_userinput = function_bundling.get_cfg('config_file.cfg', 'SECTION_INFO_MSG', 'clean_data_input_info')
cfg_clean_data_interpolate_userinput = function_bundling.get_cfg('config_file.cfg', 'SECTION_INFO_MSG', 'clean_data_interpolate_info')
cfg_save_data_userinput = function_bundling.get_cfg('config_file.cfg', 'SECTION_INFO_MSG', 'save_clean_data')

is_running = True

while is_running:

    try:
    
        print ('\nWelcome : this is simple program to calculate total charge and discharge')
        data_clean = input('{}\n'.format(cfg_clean_data_userinput))
        data_clean = data_clean.lower()

        if data_clean == "false":

            notclean_data = executable_function.run_function(path=cfg_raw_file_path, col_battery=cfg_column_battery_power, col_timediff=cfg_column_timediff, col_timestamp=cfg_column_timestamp,col_interpolation=cfg_column_interpolation ,pandas_minutes_key=cfg_pandas_minutes_key, is_clean_data= False, is_interpolating_data=False, )
            re_run = function_bundling.reruning_script(msg_userinput=cfg_rerun_script_info)
            if re_run == False:
                break


        elif data_clean == 'true' or data_clean == 'clean_and_raw':

            if data_clean == 'true':
                data_interpolated = input('{}\n'.format(cfg_clean_data_interpolate_userinput))
                data_interpolated = data_interpolated.lower()
                if data_interpolated == "true":
                    processed_data = executable_function.run_function(path=cfg_raw_file_path, col_battery=cfg_column_battery_power, col_timediff=cfg_column_timediff, col_timestamp=cfg_column_timestamp, col_interpolation=cfg_column_interpolation, pandas_minutes_key=cfg_pandas_minutes_key, is_clean_data= True, is_interpolating_data=True, )
                elif data_interpolated == "false":
                    processed_data = executable_function.run_function(path=cfg_raw_file_path, col_battery=cfg_column_battery_power, col_timediff=cfg_column_timediff, col_timestamp=cfg_column_timestamp, col_interpolation=cfg_column_interpolation, pandas_minutes_key=cfg_pandas_minutes_key, is_clean_data= True, is_interpolating_data=False, )
            elif data_clean == 'clean_and_raw':
                not_clean_data = executable_function.run_function(path=cfg_raw_file_path, col_battery=cfg_column_battery_power, col_timediff=cfg_column_timediff, col_timestamp=cfg_column_timestamp,col_interpolation=cfg_column_interpolation ,pandas_minutes_key=cfg_pandas_minutes_key, is_clean_data= False, is_interpolating_data=False, )
                processed_data = executable_function.run_function(path=cfg_raw_file_path, col_battery=cfg_column_battery_power, col_timediff=cfg_column_timediff, col_timestamp=cfg_column_timestamp, col_interpolation=cfg_column_interpolation, pandas_minutes_key=cfg_pandas_minutes_key, is_clean_data= True, is_interpolating_data=True, )
            save_file = input('{}\n'.format(cfg_save_data_userinput))
            save_file = save_file.lower()
            if save_file == 'true' :
                head_path, tail_path = os.path.split(cfg_raw_file_path)
                print(tail_path)
                #need improvement and workaround
                save_name = 'clean_.csv'
                print('you can check save file at {}'.format(save_name))
                function_bundling.saving_data_to_csv(dataframe=processed_data, location_path=cfg_save_file_path, save_file_name=save_name )    
            elif save_file == 'false':
                print(cfg_file_not_save_info)
            else : 
                print(cfg_wrong_input_val)

            re_run = function_bundling.reruning_script(msg_userinput=cfg_rerun_script_info)

            
            if re_run == False:
                break
        # else : 
        #     print(cfg_wrong_input_val)
        #     print(cfg_close_script)


        else :
            print(cfg_wrong_input_val)
            print(cfg_close_script)
            print('\n')

    except Exception as err:
        function_bundling.logging_error(err)
        break






