---
title: Programmation linéaire
---

Ce TD est à développer dans un notebook Jupyter.

## Algorithme du simplexe

On va coder l'algorithme du simplexe, en utilisant la méthode des
tableaux vue en cours.

Étant donné un programme linéaire sous forme relaxée

> Minimiser $$c·\bar{x}$$,  
> Sous $$A\bar{x} = b$$,

où $$c$$ est la fonction de coût, $$b$$ le vecteur des constantes, et
$$\bar{x}$$ le vecteur des variables (basiques et non-basiques), la
méthode encode ce programme dans le tableau

$$\begin{array}{c c | c}
1 & c & 0\\
\hline
  & A & b
\end{array}$$

Ensuite, tant qu'il existe une entrée négative dans la ligne de coût
$$c$$, l'algorithme exécute une transformation appelée *pivot* sur les
lignes du tableau. L'algorithme termine lorsqu'il n'y a plus d'entrées
négatives dans le coût, ou bien lorsqu'il détermine que le programme
linéaire est non-borné.

Si $$v$$ est la variable (non-basique) de $$x$$ sélectionnée pour
opérer le pivot, une itération du pivot consiste en les opération
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

Soit le programme linéaire sous forme relaxée

> Minimiser $$-x - y$$  
> Sous  
> $$\begin{array}{c r r r}
> r =& 8& - 4x& + y\\
> s =& 10& - 2x& - y\\
> t =& 2& + 5x& - 2y
> \end{array}$$

le tableau correspondant est

$$\begin{array}{c c c c c c | c}
  & x & y & r & s & t\\
1 & -1 & -1 & \\
\hline
& 4 & -1 & 1 &  &  & 8\\
& 2 & 1 &  & 1 &  & 10\\
& -5 & 2 &  &  & 1 & 2
\end{array},$$

où on reconnaît les variables non-basiques $$x,y$$ et les variables
basiques $$r,s,t$$ (associées à la matrice identitée), et auquel on
associe le point faisable $$x,y=0$$ et $$r,s,t=(8,10,2)$$.

Puisque les coûts associées sont $$-1,-1$$, l'algorithme du simplexe
peut choisir aussi bien la variable $$x$$ que la variable $$y$$ pour
pivoter. Choisissons la variable $$x$$, le pivot va alors calculer

- $$d_1 = 8/4 = 2$$,
- $$d_2 = 10/2 = 5$$,
- $$d_3 = +∞$$.

La ligne choisie pour pivoter sera donc la ligne 1, ce qui va donner
après pivotage le tableau

$$\begin{array}{c c c c c c | c}
  & x & y & r & s & t\\
1 & & \frac{5}{4} & -\frac{1}{4} & \\
\hline
& 1 & -\frac{1}{4} &  \frac{1}{4} &   &   & 2\\
&   &  \frac{3}{2} & -\frac{1}{2} & 1 &   & 6\\
&   & -\frac{1}{4} & \frac{5}{4} &   & 1 & 12
\end{array},$$

où $$x,s,t$$ sont devenues basiques, et où le point faisable
correspond à $$y,r=0$$ et $$x,s,t=(2,6,12)$$.

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

**:**{:.exercise} Écrire l'algorithme du simplexe complet.

## Visualisation de l'algorithme

Dans votre notebook, insérez le code suivant

~~~python
%matplotlib inline
import matplotlib.pyplot as plt
~~~

Le code suivant affiche le dessin d'une croix de largeur `l`, avec un
cercle jaune au milieu.

~~~python
def cross(l):
    fig, ax = plt.subplots()
    ax.plot([0,l], [0,l], color='black')
    ax.plot([0,l], [l,0], color='red')
	ax.plot(l/2, l/2, marker='o', color='yellow')

cross(10)
~~~

**:**{:.exercise} Modifier le code de `pivot` pour qu'il affiche le
simplexe et le point faisable choisi après pivotage (uniquement
lorsque le problème d'entrée est de dimension 2, *i.e.* il a
uniquement deux variables non-basiques).

Regardez l'algorithme avancer le long de la frontière du simplexe.
