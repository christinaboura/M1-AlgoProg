---
title: Bin packing
---

Dans ce TD nous allons étudier le problème de remplissage de boîtes
(*bin packing*).  Une instance du problème est donnée par une liste de
$$n$$ objets de taille $$s_i$$, avec $$0 < s_i <1$$.  On souhaite
ranger ces objets dans un minimum de boîtes de taille 1.  Par exemple,
des objets de tailles $$0.1, 0.2, 0.4, 0.8, 0.4$$ peuvent être rangés
dans deux boîtes.

## Un algorithme glouton

On va commencer avec un algorithme glouton, qui prend les objets un par
un et les range dans la première boîte qui peut l'accueillir.

**:**{:.exercise} Implémenter l'algorithme glouton.

**:**{:.exercise} Montrer que l'algorithme glouton ne trouve pas
  toujours la solution optimale.

Nous allons maintenant montrer que l'algorithme glouton trouve néamoins
une bonne approximation de la solution optimale.

On note $$ S = \sum_{i=1}^n s_i $$

**:**{:.exercise} Monter que le nombre optimal de boîtes nécessaires est
  au moins égal à $$\lceil S \rceil$$

**:**{:.exercise} Monter que l'algorithme glouton laisse au plus une
  boîte remplie à moins de la moitié.

**:**{:.exercise} Montrer que le nombre de boîtes utilisées par
  l'algorithme glouton est au plus $$ \lceil 2S \rceil$$

**:**{:.exercise} En conclure que l'algorithme glouton utilise au pire
  deux fois plus de boîtes qu'une solution optimale.

## Un algorithme optimal

**:**{:.exercise} Implémenter un algorithme optimal, qui teste toutes
  les positions pour chaque objet.

**:**{:.exercise} Comparer les performances des deux algorithmes.
Jusqu'à quelle tailles de donnée peut-on utiliser l'algorithme exact?

On peut générer des instances de test avec:
~~~python
import random
L = [ random.uniform(0,1) for _ in range(16) ]
~~~

## NP-complétude

On veut montrer que le problème de *bin packing* est NP-complet, par
réduction au problème du *sac à dos*.

On rappelle le problème du *sac à dos*: étant donné un ensemble
d'entiers positifs $$X = \{x_1, x_2, \dots, x_n\}$$, et un entier
$$t≥0$$, déterminer s'il existe un sous-ensemble $$X'⊂X$$ tel que

$$t = \sum_{x∈S'} x.$$

**:**{:.exercise} Montrer que le problème de *bin packing* est
  NP-complet.  

À partir d'une instance $$X = \{x_1, x_2, \dots, x_n\}$$ du *sac à dos*,
construire une instance de *bin packing* telle que le nombre minimal de
boîte soit 2 si l'instance $X$ a une solution, et 3 sinon.
