class CompteBancaire:
    def __init__(self, montant):
        self.__montant = montant  # Attribut privé

    @property
    def montant(self):
        return self.__montant

    @montant.setter
    def montant(self, montant):
        if (montant <= self.__montant):
            self.__montant -= montant
        else:
            print('montant insuffisant')


    def retirer_argent(self, montant):
        self.montant(montant);

    def retirer_1000(self):
        self.montant(1000);







# Exemple d'utilisation
tel = CompteBancaire("0123456789")
tel.retirer_1000();