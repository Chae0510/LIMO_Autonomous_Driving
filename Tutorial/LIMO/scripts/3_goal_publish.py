#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

def move_to_goal():
    rospy.init_node('send_goal_node')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map" 
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose = Pose(Point(2.0, 2.0, 0.0), Quaternion(0.0, 0.0, 0.0, 1.0))

    rospy.loginfo("Sending goal location ...")
    client.send_goal(goal)
    client.wait_for_result()

    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("You have reached the goal!")
    else:
        rospy.loginfo("The robot failed to reach the goal.")

if __name__ == '__main__':
    try:
        move_to_goal()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
