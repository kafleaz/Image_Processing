#contrast stretching
import cv2
import numpy as np

#function
def pixelVal(pix,r1,s1,r2,s2):
    if (0 <= pix and pix <= r1):
        return (s1/r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2-s1)/(r2-r1)) * (pix-r1) + s1
    else:
        return ((255-s2)/(255-r2)) * (pix-r2) + s2

img = cv2.imread('photo2.jpg')
image= cv2.resize(img,(400, 500))
cv2.imshow('Input Image', image)

#parameter
r1 = 70
s1 = 0
r2 = 255
s2 = 255

pixelVal_vec = np.vectorize(pixelVal)

cont_st_img = pixelVal_vec(img, r1, s1, r2, s2)

image= cv2.resize(cont_st_img,(400, 500))
cv2.imshow('Output Image', image)
cv2.waitKey(0)
