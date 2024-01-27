#Histogram equilization

# import Opencv
import cv2
 
# import Numpy
import numpy as np
 
# read a image using imread
img = cv2.imread('./Image_Processing/Screen.jpg', 0)
img = cv2.resize(img,(400, 500))
# cv2.imshow('input',img)
 
equ = cv2.equalizeHist(img)
 
both_image = np.hstack([img, equ])
cv2.imshow('output',both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()