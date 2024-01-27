#
import cv2
import numpy as np
import matplotlib.pyplot as plt
img= cv2.imread('./Image_Processing/gray.png')
image= cv2.resize(img,(400, 500))
# cv2.imshow('Original',image)


img_neg = 255-img
outimage= cv2.resize(img_neg,(400, 500))
both_image = np.hstack([image, outimage])
cv2.imshow('Negative',both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()