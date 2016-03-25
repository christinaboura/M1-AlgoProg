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

## Un algorithme récursif pour le problème d'optimisation

Le problème d'optimisation associé à la paire $$(S,t)$$, consiste à
trouver le sous-ensemble $$S'⊂S$$ qui maximise la valeur
$$\sum_{x∈S'}x$$ sous la contrainte $$\sum_{x∈S'}x≤t$$.

Pour $$i≥1$$, on définit la valeur $$M(i,t)$$ comme étant la solution
du problème d'optimisation associé à $$(\{x_1,\dots,x_i\},t)$$ :

$$M(i,t) = \max\left(\sum_{x∈S'}x ≤ t \;\middle\vert\; S'⊂\{x_1,\dots,x_i\}\right).$$

**:**{:.exercise} Écrire une fonction `partial_subset_sum(S, i, t)`
qui calcule $$M(i,t)$$ à l'aide de deux appels récursifs à
`partial_subset_sum(S, i-1, ...)`.

**:**{:.exercise} Récrire `subset_sum(S, t)` pour qu'il fasse appel à
`partial_subset_sum`.

## Amélioration par programmation dynamique

Les appels récursifs de la partie précédente passent beaucoup de temps
à recalcuer les valeurs $$M(i,t)$$. Par les techniques de mémoisation
et de la programmation dynamique, nous pouvons mémoriser ces appels et
réutiliser les résultats pour les appels suivants.

L'idée de la mémoisation consiste à calculer, à la place de
$$M(i,t)$$, toute la liste $$P(i,t)$$ définie comme suit :

$$P(i,t) = \left\{\sum_{x∈S'}x ≤ t \;\middle\vert\; S'⊂\{x_1,\dots,x_i\}\right\}.$$

Les deux appels récursifs de l'algorithme précedent, sont donc
remplacés par un appel récursif qui calcule $$P(i,t)$$, suivi par le
calcul de

$$P'(i,t) = \left\{x_{i+1} + \sum_{x∈S'}x ≤ t \;\middle\vert\; S'⊂\{x_1,\dots,x_i\}\right\}.$$

L'ensemble $$P(i+1,t)$$ sera alors obtenu en fusionnant $$P(i,t)$$ et
$$P'(i,t)$$. La fusion est facilitée on fait attention à garder les
deux listes ordonnées (comparer avec le [tri fusion](tris)).

**(mémoisation) :**{:.exercise} Écrire une variante
`partial_subset_sum_memo` qui procède comme décrit ci-dessus, en
calculant les listes $$P(i,t)$$ par un appel récursif.

**:**{:.exercise} Écrire une variante `partial_subset_sum_dyn` sans
appels récursifs.

**:**{:.exercise} Utiliser les techniques de mesure des performances
vues au [TD sur l'algèbre linéaire](linalg) pour comparer les
performances de vos algorithmes.
