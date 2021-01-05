import os

# Suppression du fichier résultat pour pas réécrire dedans
os.remove("flag.txt")

# String Cypher à déchiffrer
c = [358054299396778, 338303820719731, 575163265381617, 426756492371444, 512808963720303, 202722428784490, 12973247620172, 401044612595398, 121188708737752, 296367799892003, 321201931522255, 121188708737752, 401044612595398, 213898535689643, 121188708737752, 296367799892003, 401044612595398, 512808963720303, 296367799892003, 121188708737752, 401044612595398, 121188708737752, 551732685650248, 24272724667960, 4562349440334, 213898535689643, 551732685650248, 401044612595398, 53502040441064, 228350651363859]
# Parcour de tout les caractères pour uncypher avec le tools RsaCtfTool et le mettre dans un fichier flag.txt
for i in range (len(c)):
    os.system('/Users/louis/Downloads/RsaCtfTool-master/RsaCtfTool.py -n 627585038806247 -e 65537 --uncipher ' + str(c[i]) + ' --output flag.txt')

# Ouverture du fichier en lecture
f = open("flag.txt", "r")
a = f.read()
flag = ""

# Parcourt du fichier pour récupérer le flag
for i in range (len(a)):
    if (a[i].isprintable()):
        flag += a[i]

# Affichage du flag et suppression du fichier
print(flag)
os.remove("flag.txt")
