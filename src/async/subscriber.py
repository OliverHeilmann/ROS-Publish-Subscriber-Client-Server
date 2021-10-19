# Oliver Heilmann 
# sandbox scripting
# SUBSCRIBER

import rospy
import time

from std_msgs.msg import Int32

print "running subscriber"
time.sleep(3)

def callback(msg):
    print "Subscriber reading: " + str(msg.data)

rospy.init_node('topic_subscriber')

pub = rospy.Subscriber('counter', Int32, callback)

rospy.spin() # essentially a shutdown function