---
title: Graphes
---

## Représenter des graphes

Dans cette première partie, on code les deux façons vues en cours de représenter un graphe : par la matrice d'adjacence ou par les pointeurs.

Pour les pointeurs, on va procéder de la même façon que pour les arbres. Les matrices seront stockées comme des listes de listes. Ainsi l'objet

~~~python
[[1,2,3], [3,4,5]]
~~~

représente la matrice 2×3 

$$\begin{pmatrix}1&2&3\\3&4&5\end{pmatrix}.$$

### Matrices

**:**{:.exercise}

Créez une classe `Matrice`, avec un unique constructeur, qui :

- prend en paramètre une liste de listes, représentant les coefficients d'une matrice,
- vérifie que toutes les listes ont la même longueur,
- stocke les coefficients dans un champ `coeffs`,
- stocke dans des champs `nblignes` et `nbcolonnes` les dimensions de la matrice.

**Note :** Un constructeur ne fait jamais de `return`. Pour signaler une condition d'erreur dans un constructeur, vous **devez** *soulever une exception* en utilisant le mot clef `raise`, comme ceci :

~~~python
class Matrice:
    def __init__(self, coefficients):
	if len(coefficients) == 0:
	    raise RuntimeError("Matrice vide")
~~~

L'affichage par défaut des objets est peu lisible. Python offre une longue liste de méthodes dites *spéciales*, reconnaissables aux doubles tirets bas `__nom_de_la_methode__`, qui permettent de changer le comportement des objets. La méthode spéciale `__repr__(self)` doit renvoyer une chaîne de caractères (**renvoyer**, pas faire un `print` !), qui est utilisée par Python pour afficher l'objet, que ce soit dans le notebook ou dans un terminal.

**:**{:.exercise}

Donnez une méthode `__repr__` à la classe `Matrice`, qui affiche les coefficients de la matrice, avec des retours à la
ligne entre chaque ligne, comme dans cet exemple :

~~~python
>>> m = Matrice([[1,2,3], [3,4,5], [10,11,12]])
>>> m
/  1  2  3 \
|  3  4  5 |
\ 10 11 12 /
~~~

Faites l'effort de calculer la largeur maximale requise pour chaque colonne, afin d'avoir un affichage lisible. On rappelle que `"\n"` permet d'insérer un retour à la ligne dans une chaîne de caractères, et que `"\\"` permet d'insérer un antislash `\`.

**:**{:.exercise}

Écrire une fonction `rand_mat(lignes, colonnes, coeffs, min=1, max=1, symetrique=False)` qui renvoie en sortie une matrice aléatoire à `lignes` lignes, `colonnes` colonnes, avec `coeffs` entrées non-nulles comprises entre `min` et `max`, et symétrique si `symetrique` vaut `True`.

Observez la syntaxe des *paramètres par défaut* donnée dans cet exercice : les paramètres `min` et `max` valent 1 par défaut, `symetrique` vaut `False`, et chacun peut être omis lors de l'appel de la fonction.

### Pointeurs

On passe maintenant à la représentation par pointeurs

**:**{:.exercise}

Créer une classe `Noeud`, qui représente un nœud d'un graphe. Le constructeur prend en paramètre une liste de `Noeud`, qui représentent les destinations des arêtes, et la stocke.

**:**{:.exercise} 

Créer une classe `Graphe`, qui représente un graphe. Le constructeur prend en paramètre une liste de `Noeud`, qui représente tous les nœuds du graphe.

**:**{:.exercise}

Donner une méthode `adjacence` à la classe `Graphe`, qui renvoie la matrice d'adjacence du graphe. Les lignes et les colonnes de la matrice doivent apparaître dans le même ordre que dans la liste de `Noeud` du graphe.

**:**{:.exercise}

Donner une méthode `graphe` à la classe `Matrice`, qui renvoie une erreur si la matrice ne représente pas un graphe (par exemple si elle n'est pas carrée) et le graphe représenté par la matrice sinon.

Tester vos classes avec des matrices aléatoires où des graphes construits à la main.

## Parcours de graphes

**:**{:.exercise}

Coder l'algorithme de parcours de graphes en largeur et l'utiliser pour enrichir la classe `Graphe` avec les
informations suivantes :

- nombre d'arêtes,
- nombre d'arêtes entrantes et sortantes pour chaque `Noeud`,
- nombre de composantes connexes.

On rappelle ici le fonctionnement de l'algorithme, en pseudo-code.

> **Entrée :** une file $$F$$ (initialisée avec un seul nœud)
>
> - Sortir l'élement $$u$$ en tête de la file ;
> - Marquer $$u$$ comme visité ;
> - Pour chaque arrête $$e:u→v$$ :
>    - si $$v$$ n'a pas été visité :
>       - marquer $$u$$ comme parent de $$v$$ ;
>       - insérer $$v$$ dans la file ;
> - Tant que la file n'est pas vide, recommencer.
{: style="margin-left: 2em"}

Vous pouvez utiliser une liste python pour remplir la file et vous servir des méthodes `pop` (on rappelle que `pop` prend un argument optionnel) et `append`.

## Tri topolgique

**:**{:.exercise} 

Coder l'algorithme de tri topologique, en utilisant un parcours de graphe en profondeur. On rappelle l'algorithme :

> **Initialisation :** une liste $$L$$ (vide)
>
> - Parcourir le graphe avec un parcours en profondeur
> - Ajouter les nœuds dans L quand on a fini de les explorer
{: style="margin-left: 2em"}


**:**{:.exercise}

Ajouter un test pour détecter si le graphe est acyclique.

## Algorithme de Dijkstra

**:**{:.exercise}

Coder l'algorithme de Dijkstra vu en cours.

## Arbres couvrant de poids minimal

On veut répondre au problème suivant. On a plusieurs villes reliées par des routes. On souhaite déployer la fibre optique sur ce territoire, mais on veut minimiser la taille du cable totale que nous devons déployer pour relier toutes les villes entre elles.

Pour cela, on modélise les villes par des sommets d'un graphe non-orienté, où la pondération des arêtes est la distance des villes entre elles reliées par les routes.

Nous cherchons donc pour ce problème un arbre couvrant de poids minimal. 

**:**{:.exercise}

Programmez l'algorithme de Kruskal.

## Théorie, exercices

**:**{:.exercise}

Prouvez l'exactitude de l'algorithme du tri topolique en utilisant le parcours en profondeur récursif.

**:**{:.exercise}

Prouvez la propriété de relâchement du chemin: si $$G=(S,A)$$ pondéré par une fonction de pondération $$w:A\to \mathbb{R}$$. Soit $$p=(v_0,...,v_k)$$ un plus court chemin. Si l'on applique les relâchements successifs $$(v_0,v_1)$$, $$(v_1,v_2)$$,...,$$(v_{k-1},v_k)$$ en faisant n'importe quels autres relâchements entre, alors $$d[v_k] = \delta(s,v_k)$$. 

En déduire l'exactitude de l'algorithme de Bellman Ford.

**:**{:.exercise}

Évaluez la complexité de l'algorithme de Dijkstra vu en cours.

**:**{:.exercise}

Montrez l'exactitude de l'algorithme de Kruskal.

