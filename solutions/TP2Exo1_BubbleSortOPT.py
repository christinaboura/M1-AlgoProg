# -*- coding: utf-8 -*-

import random

def bubblesortOPT(L) :
    ''' Implémentation optimisée du tri à bulles '''
    
    i = len(L) - 1
    swap = True
    while i > 0 and swap : # tant que on a fait au moins un échange lors du dernier passage
        swap = False
        for j in range(i) :
            if L[j] > L[j+1] :
                L[j], L[j+1] = L[j+1], L[j] # j'échange les cases j et j+1
                swap = True # swap vaut True puisque j'ai fait (au moins) un échange
        i -= 1
    return L

L = random.sample(range(0, 100), 15)
print(L)
Ltriee = bubblesortOPT(L)
print(Ltrie)
