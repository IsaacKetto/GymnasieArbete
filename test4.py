import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)

img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A
columb = len(img[0])
row = len(img)

def flaten(img, columb, row):
    img = np.reshape(img, ((columb*row), 4))
    return img
def reshape(img, columb, row):
    img = np.reshape(img, (row, columb, 4))
    return img
# for row in img:
#     for pixel in row:
#         i = 0
#         while i < 4:
#             # pixel[i] = 100
#             i += 1





# show and save image
# print(img[0][0][3])
# cv2.imwrite("Bild.png", img)
# cv2.imshow('image',img)
cv2.waitKey(0)


