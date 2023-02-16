#encoding:utf-8

"""
    declaration d'une variable:
        nomVariable = valeurVariable;
"""

age = 15
print(type(age));
print(f"age=", age);
agePersonne="l'age de la fille vaut : {}";
print(agePersonne.format(age));

ageIbra= 26
print(f"ibrahima est age de {ageIbra} ans");
print("ibrahima est age de {} ans".format(ageIbra));
nom = 'Ibrahima'
prenom = 'Diallo'
print(nom+' '+prenom)
autreNom = input('quel est ton nom toi ? \n')
print('bonjour {}'.format(autreNom));

