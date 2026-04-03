from jouable import Jouable


class Chanson(Jouable):
    def __init__(self, titre, artiste, duree, genre):
        self.titre = titre
        self.artiste = artiste
        self._duree = 0
        self.genre = genre
        self.set_duree(duree)

    def jouer(self):
        print(f"Lecture de la chanson : {self.titre} par {self.artiste} [{self.genre.value}]")

    def get_duree(self):
        return self._duree

    def set_duree(self, duree):
        if duree > 0:
            self._duree = duree
        else:
            print("Erreur : la durée doit être positive.")

    def __str__(self):
        return f"Chanson({self.titre}, {self.artiste}, {self._duree} min, {self.genre.value})"
