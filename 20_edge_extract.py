# Program to extract edge of an Image

import cv2
import numpy as np 

# Load the image
image = cv2.imread('./Image_Processing/photo2.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(400, 500))

# Apply Gaussian blur to the image
# image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the original image and the edges side by side
output = np.hstack([image, edges])

cv2.imshow('Original Image and Edges', output)

# Wait for a key press and then close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
