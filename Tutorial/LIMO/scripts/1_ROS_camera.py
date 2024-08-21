#!/usr/bin/env python
# -*- coding: utf-8 -*-
# limo_application/scripts/lane_detection/lane_detect.py
# WeGo LIMO Pro를 이용한 차선 인식 코드

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import Int32
from dynamic_reconfigure.server import Server
from limo_application.cfg import image_processingConfig

import cv2
import numpy as np

class ROS_Camera(object):
    def __init__(self):
        rospy.init_node("ros_camera_sub_node")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.image_topic_callback)
        self.cvbridge = CvBridge()
        self.viz = True

    def image_topic_callback(self, img):

        self.original_image = self.cvbridge.compressed_imgmsg_to_cv2(img, "bgr8")
        
        cv2.imshow("lane_original", self.original_image)
        cv2.waitKey(1)
         
            
def run():
    new_class = ROS_Camera()
    rospy.spin()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("program down")
