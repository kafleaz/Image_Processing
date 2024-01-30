import cv2
import numpy as np

img= cv2.imread('photo2.jpg')
image= cv2.resize(img,(400, 500))

# cv2.imshow('Original',image)
c1=(255/np.log(1+np.max(img)))
log_transformed1 = c1 * (np.log(img + 1))

c2=(160/np.log(1+np.max(img)))
log_transformed2 = c2 * (np.log(img + 1))

log_transformed1 = np.array(log_transformed1, dtype = np.uint8)
log_transformed2 = np.array(log_transformed2, dtype = np.uint8)

log_transformed1= cv2.resize(log_transformed1,(400, 500))
log_transformed2= cv2.resize(log_transformed2,(400, 500))

both_image = np.hstack([image, log_transformed1, log_transformed2])
# outimage= cv2.resize(log_transformed,(400, 500))
cv2.imshow('Log Transformed',both_image)

cv2.waitKey(0)
cv2.destroyAllWindows()