import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys 
import cv2

np.set_printoptions(threshold=sys.maxsize)
img = mpimg.imread("C:\\Users\\Melker\\OneDrive\\Documents\\GitHub\\GymnasieArbete\\Brabild.png")
print(img[0][0])

mpimg.imsave("hej", img)
