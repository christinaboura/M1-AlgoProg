# -*- coding: utf-8 -*-

from math import sqrt, ceil


def Eratosthene (N) :
    '''Idée de cet algo : Au départ la liste est L = [0,0,2,3,4,...,N-1,N]. Ainsi, si L[i] est different de 0, il       y a égalité entre i et L[i]. Chaque fois qu'un nombre i est composé on pose L[i] = 0. A la fin de l algorithme les seuls éléments non nuls de la liste, sont les nombres premiers.'''
    
    L = [0,0] + [i for i in range(2,N+1)] # on crée une liste L contenant (0,0) puis tous les nombres de 2 à N
    
    for i in range(2,ceil(sqrt(N))) : #  2 <= i <= sqrt(N)
        if L[i] != 0 :
            p = L[i] # p represent le premier entier non-nul
            for j in range(p+1, N+1) : # parcours de tous les nombres supérieurs à p
                if j % p == 0 : # on teste si j est un multiple de p. Si c'est le cas, j n'est pas un nombre premier
                    L[j] = 0

    # On imprime les éléments non-nuls de la liste, qui sont exactement les nombres premiers.
    for i in L :
        if L[i] != 0 :
            print(i)

Eratosthene(100)
