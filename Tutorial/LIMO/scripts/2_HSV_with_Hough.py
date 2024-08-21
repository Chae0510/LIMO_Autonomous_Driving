#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import Int32
from dynamic_reconfigure.server import Server
from limo_application.cfg import image_processingConfig

import cv2
import numpy as np
from lane_detect import Lane_Detector

class ROS_Camera(Lane_Detector,object):
    def __init__(self):
        super(ROS_Camera, self).__init__()
        rospy.init_node("lane_detect_with_HSV_Hough")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.image_topic_callback)
        self.cvbridge = CvBridge()
        self.viz = True

    def image_topic_callback(self, img):
        
        original_image = self.cvbridge.compressed_imgmsg_to_cv2(img, "bgr8")
        detected_image, _ = self.detect_lines(original_image)
        
        if self.viz:
            cv2.imshow("lane_original", detected_image)
            cv2.waitKey(1)
         
            
def run():
    new_class = ROS_Camera()
    rospy.spin()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("program down")
