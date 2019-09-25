noms = "ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS " \
       "ERIS EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO " \
       "MAIA METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE " \
       "SELENE THEMIS THETIS TRITON ZEUS"
div = noms.split(" ")
dico = {}

for i in range(len(div)):
    valeur = 0
    for j in range(len(div[i])):
        valeur += ord(div[i][j])-64
    #endfor
    dico[div[i]] = valeur

print(sorted(dico.values()))

for v in sorted(dico.values()):
    print(v, end=' ; ')
    for k in dico.keys():
        if dico[k] == v:
            print(k)
            break;
