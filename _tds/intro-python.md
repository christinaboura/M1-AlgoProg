---
title: Introduction à Python
---

Python est un langage de programmation orienté objet. Sa première version a été écrite par Guido van Rossum qui était un grand fan de Monty Python. Allez sur [SageMathCloud](https://cloud.sagemath.com/).

## Python en mode calculatrice

La plus simple utilisation que vous pouvez faire du Python est de l'utiliser comme une simple calculatrice. Vous pouvez ouvrir un terminal et essayer les calculs suivants :

~~~
>>> 2+6
8
>>> 10 - 12   # Les espaces sont optionnels
-2
>>> 13 + 2*4  # La priorité des opération est comme d'habitude
21
>>> 21 / 4    # Attention ! En Python 2 cette instruction retourne la partie entière de la division
5.25          # En Python3 c'est une division flottante, même entre deux entiers
>>> 21 // 4   # Partie entière de la division
5
>>> 21 % 4    # Reste de la division
1
>>> 3 ** 4    # Opérateur puissance (3 à la puissance 4)
81         
~~~


## Données et variables

Pour pouvoir accéder aux données qu'un programme manipule on fait usage d'un nombre de variables de différents types. Une variable apparaît dans un langage de programmation sous son *nom de variable*, mais il ne s'agit de rien d'autre qu'une référence désignant l'adresse mémoire où seront stockés les données.

En Python il existe un nombre de règles simples sur les noms de variables qu'il faut respecter :

* Seules les lettres a -> z,  A -> Z, les chiffres 0-9 et le caractère `_` sont autorisés.
* La casse est significative. Par exemple `vitesse`, `Vitesse` et `VITESSE` désignent des variables différentes.

Une bonne habitude à prendre est d'écrire les noms de variables en minuscules y compris la première lettre. Il s'agit d'une convention qui est largement respectée. N'utilisez les majuscules qu'à l'intérieur du nom afin de faciliter la lisibilité. Par exemple : `matriceDesCoefficients`.

Le signe '`=`' est utilisé afin d'affecter une valeur à une variable. 

~~~
>>> n = 5
>>> message = 'Bonjour'
>>> pi = 3.14
~~~


On peut affecter une valeur à **plusieurs variables simultanément**. 

~~~
>>> x = y = z = 1
>>> x
1
>>> y
1
>>> z
1
~~~

On peut aussi effectuer des **affectations parallèles**.

~~~
>>> x, y = 3.5, 7
>>> x
3.5
>>> y
7
~~~

En Python, contrairement à d'autres langages de programmation, il n'est pas nécessaire d'écrire des lignes de code spécifiques pour définir le type des variables avant de pouvoir les utiliser. Il suffit d'assigner une valeur à un nom de variable pour que celle-ci soit automatiquement créé avec le type que correspond au mieux à la valeur fournie. On dit alors que Python est un langage à **typage dynamique**, contrairement aux langages au **typage statique** comme c'est la cas des langages C ou Java. De plus, les variables peuvent changer le type au gré des
affectations. On peut vérifier ceci avec l'opérateur `type`.

~~~
>>> x = 3
>>> type(x)
<class 'int'>
>>> x = 3.5
>>> type(x)
<class 'float'>
>>> x = 'message'
>>> type(x)
<class 'str'>
~~~


* **La fonction** `print()` Pour afficher une valeur à l'écran, il existe deux possibilités. Soit, on entre au clavier le nom de la variable et ensuite *<Enter>* (comme on a fait jusqu'à ici), soit on peut utiliser la fonction `print()`. 

~~~
>>> n = 3.5
>>> print(n)
3.5
>>> msg = 'Ça va ?'
>>> print(msg)
Ça va ?
~~~

**Attention** cependant à la différence entre `print a` (Python 2) et `print(a)` (Python 3).


## Boucles

Très souvent dans nos programmes nous avons besoin de répéter un certain nombre d'instructions plusieurs fois. Python, comme probablement tous les autres langages que vous connaissez, possède dans ce but les instructions `while` et `for`.

* La boucle `while` permet d'itérer un bloc d'instructions tant qu'une condition reste vraie.  

~~~
>>> a = 0
>>> while a < 10 : # N'oubliez pas le double point !
...     print(a)   # N'oubliez pas l'indentation !
...     a += 2
... 
0
2
4
6
8
~~~

Avant d'introduire l'instruction `for` parlons un peu de la fonction `range()`. Cette function peut nous être très utile lorsque on veut itérer sur une suite de nombres. Elle génère des progressions arithmétiques.

~~~
range(2, 10) # 2, 3, 4, 5, 6, 7, 8, 9
range(0, 15, 2) # 0, 2, 4, 6, 8, 10, 12, 14
range(10, -50, -10) # 10, 0, -10, -20, -30, -40
~~~


La boucle `for` est très utile lorsque on veut répéter un bloc d'instructions un nombre des fois connu à l'avance. Si on veut par exemple imprimer tous les nombres de 0 à 5, voici comment on peut le faire à l'aide de l'instruction `for` est de la de la fonction `range`.

~~~
>>> for i in range(6) : # N'oubliez pas le double point !
...     print(i)        # N'oubliez pas l'indentation !
...
0
1
2
3
4
5
~~~

Comme on va le voir un peu plus tard, la boucle `for` peut être utilisée très facilement pour parcourir les éléments d'une liste.

## Fonctions

Pour créer une fonction en Python, on commence par le mot-clé `def` (définition). Il doit être suivi par le nom de la fonction, la liste des paramètres en parenthèse et un double point '`:`'. Le corps de la fonction commence à la ligne suivante et doit être écrit avec un retrait de quelques espaces.

Voici une fonction qui imprime les `n` premiers termes  de la suite *Fibonacci*.

~~~
>> def fibonacci(n) :
...     a, b = 0, 1
...     for i in range(20) :
...         print(a, end = ' ')
...         a, b = b, a + b
...     print(a)
... 
>>> fibonacci(20)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
~~~

On peut bien sûr écrire une fonction qui nous renvoie quelque chose. Ceci se fait avec le mot-clé `return`.
Voici une fonction qui renvoie la somme des carrés des entiers de 0 à `n`.

~~~
>>> def sommeCarres(n) :
...     sum = 0
...     for i in range(n) :
...         sum += i**2
...     return sum
... 
>>> sommeCarres(20)
2470
>>> 
~~~

Vous trouverez plus d'informations sur les fonctions en Python ici : [docs.python.org](https://docs.python.org/3.1/tutorial/controlflow.html#)

## Listes

Les listes sont des structures ordonnées de données. En Python, une liste est définie à l'aide des crochets.

~~~
nombres = [2,5,13,-35,0]
fromages = ['roquefort', 'camembert', 'saint-nectaire', 'comté']
~~~

On peut accéder aux données d'une liste à l'aide de leur indice associée.

~~~
>>> print(nombres[2])
13
>>> print(fromages[0])
roquefort
>>> print(fromages[-1])
comté
>>> print(nombres[0:3])
[2, 5, 13]
~~~

On peut accéder à la taille d'une liste à l'aide de la fonction `len()`. Elle renvoie le nombre d'éléments présents dans la liste.

~~~ 
>>> len(nombres)
5
>>> len(fromages)
4
~~~

Il existe plusieurs manières de créer une liste. Voici quelques unes :

* Liste vide

~~~ 
>>> liste = []
~~~

* On peut créer une liste vide en lui indiquant directement à la création les éléments qu'elle doit contenir. Vous pouvez remarquer qu'une liste peut contenir d'éléments ayant des types variés.

~~~ 
>>> liste = ['ac/dc', 42, 3.14]
~~~

* Liste contenant tous les nombres entiers de 0 à 19.

~~~ 
>>> liste = [i for i in range(20)]
>>> print(liste)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
~~~

* Liste contenant le carré de tous les entiers de 0 à 9.

~~~ 
>>> liste = [i ** 2 for i in range(10)]
>>> print(liste)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
~~~

On peut parcourir une liste à l'aide d'une boucle `for`,

~~~ 
>>> nombres = [9, 13, -2, 25, 31, 7, 4]
>>> sum = 0
>>> for i in nombres :
...     sum += i
>>> print(sum)
87
~~~

où à l'aide d'une boucle `while`.

~~~
>>> i = 0
>>> sum = 0
>>> while i < len(nombres) :
...     sum += i
...     i += 3
>>> print(sum)
9
~~~

On peut tester si un élément est dans la liste à l'aide de l'instruction `in`.

~~~ 
>>> print(-2 in nombres) 
True
>>> print(8 in nombres) 
False
~~~

Les listes sont des objets, comme de toute façon à peu près tout en Python. Il existe plusieurs méthodes déjà prêts pour la classe `list` de Python, qu'on peut utiliser pour nos listes. Pour utiliser une méthode sur une liste, on écrit le nom de la liste, suivi d'un '`.`', suivi du nom de la méthode. 

Voici quelques méthodes utiles qui peuvent vous  être utiles.

* La méthode `append(x)` qui permet d'ajouter un élément `x` à la fin d'une liste.

~~~
>>> liste = [0, 3, 1, 5.0, 6, 4.3]
>>> liste.append(7)
>>> print(liste)
[0, 3, 1, 5.0, 6, 4.3, 7]
~~~

* La méthode `insert(index,x)`qui insère l'élément `x` à la position `index` de la liste.

~~~
>>> liste.insert(3, 13.2)
>>> liste
[0, 3, 1, 13.2, 5.0, 6, 4.3, 7]
~~~

* La méthode `remove(x)` qui supprime de la liste le premier élément `x`retrouvé.

~~~
>>> liste.insert(3, 13.2)
>>> liste
[0, 3, 1, 13.2, 5.0, 6, 4.3, 7]
~~~

Cette liste des méthodes est loin d'être exhaustive. Vous pouvez trouver plus d'informations sur la page [docs.python.org](https://docs.python.org/3.1/tutorial/datastructures.html).

# Exercices

## Crible d'Ératosthène

Le crible d'Ératosthène est un algorithme qui permet de trouver tous les nombres premiers qui sont inférieurs à un certain entier naturel $$N$$. Cet algorithme est dû au mathématicien grec Ératosthène de Cyrène qui est également connu pour être la première personne à avoir mesuré le méridien terrestre.

L'idée du crible est très simple. On commence par écrire la liste de tous les nombres de $$2$$ jusqu'à $$N$$. Ensuite on barre (on enlève de la liste) tous les multiples de $$2$$. On note après le plus petit nombre non-barré de la liste, qui est donc le nombre 3, et on procède de façon similaire en enlevant tous les ses multiples. On continue de la même façon jusqu'à attendre le nombre $$N$$. Les nombres qui restent à la fin  sont exactement les nombres premiers plus petits ou égaux à $$N$$.

Vous pouvez voir une jolie animation de l'exécution de l'algorithme sur la page <https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne>.

**Remarque**. En réalité, il ne suffit de tester que les multiples des nombres de 2 à $$\sqrt{N}$$, puisque un nombre composé plus petit ou égal à $$N$$, a forcément un facteur plus petit ou égal à $$\sqrt{N}$$.

Vous devez maintenant programmer le crible d'Ératosthène en  Python. Écrivez une fonction `Eratosthene(N)` qui prend comme paramètre un entier naturel $$N$$ et qui affiche à l'écran la liste de tous les nombres premiers plus petits ou égaux à $$N$$. Il existe plusieurs façons de coder cet algorithme en Python, vous êtes libres à faire à votre propre guise. 

## Recherche dichotomique

La recherche dichotomique est un algorithme très simple et efficace pour rechercher un élément dans une liste triée. 

Imaginez par exemple que nous souhaitons retrouver le numéro de téléphone d'une personne dans un annuaire qui est trié par ordre alphabétique. La recherche séquentielle, ç.-à-d. parcourir l'annuaire du début en comparant tous les noms avec celui dont on cherche le numéro de téléphone peut être très longue (surtout si le nom recherché se trouve à la fin de l'annuaire). Une approche bien plus efficace est d'ouvrir l'annuaire au milieu et commencer par regarder si le nom se trouve à cette page. Si ce n'est pas le cas, et si le nom dont on cherche se trouve plus loin, alors on recommence la recherche avec la deuxième moitié de l'annuaire. Si le nom se trouve avant, alors on recommence avec la première moitié. 

On peut voir qu'avec cette approche, on réduit à chaque étape la taille de l'annuaire à parcourir à la moitié. Cet algorithme fait partie alors des algorithms dits *diviser pour régner* et a une complexité *logarithmique* en la taille de la liste.

Pour cet exercice, on suppose que l'utilisateur possède une liste croissante des nombres et on lui fourni un nombre qu'on suppose être dans la liste. Le but est de retourner l'indice du nombre recherche dans la liste.

Si la liste fournie est [1,3,4,6,10,14,15] est l'élément dont on cherche est 10, alors le programme doit retourner 4 (rappelez vous que dans une liste, les indices sont numérotés à partir de 0).

Ecrivez une fonction `triDichotomique(valeur, listeTriee)` qui prend en entrée une liste triée des nombres et une valeur à rechercher dans la liste et renvoie l'indice de la liste correspondant à cette valeur.





