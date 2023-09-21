# Conversion of color imge into gray-scale image

import cv2
import numpy
import numpy as np

img= cv2.imread('./Image_Processing/photo2.jpg')
image= cv2.resize(img,(400, 500))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convertion Image into 3 channel for concatenation process
img2 = np.zeros_like(image)
img2[:,:,0] = gray_image
img2[:,:,1] = gray_image
img2[:,:,2] = gray_image

both_image = np.hstack([image, img2])
cv2.imshow('Original&Grayimage',both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Manual Conversion
# from PIL import Image, ImageEnhance

# img = Image.open('./Image_Processing/photo.jpg')
# img_data = img.getdata()

# lst=[]
# for i in img_data:

#     # lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114) ### Rec. 609-7 weights
#     lst.append(i[0]*0.2125+i[1]*0.7174+i[2]*0.0721) ### Rec. 709-6 weights

# new_img = Image.new("L", img.size)
# new_img.putdata(lst)

# new_img.show() 
