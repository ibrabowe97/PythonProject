#coding:utf-8;
# voici une liste

liste=[1, 2, 3, 4, 5]
print(liste)
for p, n in enumerate(liste):
    print(f"{p}:{n}")

""" 
    les tuples:
        sont immuables donc pas possible de les modifier;
        syntaxe -> nomTuple = (valeur,); tuple, faut toujours mettre une virgule.
         note: un tuple contient une seule valeur.
         
         usage: definir des constantes, declaration multiples, retourner des valeurs multiples
"""
monTuple = (13,34)
# print(monTuple)
for i in monTuple:
    print("tuple :", i)
(nombre1, nombre2) = (64, 45)
# print(dir(liste))
print(nombre1)
print(nombre2)
