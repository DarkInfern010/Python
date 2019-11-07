from PIL import Image
import numpy as np
from math import *

imgTest = Image.open("test.png")

def test (img, red, green, blue):
    im = np.copy(img)
    for i in range (im.shape[0]):
        for j in range (im.shape[1]):
            r, v, b = im[i, j]
            if (r == red and v == green and b == blue):
                im[i,j] = (0, 0, 0)
            else:
                im[i,j] = (r,v,b)
        #endfor
    #endfor
    return im
#enddef

imageTest = Image.fromarray(test(imgTest, 255, 255, 255))
imageTest.save("resultatTest.png")