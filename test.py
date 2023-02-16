#coding:utf-8

""" 
ceci est un commentaire 

        print(".git/")
        print("Hello World")
        print("Welcome \0to my training ")

"""
"""
        type() : permet de montrer le type d'une variable
"""
agePersonne = 15
print("age de la personne vaut :",agePersonne)
nomPersonne ="Ibrahima diallo"
print(nomPersonne)
print(type(nomPersonne)) #affiche le type de la variable nomPersonne
continuerRevision = True
print(continuerRevision)
exaDecimal = 0xFDABE
print(exaDecimal)

"""
Fonction vues:
                print(): afficher a l'ecran
                input(): lire a partir de la rentree standard, toujours en string
                int(), float(), bool(), str() : pour "caster" une variable
                str.format() : pour formatage (mise en forme )
"""
#formatage : la fonction ".format()"
texte ="l'age de la personne vaut :{} ans et son nom est {}"
#formatage via une variable:
print(texte.format(agePersonne,nomPersonne))
#formatage direct dans print:
print("l'age de la personne vaut :{} ans et son nom est {}".format(agePersonne, nomPersonne))

# nomJoueur = input("Saisir le nom de Messi:")
# print("Bravo {} etait bien le nom correct".format(nomJoueur))

# prixHT = input("donnez le prix hors taxe :")
# prixHT = int(prixHT)
# prixTT = prixHT + (prixHT * 18/100)
# print("le prix tout taxe vaut:", prixTT)

booleen = input("saisir la valeur booleen :")
booleen = str(booleen)
print("la valeur entiere de True est : {}".format(booleen))