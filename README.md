# Tic-Tac-Toe (Pygame)

Un jeu de morpion deux joueurs développé en Python avec Pygame.

# Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Usage](#usage)
- [Contrôles](#contrôles)
- [Structure du projet](#structure-du-projet)

# Fonctionnalités

- Plateau de jeu 3x3 interactif au clic souris.
- Deux joueurs en local (Croix vs Cercle).
- Détection automatique de victoire (lignes, colonnes, diagonales) et de match nul.
- Affichage du joueur dont c'est le tour.
- Affichage du gagnant en fin de partie.
- Redémarrage de la partie sans relancer le programme.

# Installation

## 1. Cloner le dépôt
```bash
git clone https://github.com/Romain-Chevrollier/Tic-Tac-Toe.git
cd Tic-Tac-Toe
```

## 2. Installer les dépendances
```bash
pip install pygame
```

# Usage
```bash
python main.py
```

# Contrôles

| Action | Contrôle |
|---|---|
| Jouer un coup | Clic gauche sur une case |
| Redémarrer | Espace (en fin de partie) |
| Quitter | Fermer la fenêtre |

# Structure du projet
```
Tic-Tac-Toe/
├── main.py
└── assets/
    └── font/
        └── Pixeltype.ttf
```