def bataille_de_crepe0(n, marchand1, marchand2):
    Influ1 = 0 + marchand1
    Influ2 = n - marchand2
    if (Influ1 > Influ2): print('1')
    elif (Influ2 > Influ1): print('2')
    elif (Influ1 == Influ2): print('0')
    pass

n = int(input())
marchand1 = int(input())
marchand2 = int(input())
bataille_de_crepe0(n, marchand1, marchand2)

