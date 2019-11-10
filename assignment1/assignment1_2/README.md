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

Inside of the base directory `assignment1_2` there are two folders and two files:
* `6TiSCH_stack`, this sub-project contains the files needed for the analysis of the entire 6TiSCH stack.
* `TSCH_MAC_layer`, this sub-project contains the files needed for the analysis of the TSCH MAC layer.
* `plots.xlsx`, this file contains the various plots obtained after the analysis.
* `README.md`, this file contains information about other files in the sub-directories.

Each of these sub-projects contain the following files:

* `Makefile`, this file contains a set of directives used by a make build automation tool to generate a target/goal. This Makefile can define the MODULES variable, a list of modules that should be included. It can also configure the Contiki-NG networking stack.
* `project-conf.h`, this file contains C declarations and macro definitions. It is used to configure the develop environment, the system configuration and the various layers of the stack.
* `assignment1_2.c`, this file contains the class that is meant to be run.
* `data.zip`, this file that contains the data used for the plots.




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

In base of which sub-project you want to run 
In both terminal session we will move to the specific sub-project (in base of which of them we want to run) simply typing:

```bash
cd assignment1/assignment1_2/6TiSCH_stack
```
or
```bash
cd assignment1/assignment1_2/TSCH_MAC_layer
```

Now, only in one terminal session, it is useful saves our settings and after compile the project (nodes can be something like *'/dev/ttyUSB0'* or *'/dev/ttyUSB1'*):
```bash
make TARGET=zoul BOARD=firefly savetarget
make MOTES='<1st node> <2nd node>' assignment1_2.upload
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

- ##### 6TiSCH_stack

  From the shell, you can run TSCH transparently with RPL:

  ```
  > rpl-set-root 1
  Setting as DAG root with prefix fd00::/64
  ```

  Note than whenever a node is set as RPL root, it will automatically become a TSCH coordinator.

- ##### TSCH_MAC_layer

  From the shell, set one node as TSCH coordinator:

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
