from transport import Transport
from voiture import Voiture
from avion import Avion
from bateau import Bateau

def demarrer_trajet(transport: Transport):
    transport.se_deplacer()

v = Voiture()
a = Avion()
b = Bateau()

demarrer_trajet(v)
demarrer_trajet(a)
demarrer_trajet(b)