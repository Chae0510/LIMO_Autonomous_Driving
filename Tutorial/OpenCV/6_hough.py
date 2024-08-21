import cv2
import numpy as np

image_path = './image/road.jpg'
image = cv2.imread(image_path)

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
    # _combined_image = cv2.add(image,line_image)
    cv2.imshow('Original_image',image)
    cv2.imshow('Combined_image',combined_image)
    # cv2.imshow('_Combined_image',_combined_image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
else:
    print('There is no lane.')