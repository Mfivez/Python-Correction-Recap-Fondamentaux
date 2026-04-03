from jouable import Jouable

class Podcast(Jouable):
    def __init__(self, titre, animateur, duree):
        self.titre = titre
        self.animateur = animateur
        self._duree = 0
        self.set_duree(duree)

    def jouer(self):
        print(f"Lecture du podcast : {self.titre} animé par {self.animateur}")

    def get_duree(self):
        return self._duree

    def set_duree(self, duree):
        if duree > 0:
            self._duree = duree
        else:
            print("Erreur : la durée doit être positive.")

    def __str__(self):
        return f"Podcast({self.titre}, {self.animateur}, {self._duree} min)"
