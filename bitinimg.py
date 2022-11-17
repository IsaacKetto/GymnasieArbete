
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
import math
np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('bratestbild.png', cv2.IMREAD_UNCHANGED)
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
        n += str(i)
    return n



def flaten(img, columb, row):
    img = np.reshape(img, ((columb*row), 4))
    return img

def reshape(img, columb, row):
    img = np.reshape(img, (row, columb, 4))
    return img




msg = toBinary("hej")
# msg = "01010"
print(len(msg))
#Change value in array
img = flaten(img, columb,row)

j = 0
for pixel in img:
    i = 0
    while i < 4:
        # print(pixel)
        if j < len(msg):
            print(pixel)
            print(j)
            if pixel[i] % 2 != int(msg[j]):
                print("ändrade något")
                if pixel[i] == 255:
                    pixel[i] = pixel[i]-1
                else:
                    pixel[i] = pixel[i]+1
                print(pixel)
            j += 1
            i += 1
        else:
            break






# show and save image
img = reshape(img, columb, row)
# print(img[0][0])
# print(img[0][1])
# print(img[0][2])
cv2.imwrite("Bild.png", img)
# cv2.imshow('image',img)
cv2.waitKey(0)


