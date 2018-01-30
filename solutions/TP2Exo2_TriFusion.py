# -*- coding: utf-8 -*-

import random

def fusion(L,R) :
    ''' Fonction qui fusionne deux tableaux triés en un unique tableau trié '''
    T = []
    n = len(L)
    m = len(R)
    i = 0
    j = 0
    while i < len(L) and j < len(R) : # on continue tant que les deux listes ne sont pas vides
        if L[i] < R[j] :
            T.append(L[i])
            i = i + 1
        else :
            T.append(R[j])
            j = j + 1
    if i == len(L) :
        for j in range(j,len(R)) :
            T.append(R[j])
    else :
        for j in range(i,len(L)) :
            T.append(L[i])
    return T

def triFusion(T) : 
    n = len(T)
    if n <= 1 :
        return T
    m = n // 2
    return fusion( triFusion(T[0:m]) , triFusion(T[m:n]) )

L = random.sample(range(0, 10000), 30) # generation de 30 nombres aleatoires de 0 a 9999
print(L)
Ltriee = triFusion(L)
print(Ltrie)
