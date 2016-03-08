from random import randint

def max(a,b) :
    # Fontion auxiliaire renvoyant le maximum de deux entiers
    if a < b :
        return b
    else :
        return a

class Noeud :
    
    def __init__(self,entier) :
        self.gauche = None
        self.droite = None
        self.cle = entier
            
    def inserer(self, entier) :
        if entier < self.cle :
            if self.gauche is None:
                self.gauche = Noeud(entier)
            else:
                self.gauche.inserer(entier)
        else :
            if self.droite is None:
                self.droite = Noeud(entier)
            else:
                self.droite.inserer(entier)


    def parcoursInfixe(self) :
        if self.gauche:
            self.gauche.parcoursInfixe()
        print(self.cle)
        if self.droite:
            self.droite.parcoursInfixe()

    def profondeurMaximale(self, depth) :
        if (self.droite is None) and (self.gauche is None) :
            return depth
        elif self.droite is None :
            return self.gauche.profondeurMaximale(depth + 1)
        elif self.gauche is None :
            return self.droite.profondeurMaximale(depth + 1)
        else :
            return max(self.gauche.profondeurMaximale(depth + 1), self.droite.profondeurMaximale(depth + 1))



L = []
for i in range(100) :
    L.append(randint(0, 1000))

print(L)

noeud = Noeud(L[0])

for i in range(1,len(L)) :
    noeud.inserer(L[i])

noeud.parcoursInfixe()
print(noeud.profondeurMaximale(0))
