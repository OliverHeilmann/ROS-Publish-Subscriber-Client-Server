#Run in Linux terminal with 'sh runMe.sh' command
source ~/ros_workspace/devel/setup.sh
gnome-terminal -x sh -c "roscore"
gnome-terminal -x sh -c "python2 service_server.py"
python2 service_client.py "these are some random series of words"
