#!/usr/bin/env python

import rospy
import time, pdb
import std_msgs
from basics.srv import WordCount, WordCountResponse
from std_msgs.msg import Int32

# Wait for roscore bootup
print "running server/publisher..."
time.sleep(3)

# Initialise ROS parameteres
rospy.init_node('topic_publisher' , 'service_server')
pub = rospy.Publisher('counter', std_msgs.msg.String, queue_size=5) # note that we have to change the expected message type from Int32 to String!
rate = rospy.Rate(2)

# Define count words function request which can be hit by the client
count = 1
def count_words(request):
    global count
    # tell user in consol what is happening
    print "[INFO {}]: client requested service from server".format(count)

    # find number of words
    ans = WordCountResponse(len(request.words.split()))

    # concatenate string for publishing
    pubString = request.words + ' -> ' + str(ans.count)

    # publish command
    pub.publish(pubString)
    
    # update user on status
    print "[INFO {}]: server has published the client request".format(count)
    
    # incriment up for the terminal prints
    count +=1

    return ans # return to client

# Create server servicce instance
service = rospy.Service('word_count', WordCount, count_words)

rospy.spin()