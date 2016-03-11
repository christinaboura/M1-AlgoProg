---
title: Algèbre linéaire
---

Ce TD est à développer **exclusivement** dans un *notebook* Jupyter.

- Dans SageMathCloud, créez un nouveau notebook via l'onglet
  _« ⊕ New »_, en cliquant sur le bouton _« Jupyter Notebook »_.
  Ensuite modifiez le noyau à travers le menu de Jupyter en cliquant
  _« Kernel → Change kernel → Python 3 »_.

- Dans un cartable numérique, tapez la commande
  
  ~~~
  ipython3 notebook
  ~~~
  
  pour lancer un notebook. À la fin de la session, vous pouvez
  sauvegarder votre travail en cliquant _File → Download as →
  IPython Notebook (.ipynb)_, et en transférant le fichier sur votre
  clef usb.

- Alternativement, vous pouvez
  [installer Jupyter](http://jupyter.readthedocs.org/en/latest/install.html)
  sur votre propre machine.

## Arithmétique naïve des matrices

Nous allons enrichir la classe `Matrice`, créée au
[TD précédent](graphes), avec les méthodes pour les opérations
arithmétiques de base : addition, négation, multiplication.

Nous avons déjà appris à définir la méthode spéciale `__repr__` pour
contrôler l'affichage d'un objet Python. D'autres méthodes spéciales
permettent de définir un comportement lorsque un objet est combiné
avec un opérateur arithmétique.  Par exemple, le code suivant permet
de définir un comportement pour l'addition :

~~~python
>>> class MaxPlus:
...     def __init__(self, val):
...         self.val = val
... 
...     def __repr__(self):
...         return str(self.val)
... 
...     def __add__(self, other):
...         return MaxPlus(max(self.val, other.val))
... 
>>> MaxPlus(10) + MaxPlus(2)
10
~~~

Voici une liste des méthodes spéciales qui nous intéressent pour les
matrices :

| Méthode spéciale | opération | opérateur
|-
| `__add__(self, other)` | addition | `a+b`
| `__sub__(self, other)` | soustraction | `a-b`
| `__mul__(self, other)` | mulitplication | `a*b`
| `__truediv__(self, other)` | division exacte | `a/b`
| `__neg__(self)` | négation unaire | `-a`
| `__invert__(self)` | inverse | `~a`
| `__eq__(self, other)` | test d'égalité | `a==b`
{:.pretty style="margin:auto"}

À l'exception de `__neg__` et `__invert__`, qui représentent des
opérations unaires, toutes les méthodes prennent deux paramètres : le
premier est l'opérande gauche, le deuxième l'opérande
droit.[^operands] À l'exception de `__eq__`, qui donne une valeur
booléene, toutes les autes méthodes doivent donner un objet en retour,
typiquement un nouvel objet appartenant à la même classe et
représentant le résultat de l'opération.

[^operands]: C'est toujours la méthode de la classe de l'opérande
	gauche qui est appelée. Python ne donne aucune garantie sur la classe
	de l'opérande droit, c'est la responsabilité du développeur de
	vérifier que l'opérande droit peut bien être combiné avec l'opérande
	gauche.

**:**{:.exercise} Implanter la méthode `__eq__` pour la classe
`Matrice`. Deux matrices sont égales si et seulement si toutes leurs
entrées sont égales.

**:**{:.exercise} Implanter les méthodes `__add__`, `__neg__` et
`__sub__` pour la classe `Matrice`.

**:**{:.exercise} Implanter la méthode `__mul__` pour la classe
`Matrice`, en utilisant l'algorithme de multiplication naïf.


## Algorithme de multiplication de Strassen

On rappelle les formules de Strassen. Étant données deux matrices
$$A=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$$ et
$$X=\bigl(\begin{smallmatrix}x&y\\z&t\end{smallmatrix}\bigr)$$, à
coefficients dans un anneau non-commutatif, le produit $$AX$$ se
calcule comme suit :

$$\begin{align}
q_1 &= a(x + z),\\
q_2 &= d(y + t),\\
q_3 &= (d − a)(z − y),\\
q_4 &= (b − d)(z + t),\\
q_5 &= (b − a)z,\\
q_6 &= (c − a)(x + y),\\
q_7 &= (c − d)y;
\end{align}$$

$$AX = \begin{pmatrix}
q_1 + q_5 & q_2 + q_3 + q_4 - q_5\\
q_1 + q_3 + q_6 - q_7 & q_2 + q_7\\
\end{pmatrix}.$$

**:**{:.exercise} Ajouter une méthode `strassen` à la classe
`Matrice`, qui calcule le produit de deux matrices carrées en
utilisant la méthode de Strassen récursive.

**Note :** Pour simplifier, on pourra se limiter à implanter une
méthode qui multiplie des matrices de taille une puissance de 2.

### Comparer les performances

Nous voulons maintenant comparer les performances des méthodes naïve
et de Strassen, afin de mesurer la taille à partir de laquelle la
deuxième devient intéressante.

Le notebook Jupyter nous permet de faire ces mesures aisément. La
*clef magique* `%time` permet de mesurer le temps d'exécution d'une
instruction Python. Par exemple

~~~python
%time A.strassen(X)
~~~

affichera plusieurs informations sur le temps d'exécution de la
méthode `strassen`. La clef magique `%timeit` fait des mesures plus
précises en exécutant plusieurs fois la même instruction, et en
prenant une moyenne.

**:**{:.exercise} Déterminer le point où l'algorithme de Strassen
*croise* l'algorithme naïf.

**:**{:.exercise} Optimiser la méthode de Strassen en arrêtant la
récursion en dessous d'un seuil déterminé expérimentalement.

## Solution de systèmes

**:**{:.exercise} Implanter une méthode `solve` qui prend en entrée un
vecteur $$b$$, et qui calcule une solution au système $$Ax=b$$ par la
méthode de Gauss.

**:**{:.exercise} Implanter la méthode `__invert__` pour inverser une
matrice carrée (**suggestion :** vous pouvez utiliser la méthode
`solve` de façon répétée).
