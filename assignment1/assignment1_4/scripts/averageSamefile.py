import pandas as pd
import numpy as np
import re
import sys,os

try:
    test,inFilename1,outFilename=sys.argv

except:
    print("Please specify all filenames(with extension)!")
    exit(1)

#Creating columns
mycolumns=['Total_energy_mean (J)','Total_energy_std (J)',\
          'Latency_mean (ms)','Latency_std (ms)',\
          'Throughput_mean (%)','Throughput_std (%)',\
          'kbit/Joule_mean','kbit/Joule_std']
myframe=pd.DataFrame(columns=mycolumns)

#Reading the 3 files for the average
df1 = pd.read_csv(inFilename1)

#Calculate the average
Energy_mean = np.mean((df1['Total_energy (J)']))
Latency_mean = np.mean((df1['Latency (ms)']))
Throughput_mean = np.mean((df1['Throughput (%)']))
kbit_mean = np.mean((df1['kbit/Joule']))

#calculate the std
Energy_std = np.std((df1['Total_energy (J)']))
Latency_std = np.std((df1['Latency (ms)']))
Throughput_std = np.std((df1['Throughput (%)']))
kbit_std = np.std((df1['kbit/Joule']))

#Setting the values into the table
data=[[Energy_mean,Energy_std,Latency_mean,Latency_std,\
       Throughput_mean,Throughput_std,kbit_mean,kbit_std]]
frame=pd.DataFrame(data,columns=mycolumns) 
myframe=myframe.append(frame)
    
#Writing to csv File
export_to_csv=myframe.to_csv(outFilename,index=None,header=True)
