import pandas as pd
import numpy as np
import re
import sys,os

try:
    test,inFilename1,inFilename2,inFilename3,outFilename=sys.argv

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
df2 = pd.read_csv(inFilename2)
df3 = pd.read_csv(inFilename3)

#Calculate the average
Energy_mean = np.mean((df1['Total_energy_mean (J)'],df2['Total_energy_mean (J)'],df3['Total_energy_mean (J)']))
Latency_mean = np.mean((df1['Latency_mean (ms)'],df2['Latency_mean (ms)'],df3['Latency_mean (ms)']))
Throughput_mean = np.mean((df1['Throughput_mean (%)'],df2['Throughput_mean (%)'],df3['Throughput_mean (%)']))
kbit_Joule_mean = np.mean((df1['kbit/Joule_mean'],df2['kbit/Joule_mean'],df3['kbit/Joule_mean']))

#calculate the std
Energy_std = np.mean((df1['Total_energy_std (J)'],df2['Total_energy_std (J)'],df3['Total_energy_std (J)']))
Latency_std = np.mean((df1['Latency_std (ms)'],df2['Latency_std (ms)'],df3['Latency_std (ms)']))
Throughput_std = np.mean((df1['Throughput_std (%)'],df2['Throughput_std (%)'],df3['Throughput_std (%)']))
kbit_Joule_std = np.mean((df1['kbit/Joule_std'],df2['kbit/Joule_std'],df3['kbit/Joule_std']))

#Setting the values into the table
data=[[Energy_mean,Energy_std,Latency_mean,Latency_std,\
       Throughput_mean,Throughput_std,kbit_Joule_mean,kbit_Joule_std]]
frame=pd.DataFrame(data,columns=mycolumns) 
myframe=myframe.append(frame)
    
#Writing to csv File
export_to_csv=myframe.to_csv(outFilename,index=None,header=True)
