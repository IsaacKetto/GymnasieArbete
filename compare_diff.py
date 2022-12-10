from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
import math
np.set_printoptions(threshold=sys.maxsize)


orgimg = cv2.imread('brabild.png', cv2.IMREAD_UNCHANGED)
newimg = cv2.imread('nybild.png', cv2.IMREAD_UNCHANGED)

columb = len(orgimg[0])
row = len(orgimg)


def compare_value(newimg, orgimg):
    j = 0
    change = 0
    while j < len(orgimg):
        i = 0
        while i < 4:
            if orgimg[j][i] > newimg[j][i]:
                change += orgimg[j][i] - newimg[j][i]
            else:
                change += newimg[j][i] - orgimg[j][i]
            i += 1
        j += 1    
    return change      
    

def flaten(img, columb, row):
    img = np.reshape(img, ((columb*row), 4))
    return img

def reshape(img, columb, row):
    img = np.reshape(img, (row, columb, 4))
    return img



orgimg = flaten(orgimg, columb,row)
newimg = flaten(newimg, columb,row)
print(compare_value(newimg, orgimg))