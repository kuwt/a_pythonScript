####################################################
# Aim: converting exr to png
#
# Author: kuwingto, 11 Dec 2019
# 
# Prerequisite: 
# pip install pypng
# pip install opencv-python
# pip install numpy
# pip install openexr #may need to download external package
# pip install matplotlib
###############################################

import OpenEXR, Imath, numpy
import PIL
from PIL import Image
import png

######### input variable ####################
srcPath = "image0001.exr"
dstPath = "depth0001.png"
scalingFactor = 10000
exrInvalidThd = 50

########## Read exr input #####################
srcExr = OpenEXR.InputFile(srcPath)
pt = Imath.PixelType(Imath.PixelType.FLOAT)
dw = srcExr.header()['dataWindow']
size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
height = size[1]
width = size[0]
redstr = srcExr.channel('R', pt)
red = numpy.fromstring(redstr, dtype = numpy.float32)
red.shape = (height, width) # Numpy arrays are (row, col)

############ Form numpy array #######################
arr=numpy.zeros((height,width),numpy.uint16)
for j in range(height):
    for i in range(width):
        if red[j,i] > exrInvalidThd:
            arr[j,i] = 0
        else:
            arr[j,i] = red[j,i] * scalingFactor

################ png output #####################
z=arr
with open(dstPath, 'wb') as f:
    writer = png.Writer(width=z.shape[1], height=z.shape[0], bitdepth=16, greyscale=True)
    writer.write(f, z.tolist())


