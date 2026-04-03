from jouable import Jouable
from chanson import Chanson

class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self._pistes = []

    def ajouter_piste(self, piste):
        if isinstance(piste, Jouable):
            self._pistes.append(piste)
        else:
            print("Erreur : l'objet ajouté n'est pas jouable.")

    def lire_playlist(self):
        print(f"\nLecture de la playlist : {self.nom}")
        for piste in self._pistes:
            piste.jouer()

    def filtrer_par_genre(self, genre):
        nouvelle_playlist = Playlist(f"{self.nom} - {genre.value}")
        i = 0

        while i < len(self._pistes):
            piste = self._pistes[i]
            if isinstance(piste, Chanson) and piste.genre == genre:
                nouvelle_playlist.ajouter_piste(piste)
            i += 1

        return nouvelle_playlist

    def duree_totale(self):
        total = 0
        for piste in self._pistes:
            total += piste.get_duree()
        return total

    def afficher_pistes(self):
        print(f"\nPlaylist : {self.nom}")
        for piste in self._pistes:
            print(piste)
