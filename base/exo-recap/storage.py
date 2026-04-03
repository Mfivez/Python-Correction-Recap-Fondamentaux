import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"


def creer_fichier_si_absent():
    """
    Crée le fichier de stockage (data.json) avec des livres par défaut
    s'il n'existe pas.

    :return: None
    """
    if not DATA_FILE.exists():
        livres_par_defaut = [
            {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "disponible": True},
            {"titre": "Harry Potter à l'école des sorciers", "auteur": "J.K. Rowling", "disponible": True}
        ]
        sauvegarder_biblio(livres_par_defaut)


def charger_biblio():
    """
    Charge la bibliothèque depuis le fichier JSON.

    Si le fichier n'existe pas, il est créé automatiquement.
    En cas d'erreur de lecture, une liste vide est retournée.

    :return: Liste des livres.
    :rtype: list
    """
    creer_fichier_si_absent()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except (json.JSONDecodeError, OSError):
        print("Erreur lors de la lecture de data.json.")
        return []


def sauvegarder_biblio(biblio):
    """
    Sauvegarde la bibliothèque dans le fichier JSON.

    :param biblio: Liste des livres à sauvegarder.
    :type biblio: list
    :return: None
    """
    try:
        with DATA_FILE.open("w", encoding="utf-8") as fichier:
            json.dump(biblio, fichier, ensure_ascii=False, indent=4)
    except OSError:
        print("Erreur lors de l'enregistrement de data.json.")