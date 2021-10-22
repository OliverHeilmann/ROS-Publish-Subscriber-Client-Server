#Run in Linux terminal with 'sh runMe.sh' command
source ~/ros_workspace/devel/setup.sh

#init roscore
gnome-terminal -x sh -c "roscore"

#open separate terminals for service_server_pub and the subscriber
gnome-terminal -x sh -c "python2 service_server_pub.py"
gnome-terminal -x sh -c "python2 subscriber.py"

#run simple client request script in current terminal
python2 service_client.py "these are some random series of words"
python2 service_client.py "run the script again with some more words to see if it works again..."
python2 service_client.py "how about numbers and symbols !@#$% 1235..."
