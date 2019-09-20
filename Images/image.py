from PIL import Image
from numpy import np

imgpil = Image.open("test.png")
img = np.array(imgpil)

print(img.shape) # Taille de l'image
img = img[:,:,:3] # Suppresion du quatrieme plan (alpha)
print(img.shape)

print(img[100,120]) # Affichage d'un pixel
img[100,120] = (56,120,255) # Modification de pixel

def filtres(img_origin, couleur):
    im = np.copy(img_origin) #copie de l'image dans un tableau numpy
    for i in range (im.shape[0]):
        for j in range (im.shape[1]):
            r, v, b = im[i,j]
            if (couleur == "r"):
                im[i,j] = (r,0,0)
            if (couleur == "v"):
                im[i,j] = (0,v,0)
            if (couleur == "b"):
                im[i,j] = (0,0,b)
            #endif
        #endfor
    #endfor
    return im
#enddef

imgsaveR = Image.fromarray(filtres(imgpil, "r"))
imgsaveR.save("resultatRouge.png")

imgsaveV = Image.fromarray(filtres(imgpil, "v"))
imgsaveV.save("resultatVert.png")

imgsaveB = Image.fromarray(filtres(imgpil, "b"))
imgsaveB.save("resultatBleu.png")