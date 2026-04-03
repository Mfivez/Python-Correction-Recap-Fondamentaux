from assistant import Assistant
from ecole import Ecole
from personne import Personne
from professeur import Professeur
from etudiant import Etudiant

p1 = Personne("Mauritcio", 25)
e1 = Etudiant("Lionel", 17, [14, 16])
e1.ajouter_note(18)
p2 = Professeur("Le M", 35, "Mathématiques")
a1 = Assistant("Le N", 22, "Informatique", [15, 17])

ecole = Ecole()
ecole.ajouter_personne(p1)
ecole.ajouter_personne(e1)
ecole.ajouter_personne(p2)
ecole.ajouter_personne(a1)

ecole.afficher_tous()