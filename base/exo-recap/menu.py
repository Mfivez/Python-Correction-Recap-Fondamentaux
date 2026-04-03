from storage import charger_biblio
from library import (
    afficher_bibliotheque,
    rechercher_livre,
    emprunter_livre,
    retourner_livre,
    compter_livres,
    suggestion_lecture,
)

def afficher_menu():
    """
    Affiche le menu principal de l'application.

    :return: None
    """
    print("\n===== MENU BIBLIOTHÈQUE =====")
    print("1. Afficher les livres")
    print("2. Rechercher un livre")
    print("3. Emprunter un livre")
    print("4. Retourner un livre")
    print("5. Compter les livres")
    print("6. Suggestion de lecture")
    print("7. Quitter")


def lancer_menu():
    """
    Lance l'interface en ligne de commande permettant à l'utilisateur
    d'interagir avec la bibliothèque.

    L'utilisateur peut :
    - afficher les livres
    - rechercher un livre
    - emprunter un livre
    - retourner un livre
    - compter les livres
    - obtenir une suggestion de lecture

    :return: None
    """
    biblio = charger_biblio()

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ").strip()

        if choix == "1":
            afficher_bibliotheque(biblio)

        elif choix == "2":
            titre = input("Entrez le titre du livre à rechercher : ").strip()
            livre = rechercher_livre(biblio, titre)

            if livre is None:
                print("Erreur : livre introuvable.")
            else:
                etat = "disponible" if livre["disponible"] else "emprunté"
                print(f"Livre trouvé : {livre['titre']} - {livre['auteur']} [{etat}]")

        elif choix == "3":
            titre = input("Entrez le titre du livre à emprunter : ").strip()
            emprunter_livre(biblio, titre)

        elif choix == "4":
            titre = input("Entrez le titre du livre à retourner : ").strip()
            retourner_livre(biblio, titre)

        elif choix == "5":
            total, disponibles = compter_livres(biblio)
            print(f"Nombre total de livres : {total}")
            print(f"Nombre de livres disponibles : {disponibles}")

        elif choix == "6":
            suggestion_lecture(biblio)

        elif choix == "7":
            print("Arrêt du programme.")
            break

        else:
            print("Erreur : veuillez entrer un nombre entre 1 et 7.")