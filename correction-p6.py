# 1

# def diviser(numerateur: float, denominateur: float) -> float:
#     try:
#         result = numerateur / denominateur

#     except ZeroDivisionError:
#         result = None
#         print("Division par 0, c'est non !")

# diviser(1, 0)

# 2

# try:
#     saisie = input("Entre des nombres :")
#     listNb = [int(n) for n in saisie.split()]
# except ValueError:
#     print("Veuillez entrer uniquement des nombres")

# print(sum(listNb))

# 3

# try:
#     saisie = int(input("Entre un nombre :"))
#     print(f"Merci, vous avez saisi {saisie}")
# except ValueError:
#     print('Erreur, entre un nombre')

# 4
i = 0
int_list = list()

for i in range(5):
    non_valide = True

    while non_valide:
        try:
            saisie = int(input("Entrez un nombre :"))
            int_list.append(saisie)
            non_valide = False
        except:
            print("Ce n'est pas un entier")

print(int_list)