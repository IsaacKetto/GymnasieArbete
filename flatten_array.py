import numpy as np
from noise_v2 import img

img = img.flatten()

lenghts = len(img)/4
print(lenghts)
lenghts = int(len(img)/4)
img = np.reshape(img, (lenghts, 4))

print(img)