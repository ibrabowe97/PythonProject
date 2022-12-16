#encoding:utf-8

"""
    les fonctions vues:
        print(); input(); type(); int(); float(); str(); bool(); 
        format();
    
    comment creer une fonction:
        nomage: meme condition que les variables;
        def : pour dire que c'est une fonction;
        (): pour mettre des parametres (ou pas) il faut mettre les parentheses;
        et faire une tabulations pour mettre les instructions des la fonction;

        notion de parametre:
        on peut donner des valeur par defaut au paremetre en faisant ceci:
            (nomVar=valeur);
        (*nomVar): ceci veut nombre infini d'arguments;
        

"""
### fonction avec argumentL
def dire(nom_personne, message):
    print("{} {}".format(nom_personne, message));

dire("ibrahima", "vous dit bonjour");
#fonction avec argument avec valeur par defaut predefini:
def fonction(nom="Ibrahima", age=26, mess="bye"):
    print("{} {} {}".format(nom, age, mess));

fonction("abdoul", age=23, mess="hello")

# fonction avec argument infini:
def fonctionInfini(*ListeItems):
    for item in ListeItems:
        print(item)

Liste =["ibrahima", "tidiane", "merci", 23]
fonctionInfini(12, 23.4, 45.5, "hello", "victoire", Liste)


