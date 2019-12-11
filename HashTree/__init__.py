from HashTree.HashMap import HashMap

tab = [5,9,10,17,18,24]
hashmap = HashMap(3)

for i in tab:
    hashmap.put(i, "v"+str(i))

for i in tab:
    print(hashmap.get(i).getKey(), end="    ")
    print(hashmap.get(i).getValue())
