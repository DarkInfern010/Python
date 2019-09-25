nbtete = 8542
coupsHercule = 0

while (nbtete != 1):
    nbtete = nbtete / 2
    if (nbtete % 2 != 0 and nbtete != 1):
        nbtete = (nbtete * 3) + 1
    coupsHercule += 1
#endwhile

coupsHercule += 1
print(coupsHercule)