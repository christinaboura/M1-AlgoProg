---
title: Programmation dynamique
---

## Chaîne de multiplications matricielles

**:**{:.exercise} 

Implémentez l'algorithme vu en cours pour trouver le parenthésage optimal pour la multiplication chaînée de $$n$$ matrices $$M_1M_2\cdots M_n$$. Votre algorithme doit prendre en entrée une suite de longueur $$n+1$$ contenant les dimensions des matrices et doit renvoyer le nombre minimal de produits scalaires que l'on doit effectuer afin de multiplier ces $$n$$ matrices ainsi que le parenthésage optimal lié à ce nombre.

Testez votre implémentation pour une suite de matrices dont les dimensions sont données par la séquence $$[5, 10, 3, 12, 5, 50, 6]$$, c'est-à-dire que la matrice $$M_1$$ est de dimension $$5 \times 10$$, la matrice $$M_2$$ est de dimension $$10 \times 3$$, etc. Votre programme doit renvoyer pour cet exemple $$2010$$ comme nombre minimal de produit scalaires à effectuer. Le parenthésage optimal associé à ce nombre est $$((M_1M_2)((M_3M_4)(M_5M_6))).$$

## *Egg drop*

Supposons que nous nous retrouvons devant un très haut immeuble avec un sac rempli d'œufs. Tous nos œufs sont identiques et très durs à casser. On s'intéresse à savoir quel est l'étage le plus haut duquel on peut lâcher un œuf sans qu'il ne se casse. Cependant, on souhaite répondre à cette question en cassant le moins d'œufs possible. Notre problème algorithmique peut alors se formuler de la façon suivante : 

*Étant donné le nombre d'étages de l'immeuble et le nombre d'œufs disponibles, quel est le nombre minimum d'essais qu'on doit faire afin de déterminer l'étage critique, c'est-à-dire l'étage à partir duquel tous les œufs se cassent.*

Pour cela nous faisons plusieurs suppositions :

* Un œuf qui survit à une chute peut être réutilisé.

* Un œuf cassé doit être éliminé.

* L'effet de la chute est le même pour tous les œufs.

* Si un œuf se casse lorsqu'il est lâché d'un étage $$i$$, alors tout œuf se cassera s'il est lâché d'un étage $$j \ge i$$.

* Inversement, si un œuf survit à une chute de l'étage $$i$$, alors aucun œuf ne se cassera s'il est lancé d'un étage $$j \leq i$$.

* Il est tout à fait possible qu'un œuf se casse dès le rez-de-chaussée et on ne peut pas exclure le fait que les œufs puissent survivre à une chute du dernier étage.


#### Cas $$n = 1$$

Si nous ne possédons qu'un seul œuf, il n'y a qu'une seule façon de procéder : on lance d'abord l'œuf depuis l'étage 1, ensuite depuis l'étage 2, puis 3, etc. jusqu'à ce que soit l'œuf se casse soit il survit à une chute du tout dernier étage. Dans le pire cas, cette procédure nécessitera $$h$$ étapes, et $$h$$ est alors la réponse à notre problème.

#### Problème général avec $$n$$ œufs et $$h$$ étages.

La stratégie consiste à lâcher un œuf de chaque étage possible (de $$1$$ à $$h$$) et calculer récursivement le nombre minimal de lâchers nécessaires dans le pire cas. L'étage qui donne la valeur minimale dans le pire cas fera partie de la solution.

## Sous-structure optimale

Quand on lâche un œuf d'un étage $$x$$, deux cas sont possibles :

1. **L'œuf se casse**. Si l'œuf se casse à l'étage $$x$$, alors nous n'avons qu'à vérifier avec les œufs restants les étages inférieurs à $$x$$. Le problème est dans ce cas réduit à un problème avec $$x-1$$ étages et $$n-1$$ œufs.

2. **L'œuf ne se casse pas**. Si l'œuf ne se casse pas après l'avoir lâché de l'étage $$x$$, alors nous n'avons qu'à tester les étages supérieurs à $$x$$. Dans ce cas, notre problème se réduit à un problème avec $$h-x$$ étages et $$n$$ œufs.

Puisque nous cherchons à minimiser le nombre d'essais dans le pire cas, on considère la valeur maximale de ces deux cas et on choisit l'étage qui donne le nombre minimal d'essais.

On note `eggDrop(n,h)` le nombre minimal d'essais pour trouver l'étage critique (celui à partir duquel les œufs se brisent). Cette valeur peut être calculée de façon récursive en utilisant l'équation récursive suivante :

$$\mathtt{eggDrop}(n,h) = 1 + \min_{x \in \{1, \dots h\}} \max(\mathtt{eggDrop}(n-1, x-1), \mathtt{eggDrop}(n, h-x)) $$ 


**:**{:.exercise} 

Écrire une fonction en Python, qui prend en entrée le nombre d'œufs $$n$$ et le nombre d'étages $$h$$ et qui renvoie le nombre optimal d'essais en se basant sur l'équation de récurrence ci-dessus.

Testez que pour $$n = 2$$ et $$h = 10$$ votre programme renvoie $$4$$. Testez l'efficacité de votre programme pour des valeurs plus grandes. Que se passe-t-il ? Pourquoi ? 

## Résoudre le problème à l'aide de la programmation dynamique. 

Si vous dessinez l'arbre de la récursivité pour des petites valeurs de $$n$$ et de $$h$$ vous allez remarquer qu'avec l'approche précédente, certains sous-problèmes sont résolus plus d'une fois. Comme c'est le cas d'autres problèmes typiques de la programmation dynamique, le re-calcul des mêmes sous-problèmes peut être évité en sauvegardant les solutions de chaque sous-problème dans un tableau. Ce tableau sera rempli des valeurs les plus petites aux valeurs les plus élevées. 

**:**{:.exercise}

Concevoir un algorithme et l'implémenter ensuite en Python pour résoudre le problème selon les principes de la programmation dynamique.
