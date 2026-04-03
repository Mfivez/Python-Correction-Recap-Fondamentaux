# Gestion d'une petite bibliothèque

## But du projet

Ce programme permet de gérer une petite bibliothèque en mode console.

L'utilisateur peut :
- afficher les livres
- rechercher un livre
- emprunter un livre
- retourner un livre
- compter les livres
- obtenir une suggestion de lecture aléatoire

Le programme continue à tourner jusqu'à ce que l'utilisateur choisisse de quitter.

---

## A quoi sert le fichier main.py
```python
from menu import lancer_menu

if __name__ == "__main__":
    lancer_menu()
```

---

Ce fichier est le **point d’entrée du programme**.

C’est lui qui dit à Python :

> “Lance l’application et affiche le menu.”

On l’appelle souvent : `main.py`

---

## 1. `from menu import lancer_menu`
Cette ligne signifie :
>“Va dans le fichier `menu.py` et récupère la fonction `lancer_menu`”

## 2. `if __name__ == "__main__":`
Cette ligne peut sembler étrange, mais elle est **essentielle en Python** lorsqu'on commence à séparer notre code en fichiers.

Il faut comprendre que chaque fichier Python possède une variable spéciale appelée :

```python
__name__
```

Python lui donne une valeur automatiquement.

---

### Deux cas possibles

#### Cas 1 : tu exécutes le fichier directement

```bash
python main.py
```

Alors :

```python
__name__ == "__main__"
```

Donc le code à l’intérieur du `if` va s’exécuter

---

#### Cas 2 : le fichier est importé ailleurs

```python
import main
```

Alors :

```python
__name__ == "main"
```

Donc le code **ne s’exécute pas**

---

## Objectif ?

Cela permet de :

### Séparer deux choses :

>1. Le code qui peut être **réutilisé**

>2. Le code qui doit s’exécuter **uniquement au lancement**

## 3. `lancer_menu()`

Cette ligne appelle la fonction principale :

Elle démarre ton programme (menu interactif)

---