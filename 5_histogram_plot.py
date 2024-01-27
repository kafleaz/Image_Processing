# Histogram plot of an image

import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('./Image_Processing/meroimage.jpg')

# Calculate the histogram for each color channel
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)

# Set the range of the x-axis and display the plot
plt.xlim([0, 256])
plt.show()
