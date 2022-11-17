import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('Brabild.png',1)
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