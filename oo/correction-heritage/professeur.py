from personne import Personne

class Professeur(Personne):
    def __init__(self, nom, age, matiere):
        super().__init__(nom, age)
        self.matiere = matiere

    def se_presenter(self):
        return f"Je suis le professeur {self.nom} et j’enseigne la matière {self.matiere}."