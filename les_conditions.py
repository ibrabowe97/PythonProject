#encoding:utf-8

id="ibrahima"
mdp="bowePlus"

print("interface connexion")
user_id=input("entrer votre id:\n")
user_mdp=input("saisir le mot de passe:\n")

if id == user_id:
    print("bienvenue Mr ", user_id)
if mdp == user_mdp:
    print("votre mot de passe est correct")
age=input("donnez votre age:\n")
age=int(age);
if 0 < age< 18:
    print("vous etes pre-adultes\n");
elif 18<= age < 50:
    print("vous etes adultes\n");
else:
    print("vous etes vieux\n");
victoire= 12;
if victoire:
    print("WOOOOWWW\n");
elif not victoire:
    print("courage...\n");
else:
    print("continue a apprendre");
