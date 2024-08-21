import cv2
import numpy as np

img = cv2.imread('./image/road.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass

cv2.namedWindow('hsv_image')
cv2.createTrackbar('H low', 'hsv_image',0,255, nothing)
cv2.createTrackbar('H high','hsv_image',0,255, nothing)
cv2.createTrackbar('L low', 'hsv_image',0,255, nothing)
cv2.createTrackbar('L high','hsv_image',0,255, nothing)
cv2.createTrackbar('S low', 'hsv_image',0,255, nothing)
cv2.createTrackbar('S high','hsv_image',0,255, nothing)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

    h_low = cv2.getTrackbarPos('H low', 'hsv_image')
    h_high = cv2.getTrackbarPos('H high','hsv_image')
    s_low = cv2.getTrackbarPos('L low', 'hsv_image')
    s_high = cv2.getTrackbarPos('L high','hsv_image')
    v_low = cv2.getTrackbarPos('S low', 'hsv_image')
    v_high = cv2.getTrackbarPos('S high','hsv_image')
    low_mask = (h_low, s_low, v_low)
    high_mask = (h_high, s_high, v_high)
    hsv_img = cv2.inRange(hsv, low_mask, high_mask)
    cv2.imshow('hsv_image',hsv_img)

cv2.destroyAllWindows()