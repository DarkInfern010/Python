import requests

s = requests.session()
response = s.get("http://167.99.81.99:31746/")

print(response)

response2 = s.get('http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=' + str(res))

print(response2.text)