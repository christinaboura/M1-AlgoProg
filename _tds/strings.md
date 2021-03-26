---
title: String matching
---

## Algorithme de Rabin-Karp

L'objectif de cette partie est d'implanter l'agorithme de *string
matching* de Rabin-Karp.

On rappelle qu'en Python les chaînes de caractères se comportent comme
des tableaux:

```python
>>> s = "Hello world!"
>>> len(s)
12
>>> s[0]
'H'
>>> s[4]
'o'
>>> s[-1]
'!'
>>> s[0:5]
'Hello'
>>> s[:3]
'Hel'
>>> s[6:]
'world!'
>>> s[:-1]
'Hello world'
```

On ne s'autorisera que les opérations ci-dessus pour implanter nos
algorithmes. En effet, ce serait de la triche d'utiliser

```python
s.index('ello')
1
```

**:**{:.exercise}

Implanter l'algorithme de *string matching* naïf: coder une fonction
`match(string, pattern)` qui renvoie la position de la première
occurrence de `pattern` dans `string`.

Tester votre algorithme sur le génome de l'*Escherichia coli* (souche
K-12, MG1655), que vous pouvez télécharger dans la variable `genome`
avec les commandes suivantes:

```python
from requests import get
from gzip import decompress

req = get('ecoli.gz')
genome = decompress(req.content).decode()[71:]
```
{:#ecoli}

<script>
$("#ecoli .s").textContent = `'${String(location).replace('strings', 'ecoli.gz')}'`;
</script>

Alternativement, si vous avez du mal à télécharger depuis le notebook
jupyter, [téléchargez le fichier ici](ecoli.gz), mettez-le dans le
même dossier que votre notebook, et chargez-le avec

```python
from gzip import open

genome = open('ecoli.gz').read().decode()[71:]
```

Trouvez la première occurrence de la séquence `GATTACA`.

**:**{:.exercise}

Modifiez votre code pour trouver toutes les occurrences de `pattern`,
en une seule passe sur `string`.

**:**{:.exercise}

Réalisez une fonction `rabin_karp(string, pattern, mod)` implantant
l'algorithme de Rabin-Karp. Le paramètre `mod` est un entier
paramétrant l'algorithme. Vous êtes libres d'optimiser l'algorithme
pour la recherche de séquences d'ADN (pour mémoire, l'ADN est codé par
quatre symboles: `A`, `G`, `C`, et `T`).

Testez votre algorithme en cherchant le gène dit *"aaaD"*:

```
GTGAATATATCGAACAGTCAGGTTAACAGGCTGCGGCATTTTGTCCGCGCCGGGCTTCGC
TCACTGTTCAGGCCGGAGCCACAGACCGCCGTTGAATGGGCGGATGCTAATTACTATCTC
CCGAAAGAATCCGCATACCAGGAAGGGCGCTGGGAAACACTGCCCTTTCAGCGGGCCATC
ATGAATGCGATGGGCAGCGACTACATCCGTGAGGTGAATGTGGTGAAGTCTGCCCGTGTC
GGTTATTCCAAAATGCTGCTGGGTGTTTATGCCTACTTTATAGAGCATAAGCAGCGCAAC
ACCCTTATT
```


ainsi que le gène dit *"accC"*:

```
ATGCTGGATAAAATTGTTATTGCCAACCGCGGCGAGATTGCATTGCGTATTCTTCGTGCC
TGTAAAGAACTGGGCATCAAGACTGTCGCTGTGCACTCCAGCGCGGATCGCGATCTAAAA
CACGTATTACTGGCAGATGAAACGGTCTGTATTGGCCCTGCTCCGTCAGTAAAAAGTTAT
CTGAACATCCCGGCAATCATCAGCGCCGCTGAAATCACCGGCGCAGTAGCAATCCATCCG
GGTTACGGCTTCCTCTCCGAGAACGCCAACTTTGCCGAGCAGGTTGAACGCTCCGGCTTT
ATCTTCATTGGCCCGAAAGCAGAAACCATTCGCCTGATGGGCGACAAAGTATCCGCAATC
GCGGCGATGAAAAAAGCGGGCGTCCCTTGCGTACCGGGTTCTGACGGCCCGCTGGGCGAC
GATATGGATAAAAACCGTGCCATTGCTAAACGCATTGGTTATCCGGTGATTATCAAAGCC
TCCGGCGGCGGCGGCGGTCGCGGTATGCGCGTAGTGCGCGGCGACGCTGAACTGGCACAA
TCCATCTCCATGACCCGTGCGGAAGCGAAAGCTGCTTTCAGCAACGATATGGTTTACATG
GAGAAATACCTGGAAAATCCTCGCCACGTCGAGATTCAGGTACTGGCTGACGGTCAGGGC
AACGCTATCTATCTGGCGGAACGTGACTGCTCCATGCAACGCCGCCACCAGAAAGTGGTC
GAAGAAGCGCCAGCACCGGGCATTACCCCGGAACTGCGTCGCTACATCGGCGAACGTTGC
GCTAAAGCGTGTGTTGATATCGGCTATCGCGGTGCAGGTACTTTCGAGTTCCTGTTCGAA
AACGGCGAGTTCTATTTCATCGAAATGAACACCCGTATTCAGGTAGAACACCCGGTTACA
GAAATGATCACCGGCGTTGACCTGATCAAAGAACAGCTGCGTATCGCTGCCGGTCAACCG
CTGTCGATCAAGCAAGAAGAAGTTCACGTTCGCGGCCATGCGGTGGAATGTCGTATCAAC
GCCGAAGATCCGAACACCTTCCTGCCAAGTCCGGGCAAAATCACCCGTTTCCACGCACCT
GGCGGTTTTGGCGTACGTTGGGAGTCTCATATCTACGCGGGCTACACCGTACCGCCGTAC
TATGACTCAATGATCGGTAAGCTGATTTGCTACGGTGAAAACCGTGACGTGGCGATTGCC
CGCATGAAGAATGCGCTGCAGGAGCTGATCATCGACGGTATCAAAACCAACGTTGATCTG
CAGATCCGCATCATGAATGACGAGAACTTCCAGCATGGTGGCACTAACATCCACTATCTG
GAGAAAAAACTCGGTCTTCAGGAAAAATAA
```

Comparez les performances avec la méthode naïve, et avec différentes
valeurs pour `mod`, en utilisant la clef magique `%time`.


## Automates finis

L'objectif de cette partie est d'implanter l'agorithme de *string
matching* par automates finis vu en cours.

**:**{:.exercise}

On considère l'automate fini représenté par la structure de données
Python suivante:

```python
automate = {
    0: { 'a': 1 },
    1: { 'b': 2, 'a': 1 },
    2: { 'a': 3 },
    3: { 'a': 4, b: 2 },
    4: { 'b': 5, 'a': 1 },
    5: { 'a': 6 },
    6: { 'a': 7, b: 2 },
    7: { 'a': 8, b: 5 },
    8: { 'a': 1, b: 2 },
}
```

Où chaque ligne représente un état, l'état `0` étant l'état de départ
et l'état `8` étant l'état d'acceptation, et le dictionnaire associé à
chaque état représentant les transitions (le retour à l'état `0` est
représenté implicitement par l'absence d'une lettre dans la liste des
transitions).

Dessiner à la main cet automate. Quel *pattern* reconnaît-il ?

**:**{:.exercise}

Écrire une fonction `match(string, automaton)` qui prend en entrée une
chaîne de caractères `string`, et un automate représenté comme au
point précédent, et qui renvoie les positions de toutes les
occurrences du *pattern* dans `string`.

Tester la fonction sur l'automate précédent.

**:**{:.exercise}

Écrire une fonction qui calcule l'automate à partir d'un
*pattern*. Tester sur les génomes de la partie précédente.

