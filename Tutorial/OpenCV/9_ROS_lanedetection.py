#! /usr/bin/env python
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

class LaneDetection:
    def __init__(self):
        rospy.init_node("lane_detect")
        rospy.Subscriber("/camera/rgb/image_raw/compressed", CompressedImage, self.image_topic_callback)
        self.cvbridge = CvBridge()
        self.viz = True
    
    def HSV_image(self, image):
        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        yellow_lower = np.array([20,100,100])
        yellow_upper = np.array([30,255,255])
        yellow_mask  = cv2.inRange(hsv_image,yellow_lower,yellow_upper)

        white_lower = np.array([0,0,200])
        white_upper = np.array([180,25,255])
        white_mask  = cv2.inRange(hsv_image,white_lower,white_upper)

        combined_mask = cv2.bitwise_or(yellow_mask,white_mask)
        filtered_image = cv2.bitwise_and(image,image,mask=combined_mask)

        return filtered_image

    ## Hough
    def lane_detect(self, image):
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image,(5,5),0)
        edge_image = cv2.Canny(blurred_image, 50, 150)

        lines = cv2.HoughLinesP(edge_image,1,np.pi/180,20,minLineLength=30,maxLineGap=200)
        line_image = np.zeros_like(image)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),1)

            combined_image = cv2.addWeighted(image,0.8,line_image, 1, 1)

        else:
            combined_image = image

        return combined_image
    
    def visResult(self):

        cv2.imshow("lane_original", self.original_image)
        cv2.imshow("lane_thresholded", self.combined_image)
        cv2.waitKey(1)
    
    # ==============================================
    #               Callback Functions
    # ==============================================

    def image_topic_callback(self, img):

        self.original_image = self.cvbridge.compressed_imgmsg_to_cv2(img, "bgr8")
        self.filtered_image = self.HSV_image(self.original_image)
        self.combined_image = self.lane_detect(self.filtered_image)
        
        # visualization
        if self.viz:
            self.visResult()
         
            
def run():
    new_class = LaneDetection()
    rospy.spin()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("program down")