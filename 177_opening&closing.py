import cv2
import numpy as np

# Read the image (adjust path if needed)
img = cv2.imread('./Image_Processing/man.jpg', 0)

# Get image dimensions
m, n = img.shape

# Define the 4x4 structuring element
se = [[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]]

# Initialize the output images
opened_img = np.zeros([m, n], dtype=np.uint8)
closed_img = np.zeros([m, n], dtype=np.uint8)

# Apply opening (erosion followed by dilation)
for i in range(2, m-2):
    for j in range(2, n-2):
        min_pixel = np.min(img[i-2:i+2, j-2:j+2])
        opened_img[i, j] = min_pixel

for i in range(2, m-2):
    for j in range(2, n-2):
        max_pixel = np.max(opened_img[i-2:i+2, j-2:j+2])
        opened_img[i, j] = max_pixel

# Apply closing (dilation followed by erosion)
for i in range(2, m-2):
    for j in range(2, n-2):
        max_pixel = np.max(img[i-2:i+2, j-2:j+2])
        closed_img[i, j] = max_pixel

for i in range(2, m-2):
    for j in range(2, n-2):
        min_pixel = np.min(closed_img[i-2:i+2, j-2:j+2])
        closed_img[i, j] = min_pixel

# Save the output images
out_image_opened = np.hstack([img, opened_img])
out_image_closed = np.hstack([img, closed_img])
cv2.imshow('Original and Opened Image', out_image_opened)
cv2.imshow('Original and Closed Image', out_image_closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
