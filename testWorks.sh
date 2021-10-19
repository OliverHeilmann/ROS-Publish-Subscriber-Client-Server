#run this to check that everything works as expected
gnome-terminal -x sh -c "roscore"
gnome-terminal -x sh -c "rosrun basics service_server.py"
gnome-terminal -x sh -c "rosrun basics service_client.py"