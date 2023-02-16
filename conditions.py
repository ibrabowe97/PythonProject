#encoding:utf-8
"""
    operateurs de comparaison :
        egalite              : ==
        superieur (ou egale) : >  (>=)
        inferieur (ou egale) : <  (<=)
        different            : !=

    conditions multiples: 
            and  -> (et) il est equivalent a < && >
            or   ->(ou)  ----------------- a < || >
            in   ->(dans) 
            not  -> (non ceci ou cela) --- a < ! >

"""
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

# le sinon si :
elif 18<= age < 50:
    print("vous etes adultes\n");

# le sinon :
else:
    print("vous etes vieux\n");
victoire= 12;
if victoire:
    print("WOOOOWWW\n");

# le sinon et le contraire :
elif not victoire:
    print("courage...\n");
else:
    print("continue a apprendre");
