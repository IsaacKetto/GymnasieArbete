import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('brabild.png',1)
 
# show image
print(img)
cv2.imshow('image',img)
cv2.waitKey(0)


# img = Image.open("Brabild.png") 
# imgData = np.array(img)


# print(img.format)
# print(img.size)
# print(img.mode)
# print(imgData)


# img = imageToArray(img)
# print(img)
# This method will show image in any image viewer 
# im.show() 