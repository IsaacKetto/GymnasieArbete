from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
from noise_v2 import flaten, reshape

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('Bild2.png', cv2.IMREAD_UNCHANGED)

columb = len(img[0])
row = len(img)

amount_of_value_pixels = 10 #Value that needs to be known before decoding

#Flattens the img pixel array for easier navigation
img = flaten(img, columb, row)

#function that retrieves the value from the first pixels that determines spacing between pixels
def spacingValuePixels(img):
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
i=0
value_spacing = spacingValuePixels(img)
while (i*value_spacing + amount_of_value_pixels) < len(img):
    if img[i*value_spacing + amount_of_value_pixels][3] == 255: #Checking if pixel is unchanged. If changed, the value of alpha channel will not be 255 (UTF-8 bytes doesn't have 255)
        break
    else:
        retrieved_data.append(img[i*value_spacing + amount_of_value_pixels][3])
        i += 1

decoded_message = ""

for bytes in retrieved_data:
    decoded_message += str(bytes, encoding='UTF-8', errors='strict')

print(decoded_message)