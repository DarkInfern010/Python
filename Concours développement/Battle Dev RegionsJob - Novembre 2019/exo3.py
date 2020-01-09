# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

nb = input()
d = nb.split(" ")

cableDispo = []
for i in range(1, int(d[0]) + 1):
    cableDispo.append(i)
# endfor

nbRequest = d[1]

dico = {}

res = ""

for i in range(int(nbRequest)):
    date = input().split(" ")
    dateDeb = int(date[0])
    dateFin = int(date[1])

    for j in range(dateDeb, dateFin):
        if (j in dico):
            dico[j] += 1
        else:
            dico[j] = 1
# endfor

for cle, valeur in dico.items():
    if (valeur > len(cableDispo)):
        res = "pas possible"

print(res)