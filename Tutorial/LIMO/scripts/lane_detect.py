import cv2
import numpy as np

class Lane_Detector:
    def __init__(self):
        self.white_lower = np.array([0,0,200])
        self.white_upper = np.array([180,25,255])

        self.yellow_lower = np.array([20,100,100])
        self.yellow_upper = np.array([30,255,255])

    ## HSV
    def get_mask(self,image):
        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        white_mask  = cv2.inRange(hsv_image,self.white_lower,self.white_upper)
        yellow_mask = cv2.inRange(hsv_image,self.yellow_lower,self.yellow_upper)

        combined_mask = cv2.bitwise_or(yellow_mask,white_mask)

        return combined_mask

    ## Hough
    def lane_detect(self,image):
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

        return combined_image, lines

    def detect_lines(self,image):

        combined_mask = self.get_mask(image)
        combined_image = cv2.bitwise_and(image,image,mask=combined_mask)

        detected_image, lines = self.lane_detect(combined_image)

        return detected_image, lines
