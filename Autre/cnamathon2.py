import requests

URL = "https://www.cnam-grandest.fr/le-cnamathon/440"

s = requests.session()
response = s.get(URL)

div = response.text.split('ittoken" value="1" name="')

token = div[1].split('"')
params = {
"user_rating":5,
"task":"article.vote",
"hitcount":0,
"submit_vote":"val",
"url":URL+"?hitcount=0",
str(token[0]):1
}

response2 = s.post(URL+'?hitcount=0',data=params)

print(response2)
#requests.post(url, params=params, json=data)