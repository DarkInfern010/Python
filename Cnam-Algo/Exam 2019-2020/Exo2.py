def pow (x,y : int):
    if (y == 0):
        return 1
    else:
        return x * pow(x, y-1)
#enddef
print("La puissance est : "+str(pow(4,16)))