import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)

img = Image.open("sverige.png") 
imgData = np.array(img)
print(imgData)


# img = imageToArray(img)
# print(img)
# This method will show image in any image viewer 
# im.show() 