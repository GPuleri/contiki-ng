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
mycolumns=['Total_energy_before_mean (J)','Total_energy_before_std (J)',\
               'Total_energy_after_mean (J)','Total_energy_after_std (J)',\
               'Joining_time_mean (s)','Joining_time_std (s)']
myframe=pd.DataFrame(columns=mycolumns)

#Reading the 3 files for the average
df1 = pd.read_csv(inFilename1)
df2 = pd.read_csv(inFilename2)
df3 = pd.read_csv(inFilename3)

#Calculate the average
Total_energy_before_mean = np.mean((df1['Total_energy_before (J)'],df2['Total_energy_before (J)'],df3['Total_energy_before (J)']))
Total_energy_after_mean = np.mean((df1['Total_energy_after (J)'],df2['Total_energy_after (J)'],df3['Total_energy_after (J)']))
Joining_time_mean = np.mean((df1['Joining_time (s)'],df2['Joining_time (s)'],df3['Joining_time (s)']))

#calculate the std
Total_energy_before_std = np.std((df1['Total_energy_before (J)'],df2['Total_energy_before (J)'],df3['Total_energy_before (J)']))
Total_energy_after_std = np.std((df1['Total_energy_after (J)'],df2['Total_energy_after (J)'],df3['Total_energy_after (J)']))
Joining_time_std = np.std((df1['Joining_time (s)'],df2['Joining_time (s)'],df3['Joining_time (s)']))


#Setting the values into the table
data=[[Total_energy_before_mean,Total_energy_before_std,\
  Total_energy_after_mean,Total_energy_after_std,\
  Joining_time_mean,Joining_time_std]]
frame=pd.DataFrame(data,columns=mycolumns) 
myframe=myframe.append(frame)
    
#Writing to csv File
export_to_csv=myframe.to_csv(outFilename,index=None,header=True)
