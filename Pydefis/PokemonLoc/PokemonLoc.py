pokemonsName = []
with open("PokemonLoc.txt", "r") as file:
    for line in file.readlines():
        pokemon = line.strip()
        div = pokemon.split(",")
        nom = div[0]
        pokemonsName.append(nom)
    #endfor
#endwith

compte = {}.fromkeys(set(pokemonsName),0)
for valeur in pokemonsName:
    compte[valeur] += 1
#endfor

print(compte)