import pandas as pd
import re
import sys,os

try:
    test,inFilename1,inFilename2,inFilename3,outFilename=sys.argv

except:
    print("Please specify all filenames(with extension)!")
    exit(1)

#Creating columns
mycolumns=['CPU (s)','LPM (s)','LISTEN (s)','Total time (s)',\
                       'CPU_energy (J)','LPM_energy (J)','LISTEN_energy (J)',\
                       'Total_energy (J)','Total_energy_persecond (J)']
myframe=pd.DataFrame(columns=mycolumns)

#Reading the 3 files for the average
df1 = pd.read_csv(inFilename1)
df2 = pd.read_csv(inFilename2)
df3 = pd.read_csv(inFilename3)

#Make the average
for i in range(0,60):
    CPU = np.mean((df1['CPU (s)'][i],df2['CPU (s)'][i],df3['CPU (s)'][i]))
    LPM = np.mean((df1['LPM (s)'][i],df2['LPM (s)'][i],df3['LPM (s)'][i]))
    LISTEN = np.mean((df1['LISTEN (s)'][i],df2['LISTEN (s)'][i],df3['LISTEN (s)'][i]))
    TOTALTIME = np.mean((df1['Total time (s)'][i],df2['Total time (s)'][i],df3['Total time (s)'][i]))
    CPU_energy = np.mean((df1['CPU_energy (J)'][i],df2['CPU_energy (J)'][i],df3['CPU_energy (J)'][i]))
    LPM_energy = np.mean((df1['LPM_energy (J)'][i],df2['LPM_energy (J)'][i],df3['LPM_energy (J)'][i]))
    LISTEN_energy = np.mean((df1['LISTEN_energy (J)'][i],df2['LISTEN_energy (J)'][i],df3['LISTEN_energy (J)'][i]))
    Total_energy = np.mean((df1['Total_energy (J)'][i],df2['Total_energy (J)'][i],df3['Total_energy (J)'][i]))
    Total_energy_persecond = np.mean((df1['Total_energy_persecond (J)'][i],df2['Total_energy_persecond (J)'][i],df3['Total_energy_persecond (J)'][i]))

    #Setting the values into the table
    data=[[CPU,LPM,LISTEN,TOTALTIME,\
          CPU_energy,LPM_energy,LISTEN_energy,Total_energy,Total_energy_persecond]]
    frame=pd.DataFrame(data,columns=mycolumns) 
    myframe=myframe.append(frame)
    
#Writing to csv File
export_to_csv=myframe.to_csv(outFilename,index=None,header=True)
