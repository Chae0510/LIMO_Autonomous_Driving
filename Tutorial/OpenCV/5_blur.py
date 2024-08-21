import cv2

image = cv2.imread('./image/road.jpg')
cv2.imshow('Original_image',image)

blurred_image = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('Blurred_image',blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()