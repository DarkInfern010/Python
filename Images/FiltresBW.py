from math import ceil

from PIL import Image
import numpy as np

imgpil = Image.open("test.png")
img = np.array(imgpil)

def filtreBW (img_origin, CIE):
    im = np.copy(img_origin)
    for i in range (im.shape[0]):
        for j in range (im.shape[1]):
            r, v, b = im[i,j]
            if (CIE == "709"):
                im[i,j] = (0.2125 * r + 0.7154 * v + 0.0721 * b)
            elif (CIE == "601"):
                im[i,j] = (0.299 * r + 0.587 * v + 0.114 * b)
        #endfor
    #endfor
    return im
#enddef

imgSave709 = Image.fromarray(filtreBW(imgpil, "709"))
imgSave709.save("resultat709.png")

imgSave601 = Image.fromarray(filtreBW(imgpil, "601"))
imgSave601.save("resultat601.png")