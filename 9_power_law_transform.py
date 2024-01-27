import cv2
import numpy as np
image= cv2.imread('./Image_processing/photo2.jpg')
image= cv2.resize(image,(400, 500))
# cv2.imshow('Original',image)

gamma1=0.2
gamma2= 3
gamma_corrected1 = np.array(255*(image / 255) ** gamma1, dtype = 'uint8')
gamma_corrected2 = np.array(255*(image / 255) ** gamma2, dtype = 'uint8')
both_image = np.hstack([image, gamma_corrected1, gamma_corrected2])
cv2.imshow('Gamma_corrected value 0.2 & 3',both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()