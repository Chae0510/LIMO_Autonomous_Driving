import cv2
import numpy as np

image_path = './image/road.jpg'
original_image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2HSV)

yellow_lower = np.array([20,100,100])
yellow_upper = np.array([30,255,255])

def yellow_filter(image):
    yellow_mask  = cv2.inRange(hsv_image,yellow_lower,yellow_upper)
    yellow_image = cv2.bitwise_and(image,image,mask=yellow_mask)
    return yellow_image

yellow_image = yellow_filter(original_image)

cv2.imshow('yellow_image',yellow_image)
cv2.imshow('original_image',original_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()