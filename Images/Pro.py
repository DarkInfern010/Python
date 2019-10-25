from PIL import Image
import numpy as np
from math import *

imgbleu = Image.open("resultatBleu.png")
imgvert = Image.open("resultatVert.png")
imgrouge = Image.open("resultatRouge.png")

def produit (img1, img2):
    im1 = np.copy(img1)
    im2 = np.copy(img2)
    res = np.zeros([im1.shape[0], im1.shape[1], 3], dtype=np.uint8)
    for i in range (im1.shape[0]):
        for j in range (im1.shape[1]):
            r1, v1, b1 = im1[i, j]
            r2, v2, b2 = im2[i, j]

            r = 0 if r1==0 else int(floor(r2/r1)) if r2==0 else int(floor(r1/r2)) if r1==0 else r1/r2 if r1 >= r2 else r2/r1
            v = 0 if v1==0 else int(floor(v2/v1)) if v2==0 else int(floor(v1/v2)) if v1==0 else v1/v2 if v1 >= v2 else v2/v1
            b = 0 if b1==0 else int(floor(b2/b1)) if b2==0 else int(floor(b1/b2)) if b1==0 else b1/b2 if b1 >= b2 else b2/b1

            #if (r2 == 0):
            #    r = 0 if r1==0 else int(floor(r2/r1))
            #else:
            #    r = int(floor(r1/r2)) if r1==0 else r1/r2 if r1 >= r2 else r2/r1
            #    if (r1 == 0):
            #        r = int(floor(r1/r2))
            #    else:
            #        r = r1/r2 if r1 >= r2 else r2/r1

            res [i,j] = (r, v, b)
        #endfor
    #endfor
    return res
#enddef

imageTest = Image.fromarray(produit(imgbleu, imgvert))
imageTest.save("resultatTest.png")