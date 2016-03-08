# -*- coding: utf-8 -*-

def fibonacci(n) :
    
    L = [0, 1]
    
    for i in range (2, n) :
        L.append(L[i-1] + L[i-2])
    dico = {}
    for i in range (0, n) :
        dico[L[i]] = i
    return dico


dico = fibonacci(10)
for k,v in dico.items():
    print (k,v)
print(dico)




