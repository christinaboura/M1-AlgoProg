---
title: Graphes, suite
---

## Représenter des graphes

On utilisera les classes du TD précédent pour représenter les graphes,
par matrice d'adjacence et par pointeur.  La solution donnée ici
ajoute des poids optionnels aux arrêtes.

### Matrices

~~~python
class Matrice:
    """
    Ceci est une matrice.
    
    Passer une liste de coefficents au constructeur.
    """
    def __init__(self, coefficients):
        if not isinstance(coefficients, list):
            raise RuntimeError("Pas une liste")
        if not len(coefficients) > 0:
            raise RuntimeError("Matrice vide")
        if not all(isinstance(ligne, list)
                   for ligne in coefficients):
            raise RuntimeError("Pas une liste de listes")
            
        self.nblignes = len(coefficients)
        self.nbcolonnes = len(coefficients[0])
        
        if not all(len(ligne) == self.nbcolonnes
                   for ligne in coefficients):
            raise RuntimeError("Longueurs des lignes différentes")
        self.coeffs = coefficients
   
    def __repr__(self):
        # On mesure la largeur maximale des colonnes
        largeur = max(max(len(str(c)) for c in ligne) for ligne in self.coeffs)
        
        # On compose la sortie. On utilise str.rjust() pour remplir une chaîne
        #
        # Pour du formatage plus général, voire:
        # https://docs.python.org/3.5/library/string.html#formatstrings
        resultat = ""
        for (i, ligne) in enumerate(self.coeffs):
            s = " ".join(str(c).rjust(largeur) for c in ligne)
            if i == 0:
                resultat += "/ "+s+" \\\n" 
            elif i < len(self.coeffs) - 1:
                resultat += "| "+s+" |\n" 
            else:
                resultat += "\\ "+s+" /"
        return resultat
    
    def __eq__(self, other):
        "Méthode spéciale pour tester l'égalité de matrices"
        if not isinstance(other, Matrice):
            return False
        if self.nblignes != other.nblignes or self.nbcolonnes != other.nbcolonnes:
            return False
        for i in range(self.nblignes):
            for j in range(self.nbcolonnes):
                if self.coeffs[i][j] != other.coeffs[i][j]:
                    return False
        return True
    
    def diagonale(self):
        "Renvoie la diagonale de la matrice"
        resultat = []
        for (i,c) in enumerate(self.coeffs):
            resultat.append(c[i])
        return resultat
    
def rand_mat(lignes, colonnes, coeffs, min=1, max=1, sym=False):
    if (sym and lignes != colonnes):
        raise RuntimeError("Seules les matrices carrées peuvent être symétriques")
    if coeffs > lignes*colonnes:
        raise RuntimeError("Trop de coefficients")
    
    # On crée une liste avec autant d'éléments que la matrice à créer
    # Elle commence par des éléments entre min et max, et se termine par des 0
    from random import randint, sample
    nonzero = coeffs if not sym else coeffs // 2
    total = lignes*colonnes if not sym else lignes*(lignes+1) // 2
    entrees = [randint(min, max) for _ in range(nonzero)] + [0]*(total - nonzero)
    
    # On permute la liste avec l'algorithme de Fisher-Yates 
    # https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
    for i in reversed(range(len(entrees))):
        j = randint(0,i)
        entrees[i], entrees[j] = entrees[j], entrees[i]
        
    if not sym:
        # On découpe en lignes
        mat = [entrees[i*colonnes : (i+1)*colonnes] for i in range(lignes)]
    else:
        # On remplit la partie triangulaire inférieure
        mat = [entrees[i*(i+1)//2 : (i+1)*(i+2)//2] + [None]*(lignes-i-1)
               for i in range(lignes)]
        # On symétrise
        for i in range(lignes):
            for j in range(i+1,lignes):
                mat[i][j] = mat[j][i]
        # On a été assez laxistes par rapport au paramètre coeffs
    return Matrice(mat)
~~~

### Pointeurs

~~~python
class Noeud:
    # Variable de classe, pour avoir un affichage plus lisible
    counter = 1
    
    def __init__(self, out):
        assert isinstance(out, list), "Pas une liste"
        assert all(isinstance(n, Noeud) for n in out), "Pas une liste de noeuds"
        self.out = out
        self.cnt = Noeud.counter
        Noeud.counter += 1
        
    def __repr__(self):
        if hasattr(self, 'weight'):
            s = " ".join("→{0}({1})".format(u.cnt,w) for u,w in zip(self.out,self.weight))
        else:
            s = " ".join("→{0}".format(u.cnt) for u in self.out)
        return "Noeud({0}) ".format(self.cnt) + s

class Graphe:
    def __init__(self, noeuds):
        assert isinstance(noeuds, list), "Pas une liste"
        assert all(isinstance(n, Noeud) for n in noeuds), "Pas une liste de noeuds"
        self.noeuds = noeuds
    
    def __repr__(self):
        return "Graphe:\n\t" + "\n\t".join(map(repr, self.noeuds))
    
    def adjacence(self):
        # On remplit la matrice de 0
        mat = [[0 for _ in self.noeuds] for _ in self.noeuds]
        # On met les 1
        for (i,v) in enumerate(self.noeuds):
            if hasattr(v, 'weight'):
                for u,w in zip(v.out,v.weight):
                    mat[i][self.noeuds.index(u)] = w
            else:
                for u in v.out:
                    mat[i][self.noeuds.index(u)] = 1
        return Matrice(mat)

def mat_to_graph(mat):
    assert mat.nblignes == mat.nbcolonnes, "Pas une matrice carrée"
    G = Graphe([Noeud([]) for _ in range(mat.nblignes)])
    weighted = not all(x == 0 or x == 1 for ligne in mat.coeffs for x in ligne)
    if weighted:
        for u in G.noeuds:
            u.weight= []
    for (i, ligne) in enumerate(mat.coeffs):
        for (j, c) in enumerate(ligne):
            if c:
                G.noeuds[i].out.append(G.noeuds[j])
                if weighted:
                    G.noeuds[i].weight.append(c)
    return G

Matrice.graphe = mat_to_graph
~~~

On peut construire le suivant graphe suivant avec ces opérations:

![Graphe](https://upload.wikimedia.org/wikipedia/commons/a/ae/Graphe.jpg){: style="width:10em"}
{:.centered}

~~~python
nodes = [ Noeud([]) for _ in range(9) ]
nodes[0].out = [ nodes[1], nodes[7] ]
nodes[1].out = [ nodes[2], nodes[7] ]
nodes[2].out = [ nodes[5] ]
nodes[3].out = [ nodes[2], nodes[4] ]
nodes[4].out = [ nodes[5] ]
nodes[8].out = [ nodes[7] ]
G1 = Graphe(nodes)
~~~

## Tri topolgique

**:**{:.exercise} Coder l'algorithme de tri topologique, en utilisant un
parcours de graphe en profondeur.  On rapelle l'algorithme:

> **Initialisation :** une liste $$L$$ (vide)
>
> 1. Parcourir le graphe avec un parcours en profondeur
> 2. Ajouter les nœud dans L quand on a finit de les explorer
{: style="margin-left: 2em"}


**:**{:.exercise} Ajouter un test pour detecter si le graphe est acyclique.

## Algorithme de Prim

**:**{:.exercise} Coder l'algorithme de Prim vu en cours.

On rappelle ici le fonctionnement de l'algorithme, en pseudo-code.

> **Entrée :** un arbre $$T$$ (initialisé avec un seul nœud)
>
> 1. Parmi tous les arêtes $$e:T→u$$ qui partent d'un nœud de
>    $$T$$ et qui arrivent sur un nœud pas dans $$T$$,
>    choisir celle de poids minimal ;
> 2. Ajouter $$e$$ et $$u$$ à $$T$$ ;
> 3. Continuer tant qu'il reste des arêtes qui sortent de $$T$$.
{: style="margin-left: 2em"}

On pourra utiliser le gaphe suivant comme test:

![Graphe](https://upload.wikimedia.org/wikipedia/commons/b/b4/Kruskal_Algorithm_1.svg){: style="width:15em"}
{:.centered}

~~~python
A = Noeud([])
B = Noeud([])
C = Noeud([])
D = Noeud([])
E = Noeud([])
F = Noeud([])
G = Noeud([])

A.out = [B, D]
A.weight = [7,5]
B.out = [A, C, D, E]
B.weight = [7, 8, 9, 7]
C.out = [B, E]
C.weight = [8, 5]
D.out = [A, B, E, F]
D.weight = [5, 9, 15, 6]
E.out = [B, C, D, F, G]
E.weight = [7, 5, 15, 8, 9]
F.out = [D, E, G]
F.weight = [6, 8, 11]
G.out = [E, F]
G.weight = [9, 11]
G2 = Graphe([A, B, C, D, E, F, G])
~~~

## Algorithme de Dijkstra

**:**{:.exercise} Coder l'algorithme de Dijkstra vu en cours.

## Parcours Eulériens

On appelle *cycle Eulérien* un cycle (un parcours qui part et termine
sur le même nœud) qui passe exactement une fois par chaque arête, mais
potentiellement plusieurs fois par chaque nœud.

**:**{:.exercise} Prouvez qu'un graphe dirigé possède un cycle
Eulérien si et seulement si le degré sortant de chaque nœud est égal
au degré entrant.

**:**{:.exercise} Codez un algorithme calculant, si possible, un cycle
Eulérien (suggestion : trouvez une procédure pour unir des cycles
disjoints).
