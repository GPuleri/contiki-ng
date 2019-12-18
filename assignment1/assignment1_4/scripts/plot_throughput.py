import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,os

try:
    test,inFilename1,inFilename2,inFilename3,outFilename=sys.argv

except:
    print("Please specify all the filenames(with extension)!")
    exit(1)

#create a new figure
fig=plt.gcf()
#Read files csv
data1=pd.read_csv(inFilename1)
data2=pd.read_csv(inFilename2)
data3=pd.read_csv(inFilename3)

#Read the values for the node
row1=data1['Throughput_mean (%)'][0]
row2=data2['Throughput_mean (%)'][0]
row3=data3['Throughput_mean (%)'][0]
r1=data1['Throughput_std (%)'][0]
r2=data2['Throughput_std (%)'][0]
r3=data3['Throughput_std (%)'][0]

#Set the data for the graph
xaxis = ['0', '3', '7']
y = [round(row1,3),round(row2,3),round(row3,3)]
y_std = [r1,r2,r3]

#Draw the graph
plt.errorbar(xaxis,y,yerr=y_std, fmt='o')
for i,j in zip(xaxis,y):
    plt.annotate(str(j),xy=(i,j+0.01))

#Set the title and the axis of the graph
plt.suptitle('Throughput')
plt.xlabel('TX value (dBm)')
plt.ylabel('Throughput (%)')
plt.xticks(rotation=0)
plt.ylim(0,105)

#Saving Figure as png    
fig.savefig(outFilename)
