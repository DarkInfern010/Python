from PIL import Image
import numpy as np

imgpil = Image.open("test.png")
img = np.array(imgpil)

def filtreNeg (img_origin):
    im = np.copy(img_origin)
    for i in range (im.shape[0]):
        for j in range (im.shape[1]):
            r, v, b = im[i, j]
            im[i, j] = (255-r, 255-v, 255-b)
        #endfor
    #endfor
    return im
#enddef

imgSave = Image.fromarray(filtreNeg(imgpil))
imgSave.save("resultatNeg.png")

