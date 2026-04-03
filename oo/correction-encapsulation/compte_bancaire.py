class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire # attribut public
        self.__solde = solde # attribut privé


    # Getter (lecture du solde)
    @property
    def solde(self):
        return self.__solde

    # Setter (modification du solde)
    @solde.setter
    def solde(self, valeur):
        if valeur < 0:
            print("Erreur : le solde ne peut pas être négatif.")
        else:
            self.__solde = valeur

    def afficher_solde(self):
        print(f"Solde de {self.titulaire} : {self.__solde} €")

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Dépôt de {montant} € effectué.")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if montant <= 0:
            print("Montant invalide.")
        elif montant > self.__solde:
            print("Fonds insuffisants.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué.")