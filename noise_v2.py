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

#variable to determine space between affected pixels
space_between_pixels = (len(img)*len(img[0]))/len(array_with_byte_message)

#function to retrieve pos for each pixel for every spacing amount using the spacing variable
# def pixels_to_change(spacing):
#     pixels = []
#     i = 0
#     row = 0
#     if len(img[0])*(row+1) <= spacing/(row+1):
        

#Change value in array

    # affected_pixels = pixels_to_change(space_between_pixels)
j = 0
i = 0
for row in img:
    for pixel in row:     
        if (j % space_between_pixels) == 0:
            if i < len(array_with_byte_message):
                pixel[3] = array_with_byte_message[i]
                i += 1
                print(j)
        j += 1


# show and save image
# print(img[0][0][3])
cv2.imwrite("Bild2.png", img)
# cv2.imshow('image', (cv2.imread('Bild.png',1)))
cv2.waitKey(0)


