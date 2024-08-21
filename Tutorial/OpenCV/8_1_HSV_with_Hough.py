import cv2
import numpy as np

## HSV
def HSV_image(image):
    hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    white_lower = np.array([0,0,200])
    white_upper = np.array([180,25,255])
    white_mask  = cv2.inRange(hsv_image,white_lower,white_upper)

    filtered_image = cv2.bitwise_and(image,image,mask=white_mask)

    return filtered_image

## Hough
def lane_detect(image):
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

image_path = './image/road_camera.jpg'
image = cv2.imread(image_path)

filtered_image = HSV_image(image)
detected_image = lane_detect(filtered_image)

cv2.imshow('Original_image',image)
cv2.imshow('Filtered_image',filtered_image)
cv2.imshow('Detected_image',detected_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()