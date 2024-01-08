import cv2
import matplotlib.pyplot as plt
img= cv2.imread('gray.png')
image= cv2.resize(img,(400, 500))
cv2.imshow('Original',image)


img_neg = 255-img
image= cv2.resize(img_neg,(400, 500))
cv2.imshow('Negative',image)
cv2.waitKey(0)
cv2.destroyAllWindows()