#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

rospy.init_node('joint4_publisher')

pub1 = rospy.Publisher('/scara/joint1_position_controller/command', Float64, queue_size=1)
pub2 = rospy.Publisher('/scara/joint3_position_controller/command', Float64, queue_size=1)
pub4 = rospy.Publisher('/scara/joint4_position_controller/command', Float64, queue_size=1)

rate = rospy.Rate(10) # 10 Hz

while not rospy.is_shutdown():
    try:
        data = float(input("Enter joint 4 position: "))
    except ValueError:
        print("Invalid input, please enter a floating point number.")
        continue

    msg = Float64()
    msg.data = data
    pub4.publish(msg)
    #pub1.publish(msg)
    #pub2.publish(msg)
    rate.sleep()