import requests
import pgrep
import os
import time

i = 0

while i < 1000:
    openvpn = pgrep.pgrep("openvpn")

    if (len(openvpn) == 0):
        os.system('nohup openpyn uk &')
        time.sleep(10)
        i += 1
        print(i)
    #endif
    else:
        url = "https://www.cnam-grandest.fr/le-cnamathon/431"

        s = requests.sessions()
        response = s.get(url)
        div = response.text.split('ittoken " value="1" name="')
        div1 = div[1].split('"')
        token = div1[0]

        params = {
            "user_rating":5,
            "task":"article.vote",
            "hitcount":0,
            "submit_vote":"val",
            "url":url+"?hitcount=0",
            token:1
        }

        response2 = s.post(url+"?hitcount=0", data=params)
        print(token)
        os.system('sudo kill ' + str(openvpn[0]))
        time.sleep(3)
        i += 1
        print(i)
#endwhile