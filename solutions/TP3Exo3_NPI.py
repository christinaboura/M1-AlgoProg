# -*- coding: utf-8 -*-

def estOperateur(c) :
    '''fonction qui renvoie True si c est égal à un des quatre opérateurs et False sinon'''
    if c == '+' or c == '-' or c == '*' or c == '/' :
        return True
    else :
        return False

def calcul(op, n, m) :
    '''fonction renvoyant le resultat n op m'''
    if op == '+' :
        return n + m
    elif op == '-' :
        return n - m
    elif op == '*' :
        return n * m
    elif op == '/' :
        return n / m

def evaluation(s) :
    '''évaluation de l'expession à l'aide d'une pile'''
    P = []
    for i in range(0, len(s)) : # parcours de tous les caractères de la chaîne
        if estOperateur(s[i]) == False : # s'il ne s'agit pas d'un opérateur
            P.append(float(s[i])) # alors on empile
        else : #si c'est un opérateur
            n = P.pop() # on dépile les deux derniers caractères
            m = P.pop()
            P.append(calcul(s[i], float(m), float(n))) # et on empile le résultat de l'opération
    res = P.pop() # le résultat final se trouve au sommet de la pile
    return res

#s = "12+4*3+"
s = "583-*3*31-2*3/+"
res = evaluation(s)
print "Le resultat est", res
