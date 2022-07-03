# electric_battery

Hi Cannopy Power.. , 
Thankyou for inviting me to this test, iam really grateful.

Here my explanation as per your request to finishing the test assignment: 
  1 Q : Please use python for the calculation
    A : Yes, this calculation are made using python.
    
  2 Q : Please include the explanation on how you are doing the calculation in ReadMe
    A : Actually the calculation really straighforward, I only summarize based on Charge (negative value) and Discharge (positive value).
        In my knowledge there is not any another variable or information like to calculate DoD or SoC .
        For interpolation i using built-in linear pandas modul (Pd.interpolate()).
        
  3 Q : Also include your email address and instruction to run the code in ReadMe
    A : Here my email address "azka.mhmmd@gmail.com" and how to running the code i will explain below.
    
Running script :
I assume your computer already has python program so i'am not make executable file.

1. Download this repository or you can pull directly to your computer.
2. Install all dependencies in requirements.txt to your virtual environment using pip (pip install -r requirements.txt) 
3. After installation process finish, you can running this program on your terminal "py main.py"
4. You can make several mode calculation in this script  :
          a : Calculation of raw data without any cleansing before.
          b : Calculation of clean data without interpolation.
          c : Calculation of clean data with interpolation.
          d : Calculation both raw data and clean data with interpolation
5. After you run calculation (b,c,d) you will be ask to save cleansed data.
6. There will be re-run option after save finish.

ps : 
1. I adding function to read multiple csv file on folder and its works! unfortunately there is little bug in saving multiple file , so i deciding to hardcoded the "save name file".
   At minimum this program can run to answer test challenge, and need little workaround to make extensive feature(eg: read, calculate and save multiple csv)
2. You can play around with configuration file to configuring like loading or saving directory.

Hopefully i get feedback from you guys to improving my self (bad or good).
Again thank you for this chance,

Best regards
Azka


Thank
