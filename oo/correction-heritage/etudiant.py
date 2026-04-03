from personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, notes=None):
        Personne.__init__(self, nom, age)
        self._notes = notes if notes is not None else []

    def ajouter_note(self, note):
        self._notes.append(note)

    @property
    def notes(self):
        return self._notes

    def se_presenter(self):
        return f"Je m'appelle {self.nom}, j'ai {self.age} ans et mes notes sont : {self._notes}."