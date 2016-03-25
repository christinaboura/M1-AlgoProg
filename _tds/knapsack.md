---
title: Sacs à dos
---

Dans ce TD nous allons implanter des algorithmes pour résoudre le
problème de la *somme de sous-ensembles* (*Subset sum*), aussi connu
sous le nom de problème du *sac à dos*. On rappelle le problème :
étant donné un unsemble d'entiers positifs $$S = \{x_1, x_2, \dots,
x_n\}$$, et un entier $$t≥0$$, déterminer s'il existe un sous-ensemble
$$S'⊂S$$ tel que

$$t = \sum_{x∈S'} x.$$

## Un algorithme naïf

On va commencer avec un algorithme naïf : on énumère tous les
sous-ensembles de $$S$$, jusqu'à en trouver un qui somme à $$t$$.

**:**{:.exercise} Écrire une fonction `subset_sum(S, t)` qui prend en
entrée une liste d'entiers positifs `S`, un entier positif `t`, et qui
renvoie `True` si le problème $$(S,t)$$ a une solution, en utilisant
l'algorithme naïf décrit plus haut.

## Un algorithme récursif

Pour $$i≥1$$, on définit l'ensemble $$P(i,t)$$ comme étant l'ensemble

$$P(i,t) = \left\{\sum_{x∈S'}x ≤ t \;\middle\vert\; S'⊂\{x_1,\dots,x_i\}\right\}.$$

**:**{:.exercise} Écrire une fonction `partial_subset_sum(S, i, t)`
qui calcule l'ensemble $$P(i,t)$$ à l'aide de deux appels récursifs à
`partial_subset_sum(S, i-1, t)`.

**:**{:.exercise} Récrire `subset_sum(S, t)` pour qu'il fasse appel à
`partial_subset_sum`.

**:**{:.exercise} Optimiser les appels récursifs du point précédent
pour que le troisième paramètre $$t$$ soit le plus petit possible
(tout en donnant une solution correcte).

## Amélioration par programmation dynamique

Les appels récursifs de la partie précédente passent beaucoup de temps
à recalcuer des ensembles $$P(i,t)$$. Par la technique de la
programmation dynamique, nous pouvons mémoriser ces appels et
réutiliser les résultats pour les appels suivants.

**(mémoisation) :**{:.exercise} Écrire une variante
`partial_subset_sum_memo` qui stocke les listes $$P(i,t)$$ dans une
structure de données globale, et qui réutilise ces calculs lorsque
cela est possible.

**:**{:.exercise} Écrire une variante `partial_subset_sum_dyn` sans
appels récursifs.

**:**{:.exercise} Utiliser les techniques de mesure des performances
vues au [TD sur l'algèbre linéaire](linalg) pour comparer les
performances de vos algorithmes.
