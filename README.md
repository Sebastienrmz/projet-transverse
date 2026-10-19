# Green Ball

Jeu de basket en 2D réalisé en équipe avec Python et Pygame. Deux joueurs jouent à tour de rôle pendant trois manches. Chaque passage dure 30 secondes ; le but est de marquer le plus de paniers.

## Installation

Installer Python 3.10 ou plus récent, puis ouvrir un terminal dans le dossier du jeu :

```sh
python -m venv .venv
```

Activer l'environnement : `.venv\Scripts\activate` sous Windows, ou `source .venv/bin/activate` sous Linux/macOS.

```sh
python -m pip install -r requirements.txt
python main.py
```

Conserver les images, les polices et la musique fournies à côté des scripts. Le jeu nécessite une interface graphique et un périphérique audio disponible pour la musique.

## Commandes

- Cliquer sur **Jouer**, puis saisir les noms des deux joueurs.
- Choisir la difficulté et le volume dans **Options**.
- Maintenir le bouton de la souris, déplacer la souris puis relâcher pour tirer. La direction du tir est opposée au déplacement, comme un lancer au lance-pierre.
- Appuyer sur **P** pour mettre la manche en pause ou la reprendre.
- À la fin, cliquer pour revenir au menu.

## Organisation

`main.py` lance la version intégrée située dans `TEST.py`. Ce nom historique est conservé pour éviter de déplacer tout le code. Ce fichier contient le menu, les options, les animations, les manches et l'écran de fin.

`Menu.py`, `hasan.py`, `animationHasan.py`, `code_jeu.py` et `brouillon seb.py` sont des essais ou des parties de travail conservés dans le dépôt. Ils ne sont pas les points d'entrée du jeu et certains ne fonctionnent pas seuls.

## Répartition du travail

- Sébastien Ramirez : menu.
- Scott Ngoumela : animations du menu.
- Hasan Ayintapli : animations du jeu.
- Aliyane Benchehida : fin du jeu et assemblage principal.
- Raphaël Derobien : jeu.

Cette répartition reprend la présentation initiale de l'équipe.

## À connaître

Les trajectoires utilisent une vitesse et une gravité mises à jour à chaque image. Le score repose sur une collision avec la zone du panier. Le mode difficile déplace le panier et change la position de départ de la balle.

Le projet reste un jeu de cours : les collisions sont simples, certaines animations attendent avec `pygame.time.delay`, et les scores ne sont pas enregistrés entre deux parties. Les corrections de démarrage conservent le déroulement et les visuels d'origine : chemin des ressources, police présente dans le dépôt, difficulté cohérente et chronomètre pendant la pause.
