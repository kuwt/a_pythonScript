####################################################
# Aim: cannyEdgeDetector
#
# Author:  by kuwingto on Jan 9, 2020
# Prerequisite: 
# pip install opencv-python
# pip install numpy
# pip install matplotlib
###############################################
path = "Cam_0_0.bmp"

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread(path,0)
edges = cv2.Canny(img,30,90)

im = Image.fromarray(edges)
im.save("edge.jpeg")

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
