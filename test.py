import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('Brabild.png', cv2.IMREAD_UNCHANGED)

img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A



#Change value in array
for row in img:
    for pixel in row:
        i = 0
        while i < 4:
            # pixel[3] = 100
            i += 1

print(img[0][1])
print(img[0][0])





# show and save image
# print(img[0][0][3])
# cv2.imwrite("testBild.png", img)
cv2.imshow('image',img)
cv2.waitKey(0)


