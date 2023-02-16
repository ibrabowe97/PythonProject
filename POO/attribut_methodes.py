#coding:utf-8;
# declaration d'une classe
class Humain:
    # creation du constructeur:
    def __init__(self, c_prenom, c_age):
        print("creation d'une classe Humaine...")
        self.prenom = c_prenom
        self.age = c_age

print("\n\tdebut du programme...\n")

# instenciation d'une classe :
humain1 = Humain('Abdoul', 23)
print(humain1.prenom)
print(humain1.age)

# instenciation d'une classe :
humain2 = Humain('Moussa', 22)
print(humain2.prenom)
print(humain2.age)
print("\n")