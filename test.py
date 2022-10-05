import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('brabild.png',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A

# show image
print(img)
cv2.imwrite("Bild.png", img)
# cv2.imshow('image',img)
# cv2.waitKey(0)


