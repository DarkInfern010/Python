import math

def CalculP(n):
    P = 1
    for i in range (n):
        P = 2 * P
    #endfor
    return P
#enddef

def CalculB(n):
    B = (1 / math.sqrt(2))
    for i in range (n):
        B = math.sqrt(CalculA(i)*B)
    #endfor
    return B
#endef

def CalculA(n):
    A = 1
    for i in range (n):
        A = (A + CalculB(i)) / 2
    #endfor
    return A
#enddef

def CalculT(n):
    T = 0.25
    for i in range (n):
        T = T - (CalculP(i)*pow((CalculA(i+1) - CalculA(i)),2))
    #endfor
    return T
#endef

def pi (nc: int):
    valeurPi = (pow((CalculA(nc)+CalculB(nc)),2)/(4*CalculT(nc)))
    print(valeurPi)
#endef

pi(10)
