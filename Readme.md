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

User should run the shell scripts contained in the following folders to run the programs. __NOTE: YOU WILL HAVE TO CHANGE THE SOURCE PATHS TO YOUR WORKING DIRECTORY__s:
1) async: runMe.sh
2) sync: runMe.sh
3) serverWithPub: runMe.sh