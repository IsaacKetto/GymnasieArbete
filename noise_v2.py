from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
from message_convert import array_with_byte_message

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('brabild.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A

#Values for the reshape method
columb = len(img[0])
row = len(img)

#variable defined for the first pixels that have the value of space_between_pixels_array
spacing_value_pixel_amount = 10

#Flatten method
def flaten(img, columb, row):
    img = np.reshape(img, ((columb*row), 4))
    return img

#reshape flattened array method
def reshape(img, columb, row):
    img = np.reshape(img, (row, columb, 4))
    return img

#variable to determine space between affected pixels
space_between_pixels = int((len(img)*len(img[0]) - spacing_value_pixel_amount)/len(array_with_byte_message))

#Converts space_between_pixels into bytes
space_between_pixels_encoded = bytes(str(space_between_pixels), 'UTF-8')

#append into an array for easier access
space_between_pixels_array = []
for bytes in space_between_pixels_encoded:
    space_between_pixels_array.append(bytes)
    
#encoding algorithm:
img = flaten(img, columb, row)
j = 0
for value in space_between_pixels_array:
    img[j][3] = value
    j += 1
while j < spacing_value_pixel_amount:
    img[j][3] = 0
    j += 1

i = 0
while i < len(array_with_byte_message):
    img[space_between_pixels*i + spacing_value_pixel_amount][3] = array_with_byte_message[i]
    i += 1
# for pixel in img[::space_between_pixels]:     
#     if i < len(array_with_byte_message):
#         pixel[3] = array_with_byte_message[i]
#         i += 1
img = reshape(img, columb, row)
#encoding algorithm ends here

# show and save image
cv2.imwrite("Bild2.png", img)
cv2.waitKey(0)


