from PIL import Image, ImageFilter, ImageChops
import sys
from cv2 import threshold
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('Bild.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A

changed_data = []
spacing = 4
i = 0
for row in img:
    for pixel in row[::spacing]:
        changed_data.append(pixel[3])
        i += 1
        if i < 11:
            break
        

print(changed_data)


