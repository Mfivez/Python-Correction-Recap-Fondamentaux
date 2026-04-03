
import random
from storage import sauvegarder_biblio


def afficher_bibliotheque(biblio):
    """
    Affiche la liste des livres présents dans la bibliothèque.

    :param biblio: Liste de dictionnaires représentant les livres.
                   Chaque livre contient les clés 'titre', 'auteur' et 'disponible'.
    :type biblio: list
    :return: None
    """

    if not biblio:
        print("\nLa bibliothèque est vide.")
        return

    print("\n--- Liste des livres ---")
    for index, livre in enumerate(biblio, start=1):
        etat = "disponible" if livre["disponible"] else "emprunté"
        print(f"{index}. {livre['titre']} - {livre['auteur']} [{etat}]")


def rechercher_livre(biblio, titre):
    """
    Recherche un livre dans la bibliothèque par son titre.

    La recherche est insensible à la casse et aux espaces en début/fin.

    :param biblio: Liste des livres.
    :type biblio: list
    :param titre: Titre du livre à rechercher.
    :type titre: str
    :return: Le dictionnaire du livre trouvé ou None si absent.
    :rtype: dict | None
    """
    for livre in biblio:
        if livre["titre"].strip().lower() == titre.strip().lower():
            return livre
        
    return None


def emprunter_livre(biblio, titre):
    """
    Permet d'emprunter un livre s'il est disponible.

    Met à jour l'état du livre et sauvegarde la bibliothèque.

    :param biblio: Liste des livres.
    :type biblio: list
    :param titre: Titre du livre à emprunter.
    :type titre: str
    :return: None
    """
    livre = rechercher_livre(biblio, titre)

    if livre is None:
        print("Erreur : livre introuvable.")
        return

    if not livre["disponible"]:
        print("Ce livre est déjà emprunté.")
        return

    livre["disponible"] = False
    sauvegarder_biblio(biblio)

    print(f"Le livre '{livre['titre']}' a bien été emprunté.")


def retourner_livre(biblio, titre):
    """
    Permet de retourner un livre emprunté.

    Met à jour l'état du livre et sauvegarde la bibliothèque.

    :param biblio: Liste des livres.
    :type biblio: list
    :param titre: Titre du livre à retourner.
    :type titre: str
    :return: None
    """
    livre = rechercher_livre(biblio, titre)

    if livre is None:
        print("Erreur : livre introuvable.")
        return

    if livre["disponible"]:
        print("Ce livre est déjà disponible.")
        return

    livre["disponible"] = True
    sauvegarder_biblio(biblio)
    
    print(f"Le livre '{livre['titre']}' a bien été retourné.")


def compter_livres(biblio):
    """
    Compte le nombre total de livres et le nombre de livres disponibles.

    :param biblio: Liste des livres.
    :type biblio: list
    :return: Tuple contenant (nombre total, nombre disponibles).
    :rtype: tuple(int, int)
    """
    total = len(biblio)
    disponibles = 0

    for livre in biblio:
        if livre["disponible"]:
            disponibles += 1

    return total, disponibles


def suggestion_lecture(biblio):
    """
    Propose un livre aléatoire parmi ceux disponibles.

    :param biblio: Liste des livres.
    :type biblio: list
    :return: None
    """
    livres_disponibles = []

    for livre in biblio:
        if livre["disponible"]:
            livres_disponibles.append(livre)

    if not livres_disponibles:
        print("Aucun livre disponible pour une suggestion.")
        return

    choix = random.choice(livres_disponibles)
    print(f"Suggestion de lecture : {choix['titre']} - {choix['auteur']}")