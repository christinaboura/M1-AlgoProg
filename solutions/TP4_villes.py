#-*- coding: utf-8 -*-

class Ville :
    """classe définissant une ville de France. Chaque ville a 4 attributs :
        - nom
        - numero de departement
        - population (hab)
        - superficie (km^2)
        - rang au niveau national (place)"""

    def __init__(self,liste) :
        self.nom = liste[0]
        self.departement = int(liste[1])
        self.population = int(liste[2])
        self.superficie = float(liste[3])
        self.rang = int(liste[4])

    def getRang(self) :
        return self.rang
    
    def getSuperficie(self) :
        return self.superficie

    def afficherVille(self) :
        print(self.nom, self.departement, self.population, self.superficie, self.rang)

    def afficherNom(self) :
        print(self.nom)

    def afficherVille(self) :
        print(self.nom, self.departement, self.population, self.superficie)

      
class Noeud:
    """un noeud de l'arbre : fils gauche + fils droit + un objet de type ville"""

    def __init__(self,liste):
        self.gauche = None
        self.droite = None
        self.ville = Ville(liste)
    
    def inserer(self, liste):
        ville = Ville(liste)
        if ville.getRang() < self.ville.getRang() :
        # if ville.getSuperficie() < self.ville.getSuperficie() :    
            if self.gauche is None:
                self.gauche = Noeud(liste)
            else:
                self.gauche.inserer(liste)
        else :
            if self.droite is None:
                self.droite = Noeud(liste)
            else:
                self.droite.inserer(liste)

    def afficherArbre(self): # parcours infixe
        if self.gauche:
            self.gauche.afficherArbre()
        self.ville.afficherVille()
        if self.droite:
            self.droite.afficherArbre()

    def rechercher(self, rang):
        if rang < self.ville.getRang() :
            if self.gauche is None:
                return None
            return self.gauche.rechercher(rang)
        elif rang > self.ville.getRang() :
            if self.droite is None:
                return None
            return self.droite.rechercher(rang)
        else :
            return self

    def compter_enfants(self):
        compteur = 0
        if self.gauche :
            compteur += 1
        if self.droite :
            compteur += 1
        return compteur

    def rechercheMax(self) :
        while self.droite :
            return self.droite.rechercheMax()
        return self


fichier = open("villes.txt", "r")

liste = ["Maisons-Alfort", 94, 51091, 5.4, 100]
noeud = Noeud(liste)

for ligne in fichier:
    liste = ligne.rsplit(" ",-1)
    noeud.inserer(liste)

fichier.close()
noeud.afficherArbre()

unNoeud = noeud.rechercher(130)
if unNoeud is not None :
    unNoeud.ville.afficherNom()
else :
    print("Non trouvé")

nombreEnfants = unNoeud.compter_enfants()
print("Nombre d'enfants = ", nombreEnfants)

# unNoeud = noeud.rechercheMax()
# if unNoeud is not None :
#     unNoeud.ville.afficherNom()
# else :
#     print("Arbre vide")
