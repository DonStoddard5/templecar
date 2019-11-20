#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from rpiHAT import ServoNT


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.data)
    global s
    s.pulse(data.data)


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("carcontrol", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    s = ServoNT(channel = 1, freq = 98.1)
    listener()