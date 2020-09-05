#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
#Move turtlebot in the shape of D
def my_initial_D():
	rospy.init_node('my_initials', anonymous=True)
	publishing = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	my_msg = Twist()
	my_msg.linear.x = 0
	my_msg.linear.y = 0
	my_msg.linear.z = 0
	my_msg.angular.x = 0
	my_msg.angular.y = 0
	my_msg.angular.z = 0
	rate = rospy.Rate(1)
	actions_list = ["rotateleft","forward","rotateleft","forward", "rotateleft", "forward","littleforward","backward","rotateleft","forward","rotateright","littleforward","None"]
	for action in actions_list:
		if action == "rotateleft" :
			my_msg.linear.x = 0
			my_msg.angular.z = math.pi/2
		elif action == "rotateright" :
			my_msg.linear.x = 0
			my_msg.angular.z = -math.pi/2
		elif action =="littleforward":
			my_msg.linear.x = 1.0
			my_msg.angular.z = 0
		elif action =="forward" :
			my_msg.linear.x = 3.0
			my_msg.angular.z = 0
		elif action =="backward" :
			my_msg.linear.x = -1.0
			my_msg.angular.z = 0
		else:
			my_msg.linear.x = 0
			my_msg.angular.z = 0
		publishing.publish(my_msg)
		rate.sleep()
if __name__ == '__main__':
    try:
        my_initial_D()
    except rospy.ROSInterruptException: pass



