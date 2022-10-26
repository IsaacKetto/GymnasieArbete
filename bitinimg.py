import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
import math
np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('brabild.png',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A


def toBinary(a):

    l,m=[],[]
    j = 0
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


msg = toBinary("Hejsan ")
print(msg)
#Change value in array
l = []
for row in img:
    for pixel in row:
        i = 0
        while i < 4:
            if pixel[i] % 2:
                l.append(0)
            else:
                l.append(1)
            i += 1

# k = 0
# for k in l:
# print(145%2)


# print(l)





# show and save image
# print(img[0][0][3])
# cv2.imwrite("Bild.png", img)
cv2.imshow('image',img)
cv2.waitKey(0)


