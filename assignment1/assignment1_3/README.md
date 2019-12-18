# Assignment 1_3 - Analysing the TSCH joining process

Team: 
* Gianluca Puleri
* Simone Monti

----

The source code of the project is available in this directory.



## Overview of the analysis

This analysis investigates the joining process of a node to a TSCH network. We disable the
6TiSCH stack. We report on the time it takes to join the network and the energy consumed
by the joining node and the root node. Our report explain the different parameters that influence this joining process and how. Moreover, we investigate the *EB period* and the *channel hopping sequence* in greater detail.



## Directories description

The base directory is `assignment1_3`, it contains the files needed for the second analysis.
Inside of it we find the following two sub-directories, two folders and two files: 

* `LEAF`, this directory contains all the files needed to run the leaf node.
* `ROOT`, this directory contains all the files needed to run the root node.
* `plots`, this folder contains the various plots obtained by the scripts.
* `scripts`, this folder contains the various scripts used to obtain the plots.
* `data.zip`, this file that contains the data used for the plots.
* `README.md`, this file contains information about other files in the sub-directories.

Each of these sub-directories contain the following files:

* `Makefile`, this file contains a set of directives used by a make build automation tool to generate a target/goal. This Makefile can define the MODULES variable, a list of modules that should be included. It can also configure the Contiki-NG networking stack.
* `project-conf.h`, this file contains C declarations and macro definitions. It is used to configure the develop environment, the system configuration and the TSCH layer.
* `assignment1_3.c`, this file contains the class that is meant to be run.



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

After the execution of this command we have two terminal sessions within a single container.

We move to the specific folder simply typing:
```bash
cd assignment1/assignment1_3
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
make MOTES='<1st node>' or '<2nd node>' assignment1_3.upload
```



### How to run

From this point, we can run the project simply typing:

```bash
make MOTES=<1st node> login
```
for the first terminal session, and:
```bash
make MOTES=<2nd node> login
```
for the second terminal session.

### How to run the scripts

Here we have 5 files:

* `energy_time.py`, this script is meant to retrieve data from the .txt files and convert them into a .csv files.
* `average.py`, this script is meant to make the average among the three .csv files.
* `plot_time.py`, this script is meant to draw the graphs of the joining time.
* `plot_energy.py`, this script is meant to draw the graphs of the energy consumption before the network convergence.
* `plot_energyAfter.py`, this script is meant to draw the graphs of the energy consumption after the network convergence.

#### energy_time.py

For all the .txt files:

```bash
python3 energy_time.py <txt file> <csv file>
```

For instance:

```bash
python3 energy_time.py ../data/leaf1_default.txt ../data/leaf1_default.csv
```

#### average.py

For all the .csv files (of the same configuration):

```bash
python3 average.py <1st csv file> <2nd csv file> <3rd csv file> <final csv file>
```

For instance:

```bash
python3 average.py ../data/leaf1_default.csv ../data/leaf2_default.csv ../data/leaf3_default.csv ../data/leaf_default.csv
```

#### plot_time.py

```bash
python3 plot_time.py ../data/leaf_EB2.csv ../data/leaf_HOP1.csv ../data/leaf_EB8.csv ../data/leaf_HOP2.csv ../data/leaf_default.csv ../plots/joiningTime.png
```

#### plot_energy.py

```bash
python3 plot_energy.py ../data/leaf_EB2.csv ../data/leaf_HOP1.csv ../data/leaf_EB8.csv ../data/leaf_HOP2.csv ../data/leaf_default.csv ../data/root_EB2.csv ../data/root_HOP1.csv ../data/root_EB8.csv ../data/root_HOP2.csv ../data/root_default.csv ../plots/energy.png
```

#### plot_energyAfter.py

```bash
python3 plot_energyAfter.py ../data/leaf_EB2.csv ../data/leaf_HOP1.csv ../data/leaf_EB8.csv ../data/leaf_HOP2.csv ../data/leaf_default.csv ../data/root_EB2.csv ../data/root_HOP1.csv ../data/root_EB8.csv ../data/root_HOP2.csv ../data/root_default.csv ../plots/energyAfter.png
```
