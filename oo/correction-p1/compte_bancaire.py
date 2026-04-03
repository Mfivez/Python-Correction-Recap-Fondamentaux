class CompteBancaire:
    def __init__(self, titulaire_user_input: str, interet_user_input: float, montant_user_input: float):
        self.titulaire = titulaire_user_input
        self.interet = interet_user_input
        self.montant = montant_user_input

    def vider(self):
        if self.montant == 0:
            print('Pleurer')
        else:
            self.montant = 0
            print('Pleurer')