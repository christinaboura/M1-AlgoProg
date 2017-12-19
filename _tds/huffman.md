---
title: Code de Huffman
---

Cet exercice de programmation est une version modifiée d'un TP créé par Luca De Feo et que vous pouvez consulter [ici](http://defeo.lu/in420/Construction%20du%20code%20de%20Huffman).  

Le codage de Huffman est un algorithme de compression de données sans perte, inventé par David Albert Huffman en 1952. Dans les langues naturelles, certaines lettres apparaissent avec une fréquence plus élevée que d'autres. L'idée du code de Huffman est de replacer les symboles les plus fréquents par des suites binaires courtes et de remplacer les symboles les moins fréquents par des suites plus longues.

Le principe repose sur la création d'un arbre binaire pondéré. Ce principe est expliqué dans le lien suivant :


[Compression : le code de Huffman, à l’ENPC](http://cermics.enpc.fr/polys/oap/node49.html)


Cet exercice a comme but de construire l'arbre de Huffman en Python et de l'utiliser ensuite pour coder et décoder.

## Construction de l'arbre de Huffman

**:**{:.exercise} Commencez par créer une classe `Node` qui représentera le noeud d'un arbre binaire contenant les données nécessaires à l'algorithme de Huffman. Ces données sont une variable `symbol` pour représenter un symbole de l'alphabet à encoder ainsi qu'un nombre réel `freq` pour représenter sa fréquence. Les champs `left` et `right` permettent de pointer vers les noeuds fils, et ils ont la valuer spéciale `None` lorsque le noeud est une feuille. Complétez le constructeur de la classe.

~~~python
>>> class Node :
...     def __init__(self, symbol, freq, right, left) :
        # A completer
~~~

**:**{:.exercise} Création de la méthode `creatTree`.

* La méthode `createTree` sert à créer l’arbre de Huffman. Ses entrées sont deux listes, qu’on suppose de la même longueur, contenant respectivement les symboles de l’alphabet et leurs fréquences. On rappelle brièvement le principe de l’algorithme de Huffman, et on en suggère une implantation possible.

* Créer les feuilles de l’arbre: une par symbole de l’alphabet, chacune marquée par sa fréquence. Vous pouvez utiliser une liste pour créer une liste de `Node` : un pour chaque symbole.

* Tant que l’arbre n’est pas complet, prendre les deux noeuds avec les plus petites probabilités et les relier avec un nouveau noeud. Le nouveau noeud est marqué avec la somme des fréquences des deux fils. Vous pouvez à ce stade-ci créer une méthode qui trouve et renvoie le noeud ayant la plus petite probabilité. À chaque fois que vous unissez deux noeuds, retirez-les de la liste et ajoutez-y le nouveau noeud.

* Lorsque tous les noeuds sont connectés à la racine, l’algorithme se termine. La liste de noeuds sera réduite à un seul élément, la racine, et il suffit de la renvoyer.

Testez votre méthode avec les données suivantes :

~~~python
symbols = ['a', 'b', 'c', 'd']
freqs = [0.25, 0.45, 0.20, 0.10]
~~~

ou lorsque vous êtes vraiment sûrs de votre code avec :

~~~python
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

freqs = [0.03, 0.12, 0.01, 0.06, 0.04, 0.04, 0.04, 0.01, 0.04,
0.06, 0.04, 0.03, 0.02, 0.02, 0.01, 0.10, 0.01, 0.06,
0.01, 0.03, 0.01, 0.03, 0.02, 0.03, 0.06, 0.07]
~~~

**:**{:.exercise} Méthode `createCode`

*Complétez la méthode `createCode`, qui prend en entrée la racine de l’arbre de Huffman, et qui renvoie un dictionnaire, contenant dans l’ordre les codages (binaires) des symboles de ‘a’ à ‘z’. Pour cette méthode, un algorithme récursif est le plus adapté à parcourir l’arbre. Par exemple, vous pouvez ajouter une méthode

~~~python
def traversal(node, code, codes)
~~~
qui parcourt tout le sous-arbre en dessous de `node`, en remplissant le dictionnaire de `codes`. Ici, `node`est un noeud quelconque de l'arbre, `code` est une chaîne contenant le code du chemin parcouru jusqu'au noeud et codes est le dictionnaire qui sera rempli avec les encodages.

Lorsque vous aurez implanté correctement les méthodes `createTree` et `createCode`, la sortie du main doit être égale au code suivant (ou à son complémentaire selon si vous avez assigné 0 à gauche et 1 à droite, ou vice-versa):

~~~

y : 0111
e : 00110
x : 00111
s : 110101
q : 110110
f : 00101
w : 000001
h : 0000000
m : 000011
n : 000010
r : 1000
a : 01101
g : 00100
o : 110111
u : 110100
l : 01100
p : 111
j : 1001
v : 01010
z : 0100
d : 1100
c : 0000001
i : 00011
b : 101
t : 01011
k : 00010
~~~

## Codage et décodage avec Huffman

**:**{:.exercise} Créer une fonction `encoder(codes, phrase)` qui prend en entrée le dictionnaire `codes`ci-dessus ainsi qu'une phrase à encoder et renvoie une suite binaire correspondant au codage pour le code de Huffman.

**:**{:.exercise} Créer une fonction `decoder(codes, code)` qui prend en entrée le dictionnaire `codes` et un encodage et qui renvoie la phrase avant l'encodage. Testez votre code en essayent de décoder 

~~~
"000110010101111101111101000000001011010000101000001100110111000101\
1000000000011110101010110000000001100000100111110111110100110000011\
1100000110101110000001100100000000001011"
~~~
