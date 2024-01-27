# Digital Negative

import cv2
import numpy as np
img = cv2.imread('./Image_Processing/photo2.jpg')
resimage = cv2.resize(img,(400, 500))
# image = cv2.imshow('My_image',resimage)

# Invert the image using cv2.bitwise_not
img_neg = cv2.bitwise_not(resimage)
outimage= np.hstack([resimage, img_neg])
cv2.imshow('Original&Negative',outimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

