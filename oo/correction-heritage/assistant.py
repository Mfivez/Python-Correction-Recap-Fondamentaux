from etudiant import Etudiant
from professeur import Professeur

class Assistant(Etudiant, Professeur):
    def __init__(self, nom, age, matiere, notes=None):
        Etudiant.__init__(self, nom, age, notes)
        Professeur.__init__(self, nom, age, matiere)
        
    def se_presenter(self):
        # utilise la version Etudiant (grâce à l’ordre MRO)
        presentation = super().se_presenter()
        return presentation + f" En plus, j’assiste en {self.matiere}."