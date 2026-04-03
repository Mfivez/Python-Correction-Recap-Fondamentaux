from enum import Enum

# # 1
# entree_utilisateur = int(input("Nb Entier : "))

# if (entree_utilisateur % 2 == 0):
#     print("pair")
# else:
#     print("impair")

# # 2
# note_utilisateur = int(input("Une note : "))

# if note_utilisateur > 80 and note_utilisateur <= 100:
#     print("Parfait")
# elif note_utilisateur > 50:
#     print("Moins bien")
# elif note_utilisateur > 30:
#     print("C'était pas loin...")
# else:
#     print("Nul")

# # 2.2
# note_utilisateur = int(input("Une note : "))

# match (note_utilisateur):
#     case _ if note_utilisateur > 80 and note_utilisateur <= 100:
#         grade = "Parfait"
#     case _ if note_utilisateur > 50:
#         grade = "Moins bien"
#     case _ if note_utilisateur > 30:
#         grade = "C'était pas loin..."
#     case _:
#        grade = "Nul"

# print(grade)

# 3

class TypeCafe(Enum):
    LATTE = 0
    CAPPUCCINO = 1
    ESPRESSO = 2

class TailleCafe(Enum):
    PETIT = 0
    MOYEN = 1
    GRAND = 2


type_cafe = int(input("""
    Entrez un type de café :
        0. Latte
        1. Cappuccino
        2. Espresso
"""))

taille_cafe = int(input("""
    Entrez la taille du café :
        0. Petit
        1. Moyen
        2. Grand
"""))

nbr_cafe = int(input("""
    Entrez le nombre de café : 
"""))

prix = 0

match (type_cafe):
    case TypeCafe.LATTE.value:
        prix = 8
    case TypeCafe.CAPPUCCINO.value:
        prix = 12
    case TypeCafe.ESPRESSO.value:
        prix = 5

coef = 0
match (taille_cafe):
    case TailleCafe.PETIT.value:
        coef = 1 
    case TailleCafe.MOYEN.value:
        coef = 1.5
    case TailleCafe.GRAND.value:
        coef = 2  

prix_tot = coef * prix * nbr_cafe

prix_final = prix_tot

if (prix_tot > 100 ):
    prix_final = prix_tot * 0.85
elif (prix_tot > 50):
    prix_final = prix_tot * 0.90
elif (prix_tot > 20):
    prix_final = prix_tot * 0.95


print(f"""
type : {list(TypeCafe)[type_cafe] }
taille : {list(TailleCafe)[taille_cafe] }
nombre : { nbr_cafe }
prix sans réduc : { prix_tot }
prix avec réduc : { prix_final }
""")
