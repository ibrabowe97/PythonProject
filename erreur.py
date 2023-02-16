#coding:utf-8;

"""
	Gestion Erreur:
		"try/except"
		"else/finally"
		"raise/assert"
		"pass"
			on fait un try sur une seule instruction. c'est bcp plus propre
		"else" et "finally" -> pour donner d'autres instructions
		le "finally" -> permet d'afficher une instruction a la fin du "try" meme s'il n'y a pas d'erreur

	type d'erreurs: (les plus frequentes)
		ZeroDivisionError; ValueError; NameError; TypeError
		OSError; AssertionError; KeyError

"""
age=input("Donnez l'age de l'utilisateur:\n")
try:
	age=int(age)
except:
	print("erreur de donnees\n")
else:
	print("Vous avez", age, "ans")
finally:
	print("Merci d'avoir utiliser mon petit programme\n")

n=input("entrer une valeur\n")

try:
	n=int(n)
	if n < 0:
		raise ValueError("Nombre negatif")
# except ValueError:
	# print("Vous devez entrer un nombre positif")

finally :
	print("merci")



