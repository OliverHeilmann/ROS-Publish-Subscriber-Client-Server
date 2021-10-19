# Description
'async' folder contains a publisher/ subscriber asynchronous example python code whereas 'sync' contains a server/ client example python code. Note that these should be used in different examples... (think about multithreading and doing separate processes on other threads vs waiting for some response).

# Instructions...
In order to make a ROS environment use the following terminal commands.
```text 
mkdir ~/<MY ROS WORKSPACE>

mkdir ~//<MY ROS WORKSPACE>/src

cd ~//<MY ROS WORKSPACE>/src

catkin_init_workspace

# Check that catkin has created a file called CMakeLists.txt in src using the ls command:
ls -la

cd ..

catkin_make

cd devel

# this displays contents of a file (not necessary but a useful command)
cat setup.sh	
```

User should run the shell scripts contained in the following folders to run the programs:
1) async: runMe.sh
2) sync: runMe.sh
3) serverWithPub: runMe.sh