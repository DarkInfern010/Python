from PIL import Image
import numpy as np

imagePoke1 = Image.open("poke1.png")
imagePoke1np = np.array(imagePoke1)

imagePoke2 = Image.open("poke2.png")
imagePoke2np = np.array(imagePoke2)

def traitement(image1, image2):
    imageNP1 = np.copy(image1)
    imageNP2 = np.copy(image2)

    imageNP1 = imageNP1[:, :, :3]
    imageNP2 = imageNP2[:, :, :3]

    imageRes = np.zeros((imageNP1.shape[0], imageNP1.shape[1], 3), dtype=np.uint8)

    for i in range (imageNP1.shape[0]):
        for j in range (imageNP1.shape[1]):
            r1, v1, b1 = imageNP1[i, j]
            r2, v2, b2 = imageNP2[i, j]
            if (r1 == r2): #Plan vert
                imageRes[i, j] = v1 ^ v2
            else: #Plan Bleu
                imageRes[i, j] = b1 ^ b2
            #endif
        #endfor
    #endfor
    return imageRes
#enddef

imageResult = Image.fromarray(traitement(imagePoke1, imagePoke2))
imageResult.save("resultat.png")