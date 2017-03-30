---
title: Bin packing
---

Dans ce TD nous allons étudier le problème de remplissage de boîtes
(*bin packing*).  Une instance du problème est donnée par une liste de
$$n$$ objets de taille $$s_i$$, avec $$0 \le s_i <1$$.  On souhaite
ranger ces objets dans un minimum de boîtes de taille 1.  Par exemple,
des objets de tailles $$0.1, 0.2, 0.4, 0.8, 0.4$$ peuvent être rangés
dans deux boîtes.

## Un algorithme glouton

On va commencer avec un algorithme glouton, qui prend les objets un par
un et les range dans la première boîte qui peut l'accueillir.

**:**{:.exercise} Implémenter l'algorithme glouton

**:**{:.exercise} Montrer que l'algorithme glouton ne trouve pas
  toujours la solution optimale.

Nous allons maintenant montrer que l'algorithme glouton trouve néamoins
une bonne approximation de la solution optimale.

On note $$ S = \Sum_{i=1}^n s_i $$

**:**{:.exercise} Monter que le nombre optimal de boîtes nécessaires est
  au moins égal à $$\lceil S \rceil$$

**:**{:.exercise} Monter que l'algorithme glouton laisse au plus une
  boîtes remplie à moins de la moitié.

**:**{:.exercise} Montrer que le nombre de boîtes utilisés par
  l'algorithme glouton est au plus $$ \lceil 2S \rceil$$

**:**{:.exercise} En conclure que l'algorithme glouton utilise au plus
  deux fois plus de boîtes qu'une solution optimale.

## Un algorithme optimal

**:**{:.exercise} Implémenter un algorithme optimal, qui teste toutes
  les positions pour chaque objet.

**:**{:.exercise} Comparer les performances des deux algorithmes.
Jusqu'à quelle tailles de donnée peut-on utiliser l'algorithme exact?
