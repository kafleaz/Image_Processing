import cv2
import numpy as np

# Read the image (adjust path if needed)
img = cv2.imread('./Image_Processing/open.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (400, 500))

# Get image dimensions
m, n = img.shape

# Define the structuring element
se = [[1, 1],
      [1, 1]]

# Initialize the output images
opened_img = np.zeros([m, n], dtype=np.uint8)
closed_img = np.zeros([m, n], dtype=np.uint8)

# Apply opening (erosion followed by dilation)
for i in range(1, m-1):
    for j in range(1, n-1):
        min_pixel = np.min(img[i-1:i+2, j-1:j+2])
        opened_img[i, j] = min_pixel

for i in range(1, m-1):
    for j in range(1, n-1):
        max_pixel = np.max(opened_img[i-1:i+2, j-1:j+2])
        opened_img[i, j] = max_pixel

# Apply closing (dilation followed by erosion)
for i in range(1, m-1):
    for j in range(1, n-1):
        max_pixel = np.max(img[i-1:i+2, j-1:j+2])
        closed_img[i, j] = max_pixel

for i in range(1, m-1):
    for j in range(1, n-1):
        min_pixel = np.min(closed_img[i-1:i+2, j-1:j+2])
        closed_img[i, j] = min_pixel

# Save the output images
out_image_opened = np.hstack([img, opened_img, closed_img])
# out_image_closed = np.hstack([img, closed_img])
cv2.imshow('Original, Opened and closed Image', out_image_opened)
# cv2.imshow('Original and Closed Image', out_image_closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
