entier = int(input('Entrez un entier'))
reel = float(input('Entrez un reel'))
mot = "Banane"

print (f"""
somme = {entier + reel}
produit = {entier * reel}

La chaîne est : { mot }
1er caractère : { mot[0] }
last caractère : { mot[-1] }
une partie de la chaîne : { mot[1:4]}
longueur de la châine : { len(mot) }

Correction 5.
{ bool(None) }
{ bool(12) }
{ bool("") }
{ bool("aze") }
""")

a = 2;

match a:
    case a :
        print('a')