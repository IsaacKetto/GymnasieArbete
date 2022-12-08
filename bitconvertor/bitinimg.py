
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
import math
np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('brabild.png', cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A
columb = len(img[0])
row = len(img)

def toBinary(a):
    l,m=[],[]
    n = ""
    j = 0
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    for i in m:
        i = str(i)
        while len(i) < 8:
            i = "0" + i 
        n += i
    n += "11111111"
    return n



def flaten(img, columb, row):
    img = np.reshape(img, ((columb*row), 4))
    return img

def reshape(img, columb, row):
    img = np.reshape(img, (row, columb, 4))
    return img





#Change value in array

def change_value(img,msg):
    j = 0
    for pixel in img:
        i = 0
        while i < 4:
            if j < len(msg):
                if pixel[i] % 2 != int(msg[j]):
                    if pixel[i] == 255:
                        pixel[i] = pixel[i]-1
                    else:
                        pixel[i] = pixel[i]+1
                j += 1
                i += 1
            else:
                return img             
    return img

msg = toBinary("hejsan med ää")
img = flaten(img, columb,row)
img = change_value(img,msg)
img = reshape(img, columb, row)
cv2.imwrite("Bild.png", img)
# cv2.imshow('image',img)
cv2.waitKey(0)


