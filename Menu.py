import pygame
import sys

pygame.init()

# Taille de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu Principal")

# Chargement de l'image de fond avec boutons intégrés
background = pygame.image.load("A_clean_and_stylish_UI_interface_design_for_a_bask.png")
background = pygame.transform.scale(background, (800, 600))  # Adapter à la taille de l'écran

# Exemple de coordonnées pour les ballons (à ajuster selon ton image !)
# Format : pygame.Rect(x, y, largeur, hauteur)
zone_jouer = pygame.Rect(280, 200, 220, 80)
zone_options = pygame.Rect(280, 310, 220, 80)
zone_quitter = pygame.Rect(280, 420, 220, 80)

def menu():
    clock = pygame.time.Clock()

    while True:
        screen.blit(background, (0, 0))  # Afficher le fond avec les boutons intégrés

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if zone_jouer.collidepoint(event.pos):
                    print("→ Lancement du jeu !")
                elif zone_options.collidepoint(event.pos):
                    print("→ Menu des options ")
                elif zone_quitter.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

menu()

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("A_clean_and_stylish_UI_interface_design_for_a_bask.png")
background = pygame.transform.scale(background, (800, 600))

pygame.display.set_caption("Test de coordonnées")

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Tu as cliqué en position : {event.pos}")

    pygame.display.flip()