import os

stream = os.popen('tesseract "C:/Users/Louis/Downloads/HackSecuReims2020/hsr_ocr/imgs/image_0000.png" stdout --psm 6 --dpi 70')
output = stream.read()

texte = ""
for i in range (802,902):
     k = ""
     if (i < 10):
         k = "000"+str(i)
     elif (i < 100):
         k = "00"+str(i)
     elif (i < 1000):
         k = "0"+str(i)
     else:
         k = str(i)
     stream = os.popen('tesseract "C:/Users/Louis/Downloads/HackSecuReims2020/hsr_ocr/imgs/image_'+k+'.png" stdout --psm 6 --dpi 70')
     output = stream.read()
     texte += output[0]
     print(texte)
#endfor