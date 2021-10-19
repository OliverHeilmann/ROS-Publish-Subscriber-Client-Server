#!/usr/bin/env python

import rospy

from basics.srv import WordCount,WordCountResponse

import time

time.sleep(3)

def count_words(request):
    print "Client has requested a calculation..."
    return WordCountResponse(len(request.words.split()))


rospy.init_node('service_server')

service = rospy.Service('word_count', WordCount, count_words)

rospy.spin()

