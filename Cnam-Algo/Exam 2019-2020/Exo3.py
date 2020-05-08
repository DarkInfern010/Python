def nthroot (A, n : int, cycle : int):
    X = A/2
    for i in range (cycle):
        X = (1/n)*(((n-1)*X)+(A/(pow(X,n-1))))
    #endfor
    return X
#enddef
print("La racine 3 de 16 est : "+str(nthroot(16, 3, 100)))