import cv2
import numpy as np

image = cv2.imread('./image/JackDaniels.jpg')
cv2.imshow('Original_image',image)

# Rotation
(h,w) = image.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated_image = cv2.warpAffine(image,M,(w,h))
cv2.imshow('Rotated_image',rotated_image)

# Resize
size = 300
resized_image = cv2.resize(image,(size,size))
cv2.imshow('Resized_image',resized_image)

# Affine Transform
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
affine_image = cv2.warpAffine(image,M,(w,h))
cv2.imshow('Affine_transformed_image',affine_image)

cv2.waitKey(0)
cv2.destroyAllWindows()