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
100 meters. Our report includes a satellite photo showing the different measurement positions of the leaf (and root) node. We will explain how the different metrics are affected by varying the distance.




## Directories description

The base directory is `assignment1_4`, it contains the files needed for the first analysis.
Inside of it we find the following files:

* `Makefile`, this file contains a set of directives used by a make build automation tool to generate a target/goal. This Makefile can define the MODULES variable, a list of modules that should be included. It can also configure the Contiki-NG networking stack.
* `README.md`, this file contains information about other files in the directory.
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
Now, only in one terminal session, it is useful saves our settings and after compile the project (nodes can be something like *'/dev/ttyUSB0'* or *'/dev/ttyUSB1'*):

```bash
make TARGET=zoul BOARD=firefly savetarget
make MOTES='<1st node> <2nd node>' assignment1_4.upload
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

From the shell, set one node as coordinator:

```
> tsch-set-coordinator 1
Setting as TSCH coordinator (non-secured)
```

The node will create a TSCH network and start advertising it through Enhanced Beacons (EBs). 
The other node should be scanning on all active channels. Once it receives an EB, it should join the network.

On the other node, type `tsch-status` to check if the node has joined the network yet:

```
> tsch-status
TSCH status:
-- Is coordinator: 0
-- Is associated: 1
-- PAN ID: 0xabcd
-- Is PAN secured: 0
-- Join priority: 1
-- Time source: 0012.4b00.1932.e30b
-- Last synchronized: 3 seconds ago
-- Drift w.r.t. coordinator: 4 ppm
```
