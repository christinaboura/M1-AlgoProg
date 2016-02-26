---
title: Graphes
---

## Représenter des graphes

Dans cette partie, on code les deux façons vues en cours de
représenter un graphe : par la matrice d'adjacence, et par pointeurs.

Pour les pointeurs, on va procéder de la même façon que
[pour les arbres](classes-arbres). Les matrices seront stockées comme
des listes de listes. Ainsi l'objet

~~~python
[[1,2,3], [3,4,5]]
~~~

représente la matrice 2×3

$$\begin{pmatrix}1&2&3\\3&4&5\end{pmatrix}.$$

### Matrices

**:**{:.exercise} Créez une classe `Matrice`, avec un unique
constructeur, qui :

- prend en paramètre une liste de listes, représentant les
  coefficients d'une matrice,
- vérifie que toutes les listes ont la même longueur,
- stocke les coefficients dans un champ `coeffs`,
- stocke dans des champs `nblignes` et `nbcolonnes` les dimensions de
  la matrice.

L'affichage par défaut des objets est peu lisible. Python offre une
longue liste de méthodes dites *spéciales*, reconnaissables aux
doubles tirets bas `__nom_de_la_methode__`, qui permettent de changer le
comportement des objets. La méthode spéciale `__repr__(self)` doit
renvoyer une chaîne de caractères (**renvoyer**, pas faire un
`print` !), qui est utilisée par Python pour afficher l'objet dans le
terminal ou le notebook.

**:**{:.exercise} Donnez une méthode `__repr__` à la classe `Matrice`,
qui affiche les coefficients de la matrice, avec des retours à la
ligne entre chaque ligne, comme dans cet exemple :

~~~python
>>> m = Matrice([[1,2,3], [3,4,5], [10,11,12]])
>>> m
/  1  2  3 \
|  3  4  5 |
\ 10 11 12 /
~~~

Faites l'effort de calculer la largeur maximale requise pour chaque
colonne, afin d'avoir un affichage lisible. On rappelle que `"\n"`
permet d'insérer un retour à la ligne dans une chaîne de caractères,
et que `"\\"` permet d'insérer un antislash `\`.

**:**{:.exercise} Écrire une fonction
`rand_mat(lignes, colonnes, coeffs, min=1, max=1, symetrique=False)`
qui renovie en sortie une matrice aléatoire à `lignes` lignes,
`colonnes` colonnes, avec `coeffs` entrées non-nulles comprises entre
`min` et `max`, et symétrique si `symetrique` vaut `True`.

Observez la syntaxe des *paramètres par défaut* donnée dans cet
exercice : les paramètres `min` et `max` valent 1 par défaut,
`symetrique` vaut `False`, et chacun peut être omis lors de l'appel de
la fonction.

### Pointeurs

On passe maintenant à la représentation par pointeurs

**:**{:.exercise} Créer une classe `Noeud`, qui représente un nœud
d'un graphe. Le constructeur prend en paramètre une liste de `Noeud`,
qui représentent les destinations des arêtes, et la stocke.

**:**{:.exercise} Créer une classe `Graphe`, qui représente un
graphe. Le constructeur prend en paramètre une liste de `Noeud`, qui
représente tous les nœuds du graphe.

**:**{:.exercise} Donner une méthode `adjacence` à la classe `Graphe`,
qui renvoie la matrice d'adjacence du graphe. Les lignes et les
colonnes de la matrice doivent apparaître dans le même ordre que dans
la liste de `Noeud` du graphe.

**:**{:.exercise} Donner une méthode `graphe` à la classe `Matrice`,
qui renvoie `None` si la matrice ne représente pas un graphe (par ex.,
elle n'est pas carrée), le graphe représenté par la matrice sinon.

Tester vos classes avec des matrices aléatoires.

## Parcours de graphes

**:**{:.exercise} Coder l'algorithme de parcours de graphes en
largeur, et l'utiliser pour enrichir la classe `Graphe` avec les
informations suivantes :

- nombre d'arêtes,
- nombre d'arêtes entrantes et sortantes pour chaque `Noeud`,
- nombre de composantes connexes.

On rappelle ici le fonctionnement de l'algorithme, en pseudo-code.

> **Entrée :** une file $$F$$ (initialisée avec un seul nœud)
>
> 1. Sortir l'élement $$v$$ en tête de la file ;
> 2. Pour chaque arrête non-visitée $$e:v→u$$ :
>    1. marquer $$e$$ comme visitée ;
>    2. si $$u$$ n'a pas été visité :
>       1. marquer $$u$$ comme visité ;
>       2. marquer $$v$$ comme parent de $$u$$ ;
>       3. insérer $$u$$ dans la file ;
> 3. Tant que la file n'est pas vide, recommencer.

Vous pouvez utiliser une liste python pour remplir la file, servez
vous des méthodes `pop` (on rappelle que `pop` prend un argument
optionnel) et `append`.

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
