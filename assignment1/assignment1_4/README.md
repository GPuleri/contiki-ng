# Assignment 1_4 - Analysing range capabilities

Team: 
* Gianluca Puleri
* Simone Monti

----

The source code of the project is available in this directory.




## Overview of the analysis

We will research the range capabilities in terms of latency, throughput and energy
consumption (i.e., Joule and kbits/Joule) of the Zolertia Re-Motes using the TSCH MAC
layer. We disable the 6TiSCH stack and set up a TSCH network for the two nodes. We
statically allocate one dedicated cell in the TSCH schedule for the leaf node to the root.
This cell will be used to send one packet per second: 1 meter, 10 meters, 50 meters and
100 meters. Our report includes a satellite photo showing the different measurement positions of the leaf (and root) node. Subsequently, we repeat this analysis with a smaller and larger TX power value. We will explain how the different metrics are affected by varying the distance. 




## Directories description

The base directory is `assignment1_4`, it contains the files needed for the third analysis.
Inside of it we find the following sub-directories and files: 

* `LEAF`, this directory contains all the files needed to run the leaf node.
* `ROOT`, this directory contains all the files needed to run the root node.
* `plots`, this folder contains the various plots obtained by the scripts.
* `scripts`, this folder contains the various scripts used to obtain the plots.
* `data.zip`, this file that contains the data used for the plots.
* `README.md`, this file contains information about other files in the sub-directories.

Each of these sub-directories contain the following files:

* `Makefile`, this file contains a set of directives used by a make build automation tool to generate a target/goal. This Makefile can define the MODULES variable, a list of modules that should be included. It can also configure the Contiki-NG networking stack.
* `project-conf.h`, this file contains C declarations and macro definitions. It is used to configure the develop environment, the system configuration and the TSCH layer.
* `assignment1_4.c`, this file contains the class that is meant to be run.





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
cd assignment1/assignment1_4
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
make MOTES='<1st node>' or '<2nd node>' assignment1_4.upload
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

Here we have 9 files:

* `retrieveLeaf.py`, this script is meant to retrieve data of the leaves from the .txt files and convert them into a .csv files.
* `retrieveRoot.py`, this script is meant to retrieve data of the roots from the .txt files and convert them into a .csv files.
* `averageLeaf.py`, this script is meant to make the average among the three .csv files of the leaves.
* `averageSamefile.py`, this script is meant to make the average among the various data present in the same .csv file (useful only for roots).
* `averageRoot.py`, this script is meant to make the average among the three .csv files of the roots.
* `plot_energy.py`, this script is meant to draw the graphs of the energy consumption.
* `plot_kbit_joule.py`, this script is meant to draw the graphs of the kbit/Joule.
* `plot_latency.py`, this script is meant to draw the graphs of the latency.
* `plot_throughput.py`, this script is meant to draw the graphs of the throughput.

#### retrieveLeaf.py

For all the .txt files:

```bash
python3 retrieveLeaf.py <txt file> <csv file>
```

For instance:

```bash
python3 retrieveLeaf.py ../data/1m_normal/leaf1.txt ../data/1m_normal/leaf1.csv
```

#### retrieveRoot.py

For all the .txt files:

```bash
python3 retrieveRoot.py <txt file> <csv file>
```

For instance:

```bash
python3 retrieveRoot.py ../data/1m_normal/root1.txt ../data/1m_normal/root1.csv
```

#### averageLeaf.py

For all the .csv leaves files (of the same configuration):

```bash
python3 averageLeaf.py <1st csv file> <2nd csv file> <3rd csv file> <final csv file>
```

For instance:

```bash
python3 averageLeaf.py ../data/1m_normal/leaf1.csv ../data/1m_normal/leaf2.csv ../data/1m_normal/leaf3.csv ../data/1m_normal/leaf.csv
```

#### averageSamefile.py

For all the .csv root files:

```bash
python3 averageSamefile.py <csv file> <final csv file>
```

For instance:

```bash
python3 averageSamefile.py ../data/1m_normal/root1.csv ../data/1m_normal/root1_av.csv
```

#### averageRoot.py

For all the .csv root files (of the same configuration):

```bash
python3 averageRoot.py <1st csv file> <2nd csv file> <3rd csv file> <final csv file>
```

For instance:

```bash
python3 averageRoot.py ../data/1m_normal/root1.csv ../data/1m_normal/root2.csv ../data/1m_normal/root3.csv ../data/1m_normal/root.csv
```

#### plot_energy.py

```bash
python3 plot_energy.py ../data/1m_less/leaf.csv ../data/1m_normal/leaf.csv ../data/1m_more/leaf.csv ../data/1m_less/root.csv ../data/1m_normal/root.csv ../data/1m_more/root.csv ../plots/energy.png
```

#### plot_kbit_joule.py

```bash
python3 plot_kbit_joule.py ../data/1m_less/root.csv ../data/1m_normal/root.csv ../data/1m_more/root.csv ../plots/kbit_joule.png
```

#### plot_latency.py

```bash
python3 plot_latency.py ../data/1m_less/root.csv ../data/1m_normal/root.csv ../data/1m_more/root.csv ../plots/latency.png
```

#### plot_throughput.py

```bash
python3 plot_throughput.py ../data/1m_less/root.csv ../data/1m_normal/root.csv ../data/1m_more/root.csv ../plots/throughput.png
```
