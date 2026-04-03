import math

# 1

def dire_bienvenue() -> str:
    bienvenue = "Bienvenue !"
    print(bienvenue)

    return bienvenue

dire_bienvenue();
dire_bienvenue();

# 2

def salut(prenom: str, age: int) -> str:
    salut = f"Salut {prenom}, tu as {age} an(s)"
    print(salut)

    return salut

salut("Mauritcio", 25)
salut(age=25, prenom="Mauritcio")

# 3

def carre_et_cube(n: float) -> tuple[float, float]:
    carre = n**2
    cube = n**3

    return carre, cube

carre, cube = carre_et_cube(2);

def aire_cercle(r: float) -> float:
    """Fonction pour calculer l'aire d'un cercle

    Args:
        rayon (float): Le rayon du cercle

    Returns:
        float: The return value is a float
    
    """
    return math.pi * r**2

aire_cercle(1.0)