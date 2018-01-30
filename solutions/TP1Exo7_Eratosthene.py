# -*- coding: utf-8 -*-

from math import sqrt

def Eratosthene(N) :
    '''Idée de cet algo : au départ la liste est L = [0,0,2,3,4,...,N-1,N]. Ainsi,
    si L[i] est différent de 0, il y a égalité entre i et L[i]. Chaque fois
    qu'un nombre i est composé on pose L[i] = 0. À la fin de l'algorithme les
    seuls éléments non nuls de la liste, sont les nombres premiers.'''
    
    # on crée une liste L contenant (0,0) puis tous les nombres de 2 à N
    L = [0,0] + [i for i in range(2,N+1)]

    s=sqrt(N)
    i=2
    while i <= s :
        if L[i] != 0 :
            p = L[i] # p représente le premier entier non-nul
            j=2*p;
            while j < N+1 : # on enlève tous les multiples de p
                L[j] = 0
                j += p
        i += 1;
        
    # On imprime les éléments non-nuls de la liste, qui sont exactement les nombres premiers.
    for i in L :
        if L[i] != 0 :
            print(i)

Eratosthene(100)
