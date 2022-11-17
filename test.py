import imghdr
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2

np.set_printoptions(threshold=sys.maxsize)


img = cv2.imread('bratestbild.png', cv2.IMREAD_UNCHANGED)

img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
#Datan visas i B G R A



#Change value in array
for row in img:
    for pixel in row:
        i = 0
        while i < 4:
            # pixel[3] = 100
            i += 1

# print(img[0][1])
# print(img[0][0])
print(img)



# j = 0
# for row in img:
#     for pixel in row:
#         while j < len(msg):
#             i = 0
#             while i < 4:
#                 if pixel[i] % 2 != int(msg[j]):
#                     if pixel[i] == 255:
#                         pixel[i] = pixel[i]-1
#                     else:
#                         pixel[i] = pixel[i]+1
#                 j += 1
#                 i += 1



# show and save image
# print(img[0][0][3])
# img = np.array([[[11, 11, 11, 11],[12, 12, 12, 12,],[13,13,13,13]],[[21, 21, 21, 21],[22, 22, 22, 22],[23, 23, 23, 23]]])
# cv2.imwrite("bratestBild.png", img)
cv2.imshow('image',img)
cv2.waitKey(0)


