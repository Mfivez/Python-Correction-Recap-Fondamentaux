from compte_bancaire import CompteBancaire

compte = CompteBancaire("Alice")

compte.afficher_solde()
compte.deposer(100)
compte.retirer(30)
compte.afficher_solde()

# Utilisation du getter
print("Solde actuel :", compte.solde)

# Utilisation du setter
compte.solde = 200
compte.afficher_solde()

# Tentative invalide
compte.solde = -50