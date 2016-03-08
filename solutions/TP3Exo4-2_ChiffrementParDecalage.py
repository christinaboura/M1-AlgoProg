# -*- coding: utf-8 -*-

def creerDictionnaire() :
    ''' Creation du dictionnaire en se basant sur le code ASCII de chaque lettre '''
    dico = {}
    for i in range(97, 97+23) :
        dico[chr(i)] = chr((i + 3))
        dico['x'] = 'a'
        dico['y'] = 'b'
        dico['z'] = 'c'
    return dico


def chiffrementLettre(l, d) :
    ''' Fonction qui renvoie la lettre chiffrée  correspondant à la lettre clair l, à l'aide du dictionnaire d '''
    return d[l]


def chiffrementPhrase(p,d) :
    ''' Fonction qui renvoie la phrase chiffrée corresponant à la phrase p à l'aide du dictionnaire d '''
    s = " " # Au depart la chaîne est vide
    for i in range(0, len(p)) : # On parcours la chaîne p caractère par caractère
        if p[i] != ' ' : # s'il ne s'agit pas d'un espace blanc
            s += chiffrementLettre(p[i], d) # je concatène à la chaîne la lettre chiffrée
    return s

def inverseDictionnaire(dico) :
    ''' Fonction qui crée le dictionnaire inverse du dictionnaire dico passé en paramètre '''
    dicoInv = {}
    for cle in dico :
        dicoInv[dico[cle]] = cle
    return dicoInv

dico = creerDictionnaire()
s = chiffrementPhrase("cours algorithmique et programmation", dico)
print(s)
dicoInv = inverseDictionnaire(dico)
s = chiffrementPhrase("frxuvdojrulwkpltxhhwsurjudppdwlrq", dicoInv)
print(s)





