# Assignment 1_2 - Analysing the 6TiSCH energy consumption

Team: 
* Gianluca Puleri
* Simone Monti

----

The source code of the project is available in this directory.




## Overview of the analysis

For this analysis, we compare the energy consumption during a certain time period
of the entire 6TiSCH stack to when only enabling the TSCH MAC layer, after network
convergence. For both analyses, we report on the consumption of the root and the leaf
node separately. In our report we explain the reasons for the consumption differences.
For all analyses, we will use the default network stack settings configured by Contiki-NG.




## Directories description

Inside of the base directory `assignment1_2` there are two sub-projects, two folders and two files:
* `6TiSCH_stack`, this sub-project contains the files needed for the analysis of the entire 6TiSCH stack.
* `TSCH_MAC_layer`, this sub-project contains the files needed for the analysis of the TSCH MAC layer.
* `plots`, this folder contains the various plots obtained by the scripts.
* `scripts`, this folder contains the various scripts used to obtain the plots.
* `README.md`, this file contains information about other files in the sub-directories.
* `data.zip`, this file contains the data used for the plots.

Each of these sub-projects contain the following sub-directories:

* `LEAF`, this directory contains all the files needed to run the leaf node.
* `ROOT`, this directory contains all the files needed to run the root node.

Each of these sub-directories contain the following files:

* `Makefile`, this file contains a set of directives used by a make build automation tool to generate a target/goal. This Makefile can define the MODULES variable, a list of modules that should be included. It can also configure the Contiki-NG networking stack.
* `project-conf.h`, this file contains C declarations and macro definitions. It is used to configure the develop environment, the system configuration and the various layers of the stack.
* `assignment1_2.c`, this file contains the class that is meant to be run.




## Running the project
### How to compile

Please check if you have already installed Docker and Contiki-NG. Also check if your two Zolertia Re-Mote are connected.
To start a bash inside a new container, simply type:

```bash
contiker
```
You must be under /home/*user*/contiki-ng in the container, which is mapped to your local copy of Contiki-NG.

Sometimes it is useful to have multiple terminal sessions within a single container. 
To achieve this, open a new terminal and start by running:

```bash
$ docker ps
```
This will present you with a list of container IDs. Select the ID of the container you wish to open a terminal for and then
```bash
$ docker exec -it <the ID> /bin/bash
```
Now we have two terminal sessions within a single container.

In both terminal session we will move to the specific sub-project (in base of which of them we want to run) simply typing:

```bash
cd assignment1/assignment1_2/6TiSCH_stack
```
or
```bash
cd assignment1/assignment1_2/TSCH_MAC_layer
```


At this point, we will move in the first terminal session to the root node simply tiping:

```bash
cd ROOT
```

and in the second terminal session to the leaf node:

```bash
cd LEAF
```



Now, in every terminal session, it is useful saves our settings and after compile the project (nodes can be something like *'/dev/ttyUSB0'* or *'/dev/ttyUSB1'*):

```bash
make TARGET=zoul BOARD=firefly savetarget
make MOTES='<1st node>' or '<2nd node>' assignment1_2.upload
```



### How to run

From this point (for both sub-projects) we can run the project simply typing:

```bash
make MOTES=<1st node> login
```
for the first terminal session, and:
```bash
make MOTES=<2nd node> login
```
for the second terminal session.



### How to run the scripts

Here we have 4 files:

* `energy.py`, this script is meant to retrieve data from the .txt files and convert them into a .csv files.
* `average.py`, this script is meant to make the average among the three .csv files.
* `plot.py`, this script is meant to draw the graphs.
* `plotComparison.py`, this script is meant to draw the graphs to compare root/leaf with different configurations.

#### energy.py

For all the .txt files:
```bash
python3 energy.py <txt file> <csv file>
```
For instance:
```bash
python3 energy.py ../data/leaf1.txt ../data/leaf1.csv
```

#### average.py

For all the .csv files (of the same configuration):
```bash
python3 average.py <1st csv file> <2nd csv file> <3rd csv file> <final csv file>
```
For instance:
```bash
python3 average.py ../data/leaf1.csv ../data/leaf2.csv ../data/leaf3.csv ../data/leaf.csv
```

#### plot.py

```bash
python3 plot.py <root csv file> <leaf csv file> <png file>
```
For instance:
```bash
python3 plot.py ../data/root.csv ../data/leaf.csv ../plots/energy.png
```

#### plotComparison.py

```bash
python3 plotComparison.py <root csv file> <root TSCH csv file> <png file>
```
For instance:
```bash
python3 plotComparison.py ../data/root.csv ../data/rootTSCH.csv ../plots/rootComparison.png
```

