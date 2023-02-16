#coding:utf-8

"""
mode d'ouvertures: r, w, a, x -> (lecture / ecriture), r+ (lecture / ecriture dans un meme fichier);
    open(NomVarFic, modeLecture) -> ouvrir
    nomVarFic.close() -> fermer
   if nomVarFic.closed -> verifier si fermer
   nomVarFic.read() -> lire le contenu du fichier (readline -> une ligne, readlines -> toute les lignes comme liste)

autre mode :
    with open(nomFile, modeOuv) as NomVar :
     // code...
     pas besoin de fermeture

"""
fic = open("file.txt", "r");


content = fic.read()
print(content)
fic.close()
if  fic.closed:
    print("closed\n")

with open("file.txt", "r") as fichier:
    content = fichier.readline()
    print(content)
content = "Bonjour les amis"
with open("file.txt", "w") as fichier:
    fichier.write(content "\n")
with open("file.txt", "r") as fichier:
    content = fichier.readlines()
    print(content)

