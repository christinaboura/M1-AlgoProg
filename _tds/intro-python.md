---
title: Introduction à Python
---

Python est un très joli langage. Allez sur [SageMathCloud](https://cloud.sagemath.com/).

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

# Exercices

## Crible d'Ératosthène

Le crible d'Ératosthène est un algorithme qui permet de trouver tous les nombres premiers qui sont inférieurs à un certain entier naturel $$N$$. Cet algorithme est dû au mathématicien grec Ératosthène de Cyrène qui est également connu pour être la première personne à avoir mesuré le méridien terrestre.

L'idée du crible est très simple. On commence par écrire la liste de tous les nombres de $$2$$ jusqu'à $$N$$. Ensuite on barre (on enlève de la liste) tous les multiples de $$2$$. On note après le plus petit nombre non-barré de la liste, qui est donc le nombre 3, et on procède de façon similaire en enlevant tous les ses multiples. On continue de la même façon jusqu'à attendre le nombre $$N$$. Les nombres qui restent à la fin  sont exactement les nombres premiers plus petits ou égaux à $$N$$.

Vous pouvez voir une jolie animation de l'exécution de l'algorithme sur la page https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne.

$Remarque$. En réalité, il ne suffit de tester que les multiples des nombres de 2 à $$\sqrt{N}$$, puisque un nombre composé plus petit ou égal à $$N$$, a forcément un facteur plus petit que $$\sqrt{N}$$.

Vous devez maintenant programmer le crible d'Ératosthène en  Python. Écrivez une fonction `Eratosthene` qui prend comme paramètre un entier naturel $$N$$ et qui affiche à l'écran la liste de tous les nombres premiers plus petits ou égaux à $$N$$. Il existe plusieurs façons de coder cet algorithme en Python, vous êtes libres à faire à votre propre guise. 

## Recherche dichotomique



