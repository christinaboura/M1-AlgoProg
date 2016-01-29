---
title: Implantation des algorithmes de tri en Python
---

## Tri à bulles (bubble sort)

Le *tri à bulles* est un algorithme de tri très simple dont le principe est de faire remonter à chaque étape les plus grands éléments du tableau à trier, comme les bulles d'air remontent à la surface de l'eau (d'où le nom de l'algorithme).

Commençons par un exemple du fonctionnement de l'algorithme. Supposons qu'on souhaite trier la suite des nombres 

$$[5, 1, 2, 4, 3].$$ 

Voici comment se passe le premier *passage*.

~~~
[5, 1, 2, 4, 3] # On compare 5 et 1 et on les inverse.
[1, 5, 2, 4, 3] # On compare 5 et 2 et on les inverse.
[1, 2, 5, 4, 3] # On compare 5 et 4 et on les inverse.
[1, 2, 4, 5, 3] # On compare 5 et 3 et on les inverse.
[1, 2, 4, 3, 5] # Fin du premier passage.
~~~

À la fin de ce premier passage le tableau n'est pas encore complétement trié et nous devons donc continuer (on doit recommencer par un nouveau passage lorsque au moins un échange a été effectué lors du passage précedent). 

~~~
[1, 2, 4, 3, 5] # On compare 1 et 2 et on ne fait rien.
[1, 2, 4, 3, 5] # On compare 2 et 4 et on ne fait rien.
[1, 2, 4, 3, 5] # On compare 4 et 3 et on les inverse.
[1, 2, 3, 4, 5] # Fin du deuxième passage
~~~

Le tableau est déjà trié, mais on va devoir refaire un passage puisque il y a eu un échange lors du passage précedent. Ce nouveau passage n'inversera aucun élément et l'algorithme se terminera là.

Voici le pseudo-code du tri à bulles (version non-optimisée), où $$n$$ est la longueur du tableau T à trier.

~~~
Tri-Bulles(T)
    pour i de n-1 à 1 // (pas -1)
        pour j de 0 à i - 1
            si T[j] > T[j+1]
               T[j] <-> T[j+1] // inverser T[j] et T[j+1]
~~~

**:**{:.exercise} 

* Implémentez cette version de l'algorithme en Python et testez-là en lui donnant en entrée une liste aléatoire des nombres entiers. Pour générer une liste `L` de `t` nombres entiers aléatoires compris dans l'interval `[a, b)`on peut écrire :

~~~
L = random.sample(range(a, b), t)
~~~

Par exemple, pour générer une liste de 10 entiers compris entre 0 et 99 il suffit d'écrire :

~~~
>>> import random
>>> L = random.sample(range(0, 100), 10)
>>> L
[41, 21, 38, 20, 69, 14, 10, 50, 76, 9]
~~~


* Pourquoi la version de l'algorithme que vous venez d'implementer n'est pas optimale ?

* Réflechissez à une façon de rendre l'algorithme plus optimisé. Implémentez cette méthode et testez-là.

* Quel est le temps d'exécution de cet algorithme dans le cas le plus défavorable ?




## Tri fusion (merge sort) 

Le tri fusion se base sur le principe diviser pour régner.

* Si le tableau a une seule case, alors il est considéré comme trié.

* Sinon, on découpe le tableau en deux parties de même taille (à une case près, si le nombre d'éléments du tableau est impair) et on trie chacune des deux parties.

* On fusionne les deux parties triées.


1. Appliquez le tri fusion *à la main* pour trier le tableau `T = [5 2 4 7 1 3 2 6]`.

2. Implémentez en Python le tri fusion vu en cours et testez-le sur un tableau de taille 1000 contenant des nombres aléatoires de 0  à 10000.

## Autres algorithmes de tri

Implémentez les deux autres algorithmes de tri vus en cours (**tri par insertion** et **tri rapide**).

