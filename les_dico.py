#coding:utf-8

"""
    classType = dict;

    syntaxe: NomDico = {key:value}
    acces : nomDico[<cle>]
    ajout et modif : nomDico[<cle>] = <valeur>
"""
dico = {"age": "24ans","name":"ibrahima diallo"}
print(dico["age"])
# print(dico[age])
# help(dico)
print(len(dico))
for i,j in dico.items() :
    print(i,":",j)
dico["chien"] = "le chien est un carnivore puissant"
# print(dico)
# print(type(dico))
print(dir(dico))

valeur = dico.popitem()
print(valeur)
# print(dico)
# eq(dico,dico)
dico1 = dico
# print(dico1)
dico1["chat"] = "minou"
# print(dico1)
# print(dico)
# dico1.clear()
valeur=dico1.get("chat")
print(valeur)
# dico1.setdefault( 1997)
# print(dico1)


