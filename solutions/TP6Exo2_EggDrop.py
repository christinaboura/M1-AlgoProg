#-*- coding: utf-8 -*-

import time

def eggDrop(n,h):
    if h == 0 or h == 1: #si 0 ou 1 étage, 0 ou 1 lancer nécessaire
        return h
    if n == 1: #si 1 oeuf, k lancers nécessaires
        return h
    q = 4294967296 #2^32-1 considéré comme très grand
    for k in range(1,h+1):
        q = min(q,max(eggDrop(n-1,k-1),eggDrop(n,h-k)))
    return 1+q
    
print(eggDrop(2,10))
t0=time.time()
for i in range(1000):
    eggDrop(2,10)
print(time.time()-t0)

def eggDrop(n,h):
    T = [[0 for i in range(h+1)] for i in range(n+1)]
    
    for i in range(n+1):
        T[i][0] = 0
        T[i][1] = 1
    for j in range(2,h+1):
        T[1][j] = j
        
    for i in range(2, n+1):
        for j in range(1, h+1):
            q = 4294967296 #2^32-1 considéré comme très grand
            for k in range(1,j+1):
                q = min(q,max(T[i-1][k-1],T[i][j-k]))
            T[i][j] = 1+q
    return T[n][h]

print(eggDrop(2,10))
t0=time.time()
for i in range(1000):
    eggDrop(2,10)
print(time.time()-t0)
print(eggDrop(2,36))
