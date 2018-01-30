# -*- coding: utf-8 -*-

def dichotomie(v, L) :
    ''' Recherche dichotomique non-récursive '''
    a = 0
    b = len(L) - 1
    m = (a + b) // 2 # l'indice se trouvant à la moitié de la liste

    while a < b : # tant que mon champ de recherche [a,b] ne se réduit pas à un seul élément
        if v == L[m] :
            return m
        elif v > L[m] :
            a = m + 1
        else :
            b = m - 1
        m = (a + b) // 2;
    return -1 # si l'élément n'est pas dans la liste

L = [1, 2, 4, 8, 9, 10, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 30]
v = 15

# i est la position de la liste où se trouve l'élement v
i = dichotomie(v, L)
print(i)
