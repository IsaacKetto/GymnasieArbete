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

def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

img = import_img("bild.png")
msg = contvert_to_binary(img)
msg = toString(msg)

print(msg)