import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,os

try:
    test,inFilename1,inFilename2,inFilename3,inFilename4,inFilename5,\
inFilename6,outFilename=sys.argv

except:
    print("Please specify all the filenames(with extension)!")
    exit(1)

#create a new figure
fig=plt.gcf()
#Read files csv
data1=pd.read_csv(inFilename1)
data2=pd.read_csv(inFilename2)
data3=pd.read_csv(inFilename3)
data4=pd.read_csv(inFilename4)
data5=pd.read_csv(inFilename5)
data6=pd.read_csv(inFilename6)

#Read the values for the leaf
row1=data1['Total_energy_mean (J)'][0]
row2=data2['Total_energy_mean (J)'][0]
row3=data3['Total_energy_mean (J)'][0]
r1=data1['Total_energy_std (J)'][0]
r2=data2['Total_energy_std (J)'][0]
r3=data3['Total_energy_std (J)'][0]

#Read the values for the root
row4=data4['Total_energy_mean (J)'][0]
row5=data5['Total_energy_mean (J)'][0]
row6=data6['Total_energy_mean (J)'][0]
r4=data4['Total_energy_std (J)'][0]
r5=data5['Total_energy_std (J)'][0]
r6=data6['Total_energy_std (J)'][0]

#Set the data for the graph
xaxis = ['0', '3', '7']

#leaf
y = [round(row1,3),round(row2,3),round(row3,3)]
y_std = [r1,r2,r3]

#root
y2 = [round(row4,3),round(row5,3),round(row6,3)]
y_std2 = [r4,r5,r6]

#Draw the graph
plt.errorbar(xaxis,y,yerr=y_std, fmt='o', label="leaf")
plt.errorbar(xaxis,y2,yerr=y_std2, fmt='o', label="root")
for i,j in zip(xaxis,y):
    plt.annotate(str(j),xy=(i,j+0.01))
for i,j in zip(xaxis,y2):
    plt.annotate(str(j),xy=(i,j-0.02))

#Set the title and the axis of the graph
plt.suptitle('Aggregated energy consumption')
plt.xlabel('TX value (dBm)')
plt.ylabel('Energy consumption (J)')
plt.legend()
plt.xticks(rotation=0)

#Saving Figure as png    
fig.savefig(outFilename)
