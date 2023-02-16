#coding:utf-8;

"""
	modularite : 
		importer un module: 
			import <nomDuModule> as alias; (as alias est facultatif)
			from <nomModule> import <unFonctionDuModule>

"""
import math as m # -> on importe la bibliotheque "math" pour utiliser des fonctions de mathematiques
import les_fonctions as f # on importe le fichier "les_fonctions.py"
result= int(m.sqrt(100))
# print(result)

from math import sqrt # a partir de la bibliotheque "math" on import la fonction "sqrt()" seulement
result = int(sqrt(25))

# print(f.calcul(2, 4))
 	#tester un fichier a inclure:
if __name__ == "__les_fonctions__":
	calcul(2,5)
