#coding:utf-8
"""
quelques methodes sur les listes:
	.clear() -> effacer, 
	.index(<valeur>) -> trouver l'index, 
	
	.count(<valeur>) -> compter le nombre de fois qu'un element est present dans une liste
	.sort() -> trier
	.insert(<indice>, <valeur>) -> inserer
	.reverse() -> trier par ordre decroissant
	.append()
	.remove(<valeur a supprimer>)
	.deepcopy(<nomListe>) -> copie une liste

	sorted() -> trier
	del(liste[<indice>])
	extend(nomListe) -> etendre une liste par une autre.
	enumerate(nomListe) -> faire un parcours avec recuperation d'indice des elements de la liste

	split() -> transformer une chaine en liste
		{
			nomListe = nomChaine.split("<separateur>")
		}

	join() -> passer de liste a chaine
		{
			nomVar = "<separateur>".join(nomListe)
		}

acces et affichage:
	liste[x] - affiche l'element a l'indice x
	liste[-x] - affiche l'element x en partant de la fin

	liste[:] - affiche tout les elements
	liste[x:] - affiche les x derniers elements
	liste[:x] - affiche les x premiers elements
	liste[x:y] - affiche les elements entre les indices x et y (y exclus)

"""
inventaire = list();
invent = [];
# print (invent);
# print(inventaire);

# invent = [7] * 3
# print (invent);
# invent = range(10);

# print (invent);

# for val in invent:
# 	print(val)

inventaire = ["ibrahima", 'diallo', '26', 'ans']

phrase =" ".join(inventaire)
# print(phrase)
help(list)

# for i in inventaire:
# 	print(i)

# print(inventaire[1]); # affiche l'element a l'indice 1
# print(inventaire[-1]); # affiche l'element a l'indice 1 en partant de la fin

#print(inventaire[:]); # affiche tout les elements de la listes

print("\t", inventaire[:2]) # affiche les deux premiers elements
print("\n==========================\n")
print("\t",inventaire[2:]) # affiche tout les elements de la liste a partir de l'indice 2 

# print(inventaire[1:5]) # affiche les elements de l'indice 1 a 5 


inventaire[3] = "salut" # modifie l'element d'indice 3 
# print(inventaire[:])

# inventaire[:] = ["merci"] * len(inventaire) # remplace tout les elements de la liste par "merci"
# print(inventaire[:])

# inventaire[:] = ["merci"] # ecrase toute la liste et la remplace par "merci"
# print(inventaire[:])

# if "diallo" in inventaire:
# 	print("je m'appelle ibrahima")
# else:
# 	print("je ne suis pas ibrahima");

invent = []

# print(invent)

invent.append("ibrahima")
# print(invent)

invent.append("diallo")
# print(invent)

invent.insert(1, "khaly")
# print(invent)
invent.append("diallo")
invent.append("diallo")
invent.append("diallo")
invent.append("diallo")
# print(invent)
invent.remove("diallo") # permet de supprimer la valeur en question
# print(invent)

# del invent[1] # permet de supprimer la valeur a l'indice 5
# print(invent)

indice = invent.index("khaly")
# print (indice)

invent.sort() # trier par ordre croissant

# print(invent[1])

sorted(inventaire) # trier par ordre croissant
# print(inventaire)

invent.reverse() # trier par ordre decroissant
# print(invent)
# print(invent[1])
# print("nombre de diallo =", invent.count("diallo"))