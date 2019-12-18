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
mycolumns=['Total_energy_mean (J)','Total_energy_std (J)']
myframe=pd.DataFrame(columns=mycolumns)

#Reading the 3 files for the average
df1 = pd.read_csv(inFilename1)
df2 = pd.read_csv(inFilename2)
df3 = pd.read_csv(inFilename3)

#Calculate the average
Energy_mean = np.mean((df1['Total_energy (J)'],df2['Total_energy (J)'],df3['Total_energy (J)']))

#calculate the std
Energy_std = np.std((df1['Total_energy (J)'],df2['Total_energy (J)'],df3['Total_energy (J)']))

#Setting the values into the table
data=[[Energy_mean,Energy_std]]
frame=pd.DataFrame(data,columns=mycolumns) 
myframe=myframe.append(frame)
    
#Writing to csv File
export_to_csv=myframe.to_csv(outFilename,index=None,header=True)
