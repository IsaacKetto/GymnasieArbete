from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
from message_convert import array_with_byte_message

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('brabild.png',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A

#variable to close an infinite loop
finished = False

print(len(array_with_byte_message))

#Change value in array
while finished == False:
    i = 0
    for row in img:
        for pixel in row[::4]:
            if i < len(array_with_byte_message):
                pixel[3] = array_with_byte_message[i]
                i += 1
                print(pixel)
            elif i >= len(array_with_byte_message):
                finished = True


# show and save image
# print(img[0][0][3])

cv2.imwrite("Bild.png", img)
cv2.imshow('image', (cv2.imread('Bild.png',1)))
cv2.waitKey(0)


