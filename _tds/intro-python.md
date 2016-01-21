---
title: Introduction à Python
---

Python est un langage de programmation orienté objet. Sa première version a été écrite par Guido van Rossum qui était un grand fan de Monty Python. Allez sur [SageMathCloud](https://cloud.sagemath.com/).

## Syntaxe

~~~
a = 1 + 1
print(a)
~~~
{:.python}

Attention à la différence entre `print a` (Python 2) et `print(a)` (Python 3).

~~~
def syntaxe_devinee_automatiquement(self, *is, **python):
	for i in range(10):
		print('You cannot fool me')
~~~

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





