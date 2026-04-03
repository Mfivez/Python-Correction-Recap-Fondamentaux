class Feuille:
    def __init__(self, taille_definie_user: float, couleur_definie_user: str, grammage_definie_user: float):
        self.taille = taille_definie_user
        self.couleur = couleur_definie_user
        self.grammage = grammage_definie_user

    def remplir(self):
        print("Je gribouille sur la feuille.")