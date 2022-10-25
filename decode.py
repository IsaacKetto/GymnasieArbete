from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
from noise import img

np.set_printoptions(threshold=sys.maxsize)

print(img[0][0][3])

retrieved_data = []
j=0
i=0
message_length = 3 #retrieve length with encryption key
for row in img:
    for pixel in row:
        if (i % 4) == 0:
            if j < message_length:
                retrieved_data.append(pixel[3])
            j += 1
        i += 1

print(retrieved_data)