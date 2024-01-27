#Digital Negative with histogram

import cv2
import matplotlib.pyplot as plt
# Read an image
img_bgr = cv2.imread('./Image_Processing/meroimage.jpg',3)
plt.imshow(img_bgr)
plt.show()
# Histogram plotting of original image
color = ('b', 'g', 'r')
for i, col in enumerate(color): 
    histr = cv2.calcHist([img_bgr],
                         [i], None,
                         [256],
                         [0, 256])    
    plt.plot(histr, color = col)  
    # Limit X - axis to 256
    plt.xlim([0, 256])   
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
# Negate the original image
img_neg = 1 - img_bgr
plt.imshow(img_neg)
plt.show()
# Histogram plotting of
# negative transformed image
color = ('b', 'g', 'r')
for i, col in enumerate(color):
     
    histr = cv2.calcHist([img_neg],
                         [i], None,  
                         [256],
                         [0, 256])
     
    plt.plot(histr, color = col)
    plt.xlim([0, 256])

plt.show()