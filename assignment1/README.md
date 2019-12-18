# Assignment 1

Team: 
* Gianluca Puleri
* Simone Monti

----

The source code of the projects is available in this directory (sub-directories).



## Overview of the analyses

We will investigate one of the most popular network stacks that is being used today: IPv6 over the TSCH mode of IEEE 802.15.4e (6TiSCH). 
More specifically, we will focus on the Time-Slotted Channel Hopping (TSCH) Medium Access Control (MAC) layer that is at the basis of 6TiSCH. In order to so, we will use the widely used Zolertia Re-Mote hardware development platform and the Contiki-NG firmware.


There will be 3 different analyses, divided respectively into 3 different folders.

In the first analysis we will analyze the 6TiSCH energy consumption.
In the second analysis, we will analyze the TSCH joining process.
In the last one, we will analyze range capabilities.



## Directories description

We consider the directory `assignment1` as the base directory.
As mentioned before, there are three folders called respectively `assignment1_N`, with N from 2 to 4, present into the base directory. 
All these folders are hierarchically composed by the same two sub-directories, two folders and two files:

* `assignment1_N`
  * `LEAF`
  * `ROOT`
  * `plots`
  * `scripts`
  * `data.zip`
  * `README.md`

Each of these sub-directories contain the following files:

* `Makefile`

* `project-conf.h`

* `assignment1_N.c`

  


## Setup the environment

We will use the Docker image for Contiki-NG on Ubuntu. 
In order to setup this correctly, do as follows:

```bash
sudo apt-get update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker <your-user>
docker pull contiker/contiki-ng
git clone https://github.com/GPuleri/contiki-ng.git
cd contiki-ng
git submodule update --init --recursive
export CNG_PATH=<absolute-path-to-your-contiki-ng>
alias contiker="docker run --privileged --sysctl net.ipv6.conf.all.disable_ipv6=0 --mount type=bind,source=$CNG_PATH,destination=/home/user/contiki-ng -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/bus/usb:/dev/bus/usb -ti contiker/contiki-ng"
```

If you want to install Contiki-NG for other platforms please follow the *Setting up* section at https://github.com/contiki-ng/contiki-ng/wiki.
