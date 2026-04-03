class Stylo:
    def __init__(self, couleur_definie_user: str, type_pointe_defini_user: str, est_cartouche_definie_user_vide: bool):
        self.couleur = couleur_definie_user
        self.type_pointe = type_pointe_defini_user
        self.est_cartouche_vide = est_cartouche_definie_user_vide

    def ecrire(self, feuille):
        if self.est_cartouche_vide:
            print('Le stylo est vide')
        else:
            print("J'écris sur la feuille.")