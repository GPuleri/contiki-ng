import pandas as pd
import re
import sys,os

try:
    test,inFilename,outFilename=sys.argv

except:
    print("Please specify all the filenames(with extension)!")
    exit(1)

#Creating columns
mycolumns=['CPU (s)','LPM (s)','LISTEN (s)','Total time (s)',\
                       'CPU_energy (J)','LPM_energy (J)','LISTEN_energy (J)',\
                       'Total_energy (J)']
myframe=pd.DataFrame(columns=mycolumns)

#Set the patterns to retrieve the data
pattern=r'[ ]*CPU[ ]*(\d+)s[ ]*LPM[ ]*(\d+)s[ ]*DEEP LPM[ ]*'\
        +r'(\d+)s[ ]*Total time[ ]*(\d+)s[ ]*[\n]'\
        +r'*[ ]*Radio LISTEN[ ]*(\d+)s[ ]*TRANSMIT[ ]*(\d+)s[ ]*OFF[ ]*(\d+)s*[\n][\n]'\
        +r'End of program'

file=open(inFilename,'r').read()
stats=re.findall(pattern,file)

#Energy consumption parameters
input_volt=3

#Device Profiling (Ampere)
CPU_consumption=15.35*pow(10,-3)
LPM_consumption=9.59*pow(10,-3)
LISTEN_consumption=28.32*pow(10,-3)

#Calculate the energy consumption before
for values in stats:
	#CPU energy
	CPU_energy=CPU_consumption*int(values[0])*input_volt
	#LPM energy
	LPM_energy=LPM_consumption*int(values[1])*input_volt
	#LISTEN energy
	LISTEN_energy=LISTEN_consumption*int(values[4])*input_volt
	#Calculate total energy consumption
	Total_energy=CPU_energy+LPM_energy+LISTEN_energy

	#Setting the values into the table
	data=[[values[0],values[1],values[4],values[3],\
		CPU_energy,LPM_energy,LISTEN_energy,Total_energy]]
	frame=pd.DataFrame(data,columns=mycolumns) 
	myframe=myframe.append(frame)

#Writing to csv File
export_to_csv=myframe.to_csv(outFilename,index=None,header=True)
