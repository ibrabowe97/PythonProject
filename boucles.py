#encoding:utf-8;

compteur =1;
while compteur <4:
    print("hello mama\n");
    compteur+=1;
jeu=True;
#on fait un petit jeu
"""
en fait : continue revient au debut de la boucle et break arrete la boucle

"""
while jeu:
    choix=input("voulez-vous jour?\n");
    if choix == "oui":
        continue
    elif choix == "non":
        break;
    else:
        print("faites un choix");
else:
    print('bye bye')
    exit('a bientot')
nom="ibrahima";
for letter in nom:
    print(letter);