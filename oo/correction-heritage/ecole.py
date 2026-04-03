class Ecole:
    def __init__(self):
        self._personnes = []

    def ajouter_personne(self, p):
        self._personnes.append(p)

    def afficher_tous(self):
        for personne in self._personnes:
            print(personne.se_presenter())