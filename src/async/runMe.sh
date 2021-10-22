#Run in Linux terminal with 'sh runMe.sh' command
source ~/ros_workspace/devel/setup.sh
gnome-terminal -x sh -c "roscore"
gnome-terminal -x sh -c "python2 publisher.py __name:= publisherRenamed.py counter:=/demo/incrimenter"
gnome-terminal -x sh -c "python2 subscriber.py __name:= subscriberRenamed.py counter:=/demo/incrimenter"
#gnome-terminal -x sh -c "rqt_graph"
