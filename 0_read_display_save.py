# Write a program to read, save and display an image
import cv2
import numpy as np

# read image
img= cv2.imread('./Image_Processing/photo2.jpg')

image= cv2.resize(img,(400, 500))

outimage= cv2.imshow('MyImage',image)
# save image
cv2.imwrite('./Image_Processing/0_saved_img.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
