---
title: Programmation linéaire
---

## Un problème simple

Cet exercice est à faire à la main.

Soit le programme linéaire écrit sous forme canonique

> Maximiser $$18x_1 + 12.5x_2$$  
> Sous  
> $$\begin{array}{c r r r}
> x_1 & + & x_2 & \leq & 20\\
> x_1 &  &  & \leq & 12\\
>  &  & x_2 & \leq & 16\\
>  &  & x_1,x_2 & \ge & 0\\
> \end{array}$$

1. Écrire le programme sous forme standard.
2. Résoudre le problème avec une approche géométrique.
3. Résoudre le problème en utilisant l'algorithme du simplexe.



*Le reste du TD est à développer dans un notebook Jupyter.*

## Algorithme du simplexe 

On va coder l'algorithme du simplexe, en utilisant la méthode des
tableaux.

Étant donné un programme linéaire sous forme standard

> Maximiser $$c·\bar{x}$$,  
> Sous $$A\bar{x} = b$$,

où $$c$$ est la fonction de coût, $$b$$ le vecteur des constantes, et
$$\bar{x}$$ le vecteur des variables (base et hors-base), la
méthode encode ce programme dans le tableau

$$\begin{array}{ c | c}
 c & 0\\
\hline
A & b
\end{array}$$

Ensuite, tant qu'il existe une entrée négative dans la ligne de coût
$$c$$, l'algorithme exécute une transformation appelée *pivot* sur les
lignes du tableau. L'algorithme termine lorsqu'il n'y a plus d'entrées
négatives dans le coût, ou bien lorsqu'il détermine que le programme
linéaire est non-borné.

Si $$v$$ est la variable (non-basique) de $$x$$ sélectionnée pour
opérer le pivot, une itération du pivot consiste en les opérations
suivantes :

- Pour chaque ligne $$A_i\bar{x} = b_i$$, calculer la valeur
  
  $$d_i = \begin{cases}b_i/a_i &\text{si $a_i>0$,}\\ +∞ &\text{sinon,}\end{cases}$$
  
  où $$a_i$$ est le coefficient de $$v$$ dans $$A_i$$.

- Si tous les $$d_i$$ sont $$+∞$$, renvoyer « non-borné ».

- Sinon, sélectionner la ligne $$i$$ telle que $$d_i$$ est minimal ;

- Diviser toute la ligne par $$a_i$$ ;

- Faire apparaître des $$0$$ dans la colonne de $$v$$ en faisant des
  combinaisons linéaires de la ligne $$i$$ avec les autres lignes.

La conséquence d'un pivot est de transformer la variable $$v$$ de
non-basique en basique. La solution associée à la transformation sera
celle où les variables non-basiques valent $$0$$, et les variables
basiques valent l'entrée correspondante dans le vecteur $$b$$.

### Exemple

Soit le programme linéaire sous forme standard

> Maximiser $$x_1 + x_2$$  
> Sous  
> $$\begin{array}{c r r r}
> x_3 =& 8& - 4x_1& + x_2\\
> x_4 =& 10& - 2x_1& - x_2\\
> x_5 =& 2& + 5x_1& - 2x_2
> \end{array}$$

le tableau correspondant est

$$\begin{array}{ c c c c c | c}
  x_1 & x_2 & x_3 & x_5 & x_5\\
 1 & 1 & \\
\hline
4 & -1 & 1 &  &  & 8\\
2 & 1 &  & 1 &  & 10\\
-5 & 2 &  &  & 1 & 2
\end{array},$$

où on reconnaît les variables hors-base $$x_1,x_2$$ et les variables
de base $$x_3,x_4,x_5$$ (associées à la matrice identité), et auquel on
associe la solution réalisable de base $$(x_1,x_2,x_3,x_4,x_5)=(0,0, 8, 10, 2)$$.

Puisque les coûts associées sont $$1,1$$, l'algorithme du simplexe
peut choisir aussi bien la variable $$x_1$$ que la variable $$x_2$$ comme variable entrante pour
pivoter. Choisissons la variable $$x_1$$, le pivot va alors calculer

- $$d_1 = 8/4 = 2$$,
- $$d_2 = 10/2 = 5$$,
- $$d_3 = +∞$$.

La ligne choisie pour pivoter sera donc la ligne 1, ce qui va donner
après pivotage le tableau

$$\begin{array}{c c c c c | c}
   x_1 & x_2 & x_3 & x_4 & x_5\\
 & \frac{5}{4} & -\frac{1}{4} & & & 2 \\
\hline
   1 & -\frac{1}{4} &  \frac{1}{4} &   &   & 2\\
     &  \frac{3}{2} & -\frac{1}{2} & 1 &   & 6\\
     &  \frac{3}{4} & \frac{5}{4} &   & 1 & 12
\end{array},$$

où $$x_1,x_4,x_5$$ sont devenues variables de base, et où la solution réalisable de base correspond à $$(x_1,x_2,x_3,x_4,x_5)=(2,0, 0, 6, 12)$$. La valeur de l'objectif est maintenant $$2$$.

**:**{:.exercise} Écrire une fonction `pivot(cout, variables)` 
prenant les entrées suivantes :

- `cout` est une liste contenant la fonction de cout ;
- `variables` est le tableau des variables basiques, non-basiques, et
  des constantes, avec les colonnes apparaissant dans le même ordre
  que dans la fonction de coût. Utilisez une liste de listes, comme
  vous avez fait pour les matrices.
  
La fonction doit donner en sortie le résultat d'un pivot de
l'algorithme du simplexe, c'est à dire un tuple
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

Appliquer cette fonction à :

~~~python
cout = [1, 1, 0, 0, 0, 0]
variables = [
    [ 4, -1, 1, 0, 0,  8],
    [ 2,  1, 0, 1, 0, 10],
    [-5,  2, 0, 0, 1,  2]
]
pivot(cout, variables)
~~~


**:**{:.exercise} Écrire l'algorithme du simplexe complet.

Appliquer votre programme à l'example ci-dessus :

~~~python
c = [1, 1]
A = [[4, -1],
     [2, 1],
     [-5, 2]]
b = [8, 10, 2]
simplexe(c, A, b)
~~~
