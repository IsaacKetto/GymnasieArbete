from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
from message_convert import array_with_byte_message

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('brabild.png',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A

#Values for the reshape method
columb = len(img[0])
row = len(img)

#Flatten method
def flaten(img, columb, row):
    img = np.reshape(img, ((columb*row), 4))
    return img

#reshape flattened array method
def reshape(img, columb, row):
    img = np.reshape(img, (row, columb, 4))
    return img

#variable to determine space between affected pixels
space_between_pixels = int((len(img)*len(img[0]))/len(array_with_byte_message))
print(space_between_pixels)
img = flaten(img, columb, row)
i = 0
for pixel in img[::space_between_pixels]:     
    if i < len(array_with_byte_message):
        pixel[3] = array_with_byte_message[i]
        i += 1
img = reshape(img, columb, row)

# show and save image
cv2.imwrite("Bild2.png", img)
cv2.waitKey(0)


