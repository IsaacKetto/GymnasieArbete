from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
from noise_v2 import flaten, reshape

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('Bild2.png', -1)

columb = len(img[0])
row = len(img)

#Flattens the img pixel array for easier navigation
img = flaten(img, columb, row)

#function that retrieves the value from the first pixels that determines spacing between pixels
def spacingValuePixels(img):
    amount_of_value_pixels = 10 #Value that needs to be known before decoding
    space_between_pixels = ""
    retrieved_values = []
    i = 0
    while i < amount_of_value_pixels:
        if img[i][3] == 0:
            break
        else:
            retrieved_values.append(img[i][3])
            i += 1
    for value in retrieved_values:
        space_between_pixels += str(value, encoding='UTF-8', errors='strict')
    return int(space_between_pixels)

retrieved_data = []
j=0
i=0
value_spacing = spacingValuePixels(img)
for pixel in img:
    if (i % 4) == 0:
        if j < message_length:
            retrieved_data.append(pixel[3])
        j += 1
    i += 1

print(retrieved_data)

decoded_message = ""

for bytes in retrieved_data:
    decoded_message += str(bytes, encoding='UTF-8', errors='strict')

print(decoded_message)