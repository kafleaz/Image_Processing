# Implementation of minimum filtering

import cv2
import numpy as np

img = cv2.imread('./Image_Processing/photo2.jpg')
image = cv2.resize(img,(400, 500))

# Creating a 5*5 kernel
kernel = np.ones((3,3),np.uint8)

# Minimum filtering
min_image = cv2.erode(image,kernel,iterations = 1)

outimage = np.hstack([image, min_image])
cv2.imshow('Original and min image',outimage)

cv2.waitKey(0)
cv2.destroyAllWindows()