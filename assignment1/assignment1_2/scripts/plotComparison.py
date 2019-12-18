import pandas as pd
import matplotlib.pyplot as plt
import sys,os

try:
    test,inFilename1,inFilename2,outFilename=sys.argv

except:
    print("Please specify all the filenames(with extension)!")
    exit(1)

#create a new figure
fig=plt.gcf() 
data1=pd.read_csv(inFilename1)
data2=pd.read_csv(inFilename2)
#create axis
curr_axis=plt.gca()

#Draw the graph
data1.plot(kind='line',x='Total time (s)',y='Total_energy (J)',label='6TiSCH',ax=curr_axis)
data2.plot(kind='line',x='Total time (s)',y='Total_energy (J)',label='TSCH',ax=curr_axis)

#Set the title and the axis
if 'root' in outFilename:
    plt.suptitle('Total energy consumption of the root 6TiSCH vs TSCH')
if 'leaf' in outFilename:
    plt.suptitle('Total energy consumption of the leaf 6TiSCH vs TSCH')
plt.xlabel('Time (s)')
plt.ylabel('Energy consumption (J)')
plt.axis([0, 59, 0, 2])

#Saving Figure as png    
fig.savefig(outFilename)
