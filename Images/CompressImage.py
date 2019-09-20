from math import floor

from PIL import Image
import numpy as np

imgpil = Image.open("test.png")
img = np.array(imgpil)

def compress (img_origin, taille):
    im = np.copy(img_origin)
    res = np.zeros((floor(im.shape[0] / taille), floor(im.shape[1] / taille), 3), dtype=np.uint8)
    for i in range (im.shape[0]):
        for j in range (im.shape[1]):
            if (i % taille == 0):
                r, v, b = im[i, j]
                res[floor(i/taille), floor(j/taille)] = (r,v,b)
        #endfor
    #endfor
    return res
#enddef

imgSave = Image.fromarray(compress(imgpil,2))
imgSave.save("resultatCompress2.png")

imgSave = Image.fromarray(compress(imgpil,4))
imgSave.save("resultatCompress4.png")

