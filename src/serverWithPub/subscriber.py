# Oliver Heilmann 
# sandbox scripting
# SUBSCRIBER

import rospy
import time
import std_msgs
from std_msgs.msg import Int32

print "running subscriber"
time.sleep(3)

def callback(msg):
    print "Subscriber reading: " + str(msg.data)

rospy.init_node('topic_subscriber')

pub = rospy.Subscriber('counter', std_msgs.msg.String, callback) # note that we have to change the expected message type from Int32 to String!

rospy.spin() # essentially a shutdown function