
from PIL import Image, ImageFilter, ImageChops
import sys 
import numpy as np
import cv2
import math
np.set_printoptions(threshold=sys.maxsize)

def import_img(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    img = img.flatten()
    return img

def toBinary(a):
    l,m=[],[]
    n = ""
    j = 0
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    for i in m:
        i = str(i)
        while len(i) < 8:
            i = "0" + i 
        n += i
    n += "11111111"
    return n

def contvert_to_binary(img):
    i = 0
    msg = []
    j = 0
    msg_temp = ""
    while i < len(img):     
        if j < 8:
            # print(img[i])
            
            if img[i] % 2 == 0:
                msg_temp += "0"
            else:
                msg_temp += "1"
            i +=1
            j += 1
        else:
          if msg_temp == "11111111":
            break
          else:
            msg.append(int(msg_temp))
            msg_temp = ""
            j = 0
    # msg.append(int(msg_temp))
    return msg

msg = (toBinary(" "))

while msg[0] != "1":
    msg = msg.replace('0', '', 1)

print(msg)   
img = import_img("bild.png")
msg = contvert_to_binary(img)

print(msg)