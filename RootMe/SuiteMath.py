import requests
# s = requests.session()
# r = s.get("http://challenge01.root-me.org/programmation/ch1/")
#
# div = r.text.split("</iframe>")
#
# recupUn1 = div[1].split("<br />")[0]
# recup2Un1 = recupUn1.split("=")[1]
# recup3Un1 = recup2Un1.replace('<sub>','')
# Un1 = recup3Un1.replace('</sub>','').strip()
# Un1 = Un1.replace('[','(')
# Un1 = Un1.replace(']',')')
#
# recupUn0 = div[1].split("<br />")[1]
# Un0 = recupUn0.split("=")[1].strip()
#
# recupIteration = div[1].split("<br />")[2]
# recup2Iteration = recupIteration.split("<sub>")[1]
# iteration = recup2Iteration.split("</sub>")[0].strip()
#
# p1 = Un1.split(")")
# p1s = p1[0].replace("(","")
# nombreP1 = p1s.split("+")[0]
# nombreP1 = nombreP1.strip()
#
# p2 = Un1.split("(")[2]
# p2s = p2.replace(")","")
# nombreP2 = p2s.split("*")[1]
# nombreP2 = nombreP2.strip()
#
# def u(n):
#     U = int(Un0)
#     for i in range (0,n+1):
#         U =(int(nombreP1)+U)-(i*int(nombreP2))
#     #endfor
#     return U
# #enddef
# res = u(int(iteration))
#
# data = {"result":str(res)}
# reponse = s.get("http://challenge01.root-me.org/programmation/ch1/ep1_v.php", params=data)
#
# print(reponse.url)
# print(reponse.text)
# print(reponse.cookies)
#
# print(r.cookies)

s = requests.session()
response = s.get("http://challenge01.root-me.org/programmation/ch1/")

div = response.text.split("</iframe>")

Un1 = div[1].split("<br />")[0].split("=")[1].replace('<sub>','').replace('</sub>','').strip().replace('[','(').replace(']',')')
Un0 = div[1].split("<br />")[1].split("=")[1].strip()
iteration = div[1].split("<br />")[2].split("<sub>")[1].split("</sub>")[0].strip()

nombreP1 = Un1.split(")")[0].replace("(","").split("+")[0].strip()
nombreP2 = Un1.split("(")[2].replace(")","").split("*")[1].strip()

def u(n):
    U = int(Un0)
    for i in range (0,n):
        U =(int(nombreP1)+U)-(i*int(nombreP2))
    #endfor
    return U
#enddef
res = u(int(iteration))

response2 = s.get('http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=' + str(res))

print(response2.text)