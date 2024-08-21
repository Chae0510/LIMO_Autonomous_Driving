import cv2

image = cv2.imread('./image/JackDaniels.jpg')
edge_image = cv2.Canny(image,50,300)
image_with_edge = image.copy()

contours, hierarchy = cv2.findContours(edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image_with_edge,contours,-1,(0,255,0),1)

cv2.imshow("Image", image)
cv2.imshow("Edge_image", edge_image)
cv2.imshow("Image_with_edge", image_with_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()