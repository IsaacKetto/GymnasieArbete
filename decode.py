from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)

img = cv2.imread('Bild2.png', -1)

retrieved_data = []
j=0
i=0
message_length = 13 #retrieve length with encryption key
for row in img:
    for pixel in row:
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