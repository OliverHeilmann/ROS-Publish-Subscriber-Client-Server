# Description
'async' folder contains a publisher/ subscriber asynchronous example python code whereas 'sync' contains a server/ client example python code. Note that these should be used in different examples... (think about multithreading and doing separate processes on other threads vs waiting for some response). 

__The most noteworthy work is found in [serverWithPub](https://github.com/OliverHeilmann/ROS-Publish-Subscriber-Client-Server/tree/main/src/serverWithPub) as this leverages both the asynchronous publish/subscrib and synchronous client/server ROS functionalities.__

# Instructions...
In order to make a ROS environment use the following terminal commands.
```text 
mkdir ~/<MY ROS WORKSPACE>

mkdir ~//<MY ROS WORKSPACE>/src

cd ~//<MY ROS WORKSPACE>/src

catkin_init_workspace

#check that catkin has created a file called CMakeLists.txt in src using the ls command:
ls -la

cd ..

catkin_make

cd devel

#this displays contents of a file (not necessary but a useful command)
cat setup.sh

#check everything is working, run the following in separate terminals
sh testWorks.sh
```

User should run the shell scripts contained in the following folders to run the programs. __NOTE: YOU WILL HAVE TO CHANGE THE SOURCE PATHS TO YOUR WORKING DIRECTORY__:
1) async: runMe.sh
2) sync: runMe.sh
3) serverWithPub: runMe.sh

# Installing Ubuntu Virtual Machine on Apple Silicon (And ROS Noetic)
How to setup sharing clipboard and directories:
1. Install UTM from their [website](https://mac.getutm.app) or from the Apple App Store.
1. Follow the UTM [instructions](https://mac.getutm.app/gallery/ubuntu-20-04) on how to setup Ubuntu 20.04. 
2. Find Shared Directory in UTM navigator, choose your directory to share (ensure Ubuntu instance is shut off first).
3. Boot up Ubuntu and run the following commands:
    1. cd ~/Documents && mkdir VMShare && cd VMShare
    2. sudo apt-get install davfs2
    3. sudo mount -t http://127.0.0.1:9843/ davfs ~/Documents/VMShare
    4. sudo nano ~/.bashrc 
    5. echo _UBUNTU-PASSWORD_ | sudo -S mount -t davfs http://127.0.0.1:9843/  ~/Documents/VMShare -o username= _HOST-MACHINE-USERNAME_
4. Install ROS Noetic from their [website](http://wiki.ros.org/noetic/Installation/Ubuntu).