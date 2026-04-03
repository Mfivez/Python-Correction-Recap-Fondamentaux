from jouable import Jouable

class Publicite(Jouable):
    def __init__(self, marque, duree):
        self.marque = marque
        self._duree = 0
        self.set_duree(duree)

    def jouer(self):
        print(f"Publicité en cours : découvrez les offres de {self.marque}")

    def get_duree(self):
        return self._duree

    def set_duree(self, duree):
        if duree > 0:
            self._duree = duree
        else:
            print("Erreur : la durée doit être positive.")

    def __str__(self):
        return f"Publicite({self.marque}, {self._duree} min)"
