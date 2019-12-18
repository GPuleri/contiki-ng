import pandas as pd
import matplotlib.pyplot as plt
import sys,os

try:
    test,inFilename1,inFilename2,inFilename3,inFilename4,inFilename5,outFilename=sys.argv

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

#Read the joining times (mean and std)
row1=data1['Joining_time_mean (s)'][0]
row2=data2['Joining_time_mean (s)'][0]
row3=data3['Joining_time_mean (s)'][0]
row4=data4['Joining_time_mean (s)'][0]
row5=data5['Joining_time_mean (s)'][0]
r1=data1['Joining_time_std (s)'][0]
r2=data2['Joining_time_std (s)'][0]
r3=data3['Joining_time_std (s)'][0]
r4=data4['Joining_time_std (s)'][0]
r5=data5['Joining_time_std (s)'][0]

#Set data for the graph
xaxis = ['EBperiod_2', 'CH_HOP_1', 'EBperiod_8', 'CH_HOP_2', 'default']
y = [round(row1,2),round(row2,2),round(row3,2),round(row4,2),round(row5,0)]
y_std = [r1,r2,r3,r4,r5]

#Draw the graph
plt.errorbar(xaxis,y,yerr=y_std, fmt='o')
for i,j in zip(xaxis,y):
    plt.annotate(str(j),xy=(i,j+1.5))

#Set the title and the axis of the graph
plt.suptitle('Joining time of the leaf')
plt.xlabel('Parameters')
plt.ylabel('Time (s)')
plt.xticks(rotation=0)

#Saving Figure as png    
fig.savefig(outFilename)
