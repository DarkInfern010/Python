import requests
import base64

s = requests.session()
response = s.get("http://challenge01.root-me.org/programmation/ch8/")

image64 = response.text.split('base64,')[1].split('" />')[0]
image = base64.b64decode(image64)

print(image)