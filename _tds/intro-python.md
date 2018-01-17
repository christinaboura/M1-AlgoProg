---
title: Introduction à Python
---

Python est un langage de programmation orienté objet (mais oublions le côté objet pour l'instant). Sa première version a été écrite par Guido van Rossum qui était un grand fan de Monty Python. Ici, nous allons utiliser la version 3 du langage qui apporte beaucoup de modifications par rapport aux versions précédentes. 

Ce mini-tutoriel est une introduction très basique et rapide à la syntaxe et aux règles du langage. Si vous voulez approfondir plus, plein de tutoriels bien faits existent sur le net, n'hésitez pas à les consulter.

Pendant ces TP nous allons travailler avez l'environnement `Jupyter` et l'interpréteur `python3`. Tout cela est disponible sur les cartables numériques, mais aussi [en ligne](https://sage.prism.uvsq.fr/hub/login). Cliquez sur `New --> Python 3` pour créer un nouveau notebook. `python3` est aussi accessible directement dans un terminal : tapez `python3` pour lancer l'interpréteur. 

## Python en mode calculatrice

La plus simple utilisation que vous pouvez faire de Python est de l'utiliser comme une simple calculatrice. Vous pouvez essayer dans le terminal les calculs suivants :

~~~python
>>> 2+6
8
>>> 10 - 12   # Les espaces sont optionnels
-2
>>> 13 + 2*4  # La priorité des opérations est comme d'habitude
21
>>> 21 / 4    # Attention ! En Python 2 cette instruction retourne 
5.25          # la partie  entière de la division. En Python 3 c'est  
              # une division flottante, même entre deux entiers
>>> 21 // 4   # Partie entière de la division
5
>>> 21 % 4    # Reste de la division
1
>>> 3 ** 4    # Opérateur puissance (3 à la puissance 4)
81
>>> 10 < 2 * 13  # Comparaison
True
>>> 10 < 4 or not 10 < 4  # Connecteurs booléens
True
>>> 1 < 2 == 1 + 1 < 3   # Comparaisons chaînées
True
~~~

**:**{:.exercise} Calculer :


- $$5 \cdot (1293 - 390)$$,

- La partie entière ainsi que le reste de la division de 1234 par 7,

- $$13^{13}$$.


## Données et variables

Pour pouvoir accéder aux données qu'un programme manipule on fait usage d'un nombre de **variables** de différents types. Une variable apparaît dans un langage de programmation sous son *nom de variable*, mais il ne s'agit de rien d'autre qu'une référence désignant l'adresse mémoire où sont stockées les données.

En Python il existe un nombre de règles simples sur les noms de variables qu'il faut respecter :

* Seules les lettres a -> z,  A -> Z, les chiffres 0-9 et le caractère '`_`' sont autorisés.
* Le nom d'une variable doit toujours commencer par une lettre.
* La casse est significative. Par exemple `vitesse`, `Vitesse` et `VITESSE` désignent des variables différentes.

Une bonne habitude à prendre est d'écrire les noms de variables en minuscules y compris la première lettre. Il s'agit d'une convention qui est largement respectée. N'utilisez les majuscules qu'à l'intérieur du nom afin de faciliter la lisibilité. Par exemple : `matriceDesCoefficients`.

Le signe '`=`' est utilisé afin d'affecter une valeur à une variable. 

~~~python
>>> n = 5
>>> message = 'Bonjour'
>>> pi = 3.14
~~~


On peut affecter une valeur à **plusieurs variables simultanément**. 

~~~python
>>> x = y = z = 1
>>> x
1
>>> y
1
>>> z
1
~~~

On peut aussi effectuer des **affectations parallèles**.

~~~python
>>> x, y = 3.5, 7
>>> x
3.5
>>> y
7
~~~

En Python, contrairement à d'autres langages de programmation, il n'est pas nécessaire d'écrire des lignes de code spécifiques pour définir le type des variables avant de pouvoir les utiliser. Il suffit d'assigner une valeur à un nom de variable pour que celle-ci soit automatiquement créée avec le type qui correspond à la valeur fournie. On dit alors que Python est un langage à **typage dynamique**, contrairement aux langages à **typage statique** comme c'est le cas des langages C ou Java. De plus, les variables peuvent changer de type au gré des affectations. On peut vérifier ceci avec l'opérateur `type`.

~~~python
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

* **Fonction** `print()`. Pour afficher une valeur à l'écran, il existe deux possibilités. Soit, on entre au clavier le nom de la variable et ensuite on appuie sur *Enter* (comme on a fait jusqu'à ici), soit on peut utiliser la fonction `print()`.

~~~python
>>> n = 3.5
>>> print(n)
3.5
>>> msg = 'Ça va ?'
>>> print(msg)
Ça va ?
~~~

**Attention** cependant à la différence entre `print a` (Python 2) et `print(a)` (Python 3).

On peut combiner texte et variables dans une même fonction `print()`.

~~~python
>>> poids = 3.67
>>> print("Le poids du nouveau-né est", poids, "kilos.")
Le poids du nouveau-né est 3.67 kilos.
~~~

**:**{:.exercise}

 Soient deux points de l'espace $$A$$ et $$B$$.  Déclarez 4 variables $$x_A$$, $$x_B$$, $$y_A$$ et $$y_B$$ correspondant aux coordonnées réelles de ces deux points et affectez-leur des valeurs. Calculez la distance entre $$A$$ et $$B$$, donnée par la formule $$\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$, et affichez le résultat à l'écran sous la forme *La distance entre $$A$$ et $$B$$ est : .*

**Attention !** Vous devez utiliser pour cet exercice la méthode `math.sqrt()`. Pour utiliser cette méthode il faut d'abord importer le module math, avec l'instruction `import math`.

## Contrôle du flux d'exécution 

Dans la plupart des programmes que vous allez écrire vous aurez besoin d'utiliser des instructions qui permettront au programme de suivre des chemins différents selon les circonstances. Pour ceci il est nécessaire de disposer d'instructions capables de *tester une certaine condition* et de modifier le comportement du programme en conséquence.

L'instruction qui est sans doute la plus utile afin de permettre un tel comportement est l'instruction `if`. Son fonctionnement sous Python est très simple. Si la condition à droite du mot-clé `if` est vraie, alors le bloc d'instructions en dessus est exécuté. 

~~~python
>>> if age > 18 :
...     print("La personne peut acheter de l'alcool.")
~~~

#### Indentation

En Python, les instructions composées (comme c'est le cas de l'instruction `if`, mais aussi des instructions `while`, `for` et des *fonctions* que nous verrons plus tard) ont toujours la même structure : une *ligne d'entête* terminée par un *deux-points*, suivie d'un bloc d'instructions indenté sous la ligne d'entête. Toutes les instructions de ce bloc **doivent être indentées exactement au même niveau**. Une convention très respectée est d'utiliser un décalage de 4 espaces. 

Avec une telle convention, il est inutile de marquer le début et la fin d’un bloc par des éléments du langage (comme des accolades { et } en C ou Java , ou les mots réservés `begin` et `end` dans certains autres langages).

Pour cette raison, en Python on n'est pas libres d'insérer des retours
à la ligne partout comme en C. Les retours à la ligne sont
*obligatoires* à la fin d'une instruction, et *permis* à l'intérieur
des parenthèses. En effet, ce code n'est pas correct :

~~~python
if a < 1
    and b < 2:
    print('hello')
~~~

alors que ce code l'est :

~~~python
if (a < 1
    and b < 2):
    print('hello')
~~~

On peut, si on le souhaite ajouter une instruction `else`  pour exécuter un autre bloc si la condition est fausse :

~~~python
>>> if age > 18:
...     print("La personne peut acheter de l'alcool.")
... else:
...     print("Trop jeune !")
~~~

Plutôt que d’emboîter des instructions `if`, on peut utiliser une instruction `if` suivie par une ou plusieurs instructions `elif` (raccourci de *else if*):

~~~python
>>> if n == 0:
...     print("Le nombre est égal à zéro")
... elif n > 0:
...     print("Le nombre est positif")
... else:
...     print("Le nombre est négatif") 
~~~

**:**{:.exercise}

Déclarez une variable et affectez lui un entier naturel. Testez en utilisant les instructions `if` et `else` si l'entier est pair ou impair et affichez le résultat.

**:**{:.exercise}

Déclarez trois variables `a`, `b` et `c` correspondant aux coefficients de l'équation quadratique $$ax^2 + bx + c = 0$$. Calculez le discriminant $$\Delta = b^2 - 4ac$$ de l'équation. Testez en utilisant les instructions `if`, `elif` et `else` la valeur du déterminant et calculez la ou les solutions de l'équation. Si le déterminant est négatif, affichez le message "*L'équation n'a pas de solutions*".

## Boucles

Très souvent dans nos programmes nous avons besoin de répéter un certain nombre d'instructions plusieurs fois. Python, comme probablement tous les autres langages que vous connaissez, possède dans ce but les instructions `while` et `for`.

* La boucle `while` permet d'itérer un bloc d'instructions tant qu'une condition reste vraie.  

~~~python
>>> a = 0
>>> while a < 10: # N'oubliez pas le deux-points !
...     print(a)   # N'oubliez pas l'indentation !
...     a += 2
... 
0
2
4
6
8
~~~

Avant d'introduire l'instruction `for` parlons un peu de la fonction `range()`. Cette fonction peut nous être très utile lorsque on veut itérer sur une suite de nombres. Elle génère des progressions arithmétiques.

~~~python
range(2, 10) # 2, 3, 4, 5, 6, 7, 8, 9
range(0, 15, 2) # 0, 2, 4, 6, 8, 10, 12, 14
range(10, -50, -10) # 10, 0, -10, -20, -30, -40
~~~


La boucle `for` est très utile lorsque on veut répéter un bloc d'instructions un nombre des fois connu à l'avance. Si on veut par exemple imprimer tous les nombres de 0 à 5, voici comment on peut le faire à l'aide de l'instruction `for` et de la de la fonction `range`.

~~~python
>>> for i in range(6): # N'oubliez pas le deux-points !
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

**:**{:.exercise} 

Initialisez deux entiers : `a = 0` et `b = 15`.
Écrivez une boucle qui affiche et incrémente la valeur de `a` tant qu’elle reste inférieure
à celle de `b`.

Écrivez ensuite une autre boucle qui décrémente la valeur de `b` et affiche sa valeur seulement si elle est
impaire. Itérez tant que `b` est supérieur à 0.

**:**{:.exercise}

Affichez la somme des cubes de tous les multiples de 3 compris entre 0 et 99 inclus. Utilisez pour cela l'instruction `for` et la fonction `range()`.

## Fonctions

Pour créer une fonction en Python, on commence par le mot-clé `def` (définition). Il doit être suivi par le nom de la fonction, la liste des paramètres entre parenthèses et un deux-points '`:`'. Le corps de la fonction commence à la ligne suivante et doit être écrit avec un retrait de quelques espaces.

Voici une fonction qui imprime les `n` premiers termes  de la suite *Fibonacci*.

~~~python
>> def fibonacci(n):
...     a, b = 0, 1
...     for i in range(20):
...         print(a, end=' ')
...         a, b = b, a + b
...     print(a)
... 
>>> fibonacci(20)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
~~~

On peut bien sûr écrire une fonction qui nous renvoie quelque chose. Ceci se fait avec le mot-clé `return`.
Voici une fonction qui renvoie la somme des carrés des entiers de 0 à `n`.

~~~python
>>> def sommeCarres(n):
...     sum = 0
...     for i in range(n):
...         sum += i**2
...     return sum
... 
>>> sommeCarres(20)
2470
>>> 
~~~

Vous trouverez plus d'informations sur les fonctions en Python ici : [docs.python.org](https://docs.python.org/3.1/tutorial/controlflow.html#)

**:**{:.exercise}

Écrivez une fonction `tableDeMultiplication(base, fin)` qui prend en paramètre un entier `base` et un entier `fin`
et affiche à l'écran les `fin` premiers éléments de la  table de multiplication de l'entier `base`.

Par exemple :

~~~python
>>> tableDeMultiplication(3, 10)
0 3 6 9 12 15 18 21 24 27
~~~

## Listes

Les listes sont des structures ordonnées de données. En Python, une liste est définie à l'aide des crochets.

~~~python
nombres = [2,5,13,-35,0]
fromages = ['roquefort', 'camembert', 'saint-nectaire', 'comté']
~~~

On peut accéder aux données d'une liste à l'aide de leur indice associé.

~~~python
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

~~~python
>>> len(nombres)
5
>>> len(fromages)
4
~~~

Il existe plusieurs manières de créer une liste. Voici quelques unes :

* Liste vide

~~~python
>>> liste = []
~~~

* On peut créer une liste en indiquant à la création les éléments qu'elle doit contenir. Vous pouvez remarquer qu'une liste peut contenir d'éléments ayant des types variés.

~~~python
>>> liste = ['ac/dc', 42, 3.14]
~~~

* La syntaxe des *compréhensions de listes* permet de générer une liste par une boucle.

~~~python
>>> liste = [i for i in range(20)]
>>> print(liste)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
~~~

* Liste contenant le carré de tous les entiers de 0 à 9.

~~~python
>>> liste = [i ** 2 for i in range(10)]
>>> print(liste)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
~~~

On peut parcourir une liste à l'aide d'une boucle `for`,

~~~python
>>> nombres = [9, 13, -2, 25, 31, 7, 4]
>>> sum = 0
>>> for i in nombres:
...     sum += i
>>> print(sum)
87
~~~

où à l'aide d'une boucle `while`.

~~~python
>>> i = 0
>>> sum = 0
>>> while i < len(nombres):
...     sum += i
...     i += 3
>>> print(sum)
9
~~~

On peut tester si un élément est dans la liste à l'aide de l'instruction `in`.

~~~python
>>> print(-2 in nombres) 
True
>>> print(8 in nombres) 
False
~~~

Les listes sont des objets (comme tout autre type en Python). Il existe plusieurs méthodes déjà définies pour la classe `list` de Python, qu'on peut utiliser pour nos listes. Pour utiliser une méthode sur une liste, on écrit le nom de la liste, suivi d'un '`.`', suivi du nom de la méthode. 

Voici quelques méthodes qui peuvent vous  être utiles.

* La méthode `append(x)` qui permet d'ajouter un élément `x` à la fin d'une liste.

~~~python
>>> liste = [0, 3, 1, 5.0, 6, 4.3]
>>> liste.append(7)
>>> print(liste)
[0, 3, 1, 5.0, 6, 4.3, 7]
~~~

* La méthode `insert(index,x)`qui insère l'élément `x` à la position `index` de la liste.

~~~python
>>> liste.insert(3, 13.2)
>>> liste
[0, 3, 1, 13.2, 5.0, 6, 4.3, 7]
~~~

* La méthode `remove(x)` qui supprime de la liste le premier élément `x` trouvé.

~~~python
>>> liste.remove(13.2)
>>> liste
[0, 3, 1, 5.0, 6, 4.3, 7]
~~~

Cette liste des méthodes est loin d'être exhaustive. Vous pouvez trouver plus d'informations sur la page [docs.python.org](https://docs.python.org/3.1/tutorial/datastructures.html).

**:**{:.exercise}

Définissez la liste `liste = [34, 0, -17, 5, 18, 9]`, puis effectuez les actions suivantes :

- Triez et affichez la liste.

- Ajoutez l’élément 15 à la fin de la liste et affichez la.

- Renversez et affichez la liste.

- Affichez l’indice de l’élément -17.

- Enlevez l’élément 5 et affichez la liste.

- Affichez la sous-liste du $$2^e$$ au $$3^e$$ élément.

- Affichez la sous-liste du début au $$4^e$$ élément.

- Affichez la sous-liste du $$3^e$$ élément à la fin de la liste.

- Affichez l'avant dernier élément en utilisant un indiçage négatif.

**:**{:.exercise}

Modifier la fonction `fibonacci(n)` de la Section 5 afin qu'elle renvoie une liste avec les `n` premiers termes de la suite Fibonacci.

# Exercices

Vous êtes prêts maintenant à écrire par vous mêmes des programmes un peu plus longs et compliqués. Le mode terminal que nous avons utilisé jusqu'ici n'est plus très adapté. Pour cette raison vous allez utiliser des *scripts* pour écrire, sauvegarder et modifier vos programmes. Pour écrire un script il suffit dans votre compte [SageMathCloud](https://cloud.sagemath.com/) de cliquer sur `New` et créer un fichier dont le nom se termine par `.py` afin d'indiquer qu'il s'agit bien d'un script Python. Vous pouvez ensuite l'exécuter dans un terminal en écrivant

~~~
python3 monPremierScript.py
~~~

## Crible d'Ératosthène

Le crible d'Ératosthène est un algorithme qui permet de trouver tous les nombres premiers qui sont inférieurs à un certain entier naturel $$N$$. Cet algorithme est dû au mathématicien grec Ératosthène de Cyrène qui est également connu pour être la première personne à avoir mesuré le méridien terrestre.

L'idée du crible est très simple. On commence par écrire la liste de tous les nombres de $$2$$ jusqu'à $$N$$. Ensuite on barre (on enlève de la liste) tous les multiples de $$2$$. On note ensuite le plus petit nombre non-barré de la liste, qui est donc le nombre 3, et on procède de façon similaire en enlevant tous ses multiples. On continue de la même façon jusqu'à atteindre le nombre $$N$$. Les nombres qui restent à la fin  sont exactement les nombres premiers plus petits ou égaux à $$N$$.

Vous pouvez voir une jolie animation de l'exécution de l'algorithme sur la page <https://fr.wikipedia.org/wiki/Crible d'Ératosthène>.

**Remarque**. En réalité, il suffit de tester uniquement les multiples des nombres de 2 à $$\sqrt{N}$$, puisque un nombre composé plus petit ou égal à $$N$$, a forcément un facteur plus petit ou égal à $$\sqrt{N}$$.

Vous devez maintenant programmer le crible d'Ératosthène en  Python. Écrivez une fonction `eratosthene(N)` qui prend comme paramètre un entier naturel $$N$$ et qui affiche à l'écran la liste de tous les nombres premiers plus petits ou égaux à $$N$$. Il existe plusieurs façons de coder cet algorithme en Python, vous êtes libres de faire à votre propre guise. 

## Recherche dichotomique

La recherche dichotomique est un algorithme très simple et efficace pour rechercher un élément dans une liste triée. 

Imaginez par exemple que nous souhaitons retrouver le numéro de téléphone d'une personne dans un annuaire qui est trié par ordre alphabétique. La recherche séquentielle, c.-à-d. parcourir l'annuaire du début en comparant tous les noms avec celui dont on cherche le numéro de téléphone peut être très longue (surtout si le nom recherché se trouve à la fin de l'annuaire). Une approche bien plus efficace est d'ouvrir l'annuaire au milieu et commencer par regarder si le nom se trouve à cette page. Si ce n'est pas le cas, et si le nom dont on cherche se trouve plus loin, alors on recommence la recherche avec la deuxième moitié de l'annuaire. Si le nom se trouve avant, alors on recommence avec la première moitié. 

On peut voir qu'avec cette approche, on réduit à chaque étape la taille de l'annuaire à parcourir de la moitié. Cet algorithme fait partie alors des algorithmes dits *diviser pour régner* et a une complexité *logarithmique* en la taille de la liste.

Pour cet exercice, on suppose que l'utilisateur possède une liste croissante de nombres et on lui fournit un nombre qu'on suppose être dans la liste. Le but est de retourner l'indice du nombre recherché dans la liste.

Si la liste fournie est [1,3,4,6,10,14,15] et l'élément qu'on cherche est 10, alors le programme doit retourner 4 (souvenez-vous que, dans une liste, les indices sont numérotés à partir de 0).

Écrivez une fonction `rechercheDichotomique(valeur, listeTriee)` qui prend en entrée une liste triée de nombres et une valeur à rechercher dans la liste et renvoie l'indice de la liste correspondant à cette valeur.





