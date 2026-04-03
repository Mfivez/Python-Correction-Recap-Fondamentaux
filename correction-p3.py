compteur_for = 0;
compteur_while = 0;
compteur_do_while = 0;

while (compteur_while < 10):
    print(compteur_while)
    compteur_while +=1

while True:
    print(compteur_do_while)

    compteur_do_while += 1

    if (compteur_do_while == 10):
        break

for compteur_for in range(10):
    print(compteur_for)


# 2

import random

nb_random = random.randint(1, 10);
nb_vie = 5

while (nb_vie > 0):
    essai = int(input("Devinez le nombre : "))

    if (essai == nb_random):
        print('Bravo')
        break;
    else:
        nb_vie -= 1

with open("fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read();