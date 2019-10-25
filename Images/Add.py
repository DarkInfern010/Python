from PIL import Image
import numpy as np

imgbleu = Image.open("resultatBleu.png")
imgvert = Image.open("resultatVert.png")
imgrouge = Image.open("resultatRouge.png")

def add (img1, img2):
    im1 = np.copy(img1)
    im2 = np.copy(img2)
    res = np.zeros([im1.shape[0], im1.shape[1], 3], dtype=np.uint8)
    for i in range (im1.shape[0]):
        for j in range (im1.shape[1]):
            r1, v1, b1 = im1[i, j]
            r2, v2, b2 = im2[i, j]
            res [i,j] = (r1+r2, v1+v2, b1+b2)
        #endfor
    #endfor
    return res
#enddef

imageCyan = Image.fromarray(add(imgbleu, imgvert))
imageCyan.save("resultatCyan.png")

imageMagenta = Image.fromarray(add(imgbleu, imgrouge))
imageMagenta.save("resultatMagenta.png")

imageJaune = Image.fromarray(add(imgrouge, imgvert))
imageJaune.save("resultatJaune.png")