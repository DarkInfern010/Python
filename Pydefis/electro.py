import requests

code = "03fCF23cfE"
for i in range (200):
	co = requests.get('https://callicode.fr/pydefis/UrlElectro/code/'+code).text
	url = co.split('code/')
	code1 = url[-1]
	code1 = code1.split(' ')
	code = code1[0]
	print (str(i) + " : " + co)
#endfor