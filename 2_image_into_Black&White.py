import cv2
import numpy as np

img= cv2.imread('./Image_Processing/photo2.jpg')
img = cv2.resize(img,(400, 500))

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, bimage1) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

(thresh, bimage2) = cv2.threshold(image, 150, 200, cv2.THRESH_BINARY)

both_image = np.hstack([image, bimage1, bimage2])

cv2.imshow('Black&White_image_with_different_threshold_values',both_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()