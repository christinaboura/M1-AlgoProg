---
title: Programmation linéaire
---

Ce TD est à développer dans un notebook Jupyter.

## Algorithme du symplexe

On va code l'algorithme du symplexe, en utilisant la méthode des
tableaux vue en cours.

**:**{:.exercise} Écrire une fonction `iteration(cout, variables)` 
prenant les entrées suivantes :

- `cout` est une liste contenant la fonction de cout ;
- `variables` est le tableau des variables basiques, non-basiques, et
  des constantes, avec les colonnes apparaissant dans le même ordre
  que dans la fonction de coût. Utilisez une liste de listes, comme
  vous avez fait pour les matrices.
  
La fonction doit donner en sortie le résultat d'un pivot de
l'algorithme du symplexe, c'est à dire un tuple
`(cout, variables, faisable)`, où

- `cout` est la fonction de coût mise à jour ;
- `variables` est le tableau des variables et des constantes mis à
  jour après le pivot ;
- `faisable` est le point faisable donné par le pivot.

Si le problème est non-borné, on va plutôt donner en sortie
`(cout, variables, None)`, où `cout` et `variables` n'ont pas été
modifiés. Si l'algorithme a déjà atteint le maximum, on n'opérera pas
de pivot, on donnera en sortie `(cout, variables, faisable)`, où
`cout` et `variables` n'ont pas été modifiés.

**:**{:.exercise} Écrire l'algorithme du symplexe complet.

## Visualisation de l'algorithme

...en cours
