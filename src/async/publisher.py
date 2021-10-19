# Oliver Heilmann 
# sandbox scripting
# PUBLISHER

import rospy
import time

from std_msgs.msg import Int32

print "running publisher..."
time.sleep(3)

rospy.init_node('topic_publisher')

pub = rospy.Publisher('counter', Int32, queue_size=2)

rate = rospy.Rate(2)

count = 0
while not rospy.is_shutdown():
    pub.publish(count)
    count +=1
    print "Publisher publishing: " + str(count)
    rate.sleep()