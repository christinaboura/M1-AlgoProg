# -*- coding: utf-8 -*-

def estOuvrante(c) :
    ''' fonction qui renvoie True si le caractère passé en paramètre est un symbole ouvrant et renvoie False sinon '''
    if c == '(' or c == '[' or c == '{' :
        return True
    else :
        return False

def fermante(c) :
    ''' Fonction qui renvoie le symbole fermant correspondant '''
    if c == '[' :
        return ']'
    elif c == '(' :
        return ')'
    elif c == '{' :
        return '}'
    else :
        return None

def verification(s) :
    ''' Fonction qui vérifie à l'aide d'une pile P si le parenthésage est correct '''
    P = []
    for i in range(0, len(s)) :
        if(estOuvrante(s[i])) :
            P.append(fermante(s[i])) # si s[i] est un symbole ouvrant on empile le symbole fermant correspondant
        else :
            if s[i] == P[len(P) - 1] : # si s[i] est égal au caractere se trouvant au sommet de la pile
                P.pop() # on dépile le caractere
    if not P : # si la pile est vide à la fin alors le parenthesage est correct
        return True
    else :
        return False


s = "[La (petite) maison [celle à côté du (grand) sapin (très vert {et moche})]
 est en feu.]"
if(verification(s)) :
    print("Parenthesage correct")
else :
    print("Parenthesage incorrect")
