import glob
import pandas as pd

path = "C:/Users/sebra/Documents/MPT/Precitec/Metrology/Shawn_L/"
all_files = glob.glob(path + "*.dat")


data_all = []
for filename in all_files:
    df = pd.read_table(filename, delimiter=';',skiprows=6,index_col=False, on_bad_lines='skip')
    data_all.append(df)
    
num = 1
for data in data_all :
    data.to_csv(path+'test'+str(num)+'.csv', index=False, header=True)
    num = num + 1
    
    
    
