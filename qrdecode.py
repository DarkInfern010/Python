from PIL import Image
from PIL import GifImagePlugin
import qrtools
import os

imageObject = Image.open("qrcode.gif")
print(imageObject.is_animated)
print(imageObject.n_frames)

for frame in range(0,imageObject.n_frames):
    imageObject.seek(frame)
    if (frame < 10):
    	imageObject.save('gif/test00'+str(frame)+'.png')
    elif (frame < 100):
		imageObject.save('gif/test0'+str(frame)+'.png')
    else:
		imageObject.save('gif/test'+str(frame)+'.png')

liste = []

for i in range (len(os.listdir("gif/"))):
	qr = qrtools.QR()
	if (i < 10):
		qr.decode("gif/test00"+str(i)+'.png')
		print("gif/test00"+str(i)+'.png')
	elif (i < 100):
		qr.decode("gif/test0"+str(i)+'.png')
		print("gif/test0"+str(i)+'.png')
	else:
		qr.decode("gif/test"+str(i)+'.png')
		print("gif/test"+str(i)+'.png')
	liste.append(qr.data)
chaine = "".join(liste)

print(chaine)



