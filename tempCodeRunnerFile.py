import cv2
import numpy as np

# Read the image (adjust path if needed)
img = cv2.imread('./Image_Processing/man.jpg', 0)

# Define the structuring element
se = np.ones((5,5), np.uint8)

# Apply opening operation (erosion followed by dilation)
opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, se)

# Apply closing operation (dilation followed by erosion)
closed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, se)

# Display the images
out_image=np.hstack([img, opened_img, closed_img])
cv2.imshow('Original, Opened, and Closed Image', out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
