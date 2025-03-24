import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Charger la musique du menu
pygame.mixer.init()
pygame.mixer.music.load("welcome-to-arena-sport-hip-hop-207257.mp3")  # Remplace par ton fichier audio téléchargé
pygame.mixer.music.set_volume(0.5)  # Ajuste le volume (0.0 à 1.0)
pygame.mixer.music.play(-1)  # -1 permet de jouer en boucle

# Charger l’image de fond
background = pygame.image.load("cartoon-background-of-street-basketball-vector-22899763.jpg")  # Mets le bon nom de ton image
background = pygame.transform.scale(background, (800, 600))  # Adapter à la fenêtre

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERT = (0, 255, 0)
GRAY = (100, 100, 100)

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket Game - Menu")

# Police et texte
font = pygame.font.Font(None, 50)

# Définition des boutons
buttons = {
    "Jouer": pygame.Rect(50, 280, 200, 50),
    "Options": pygame.Rect(300, 280, 200, 50),
    "Quitter": pygame.Rect(550, 280, 200, 50),
}


def draw_menu():
    screen.blit(background, (0, 0))  # Afficher l’image de fond

    # Titre du jeu
    title = font.render("Green ball", True, VERT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    # Dessin des boutons
    for text, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        label = font.render(text, True, BLACK)
        screen.blit(label, (rect.x + 50, rect.y + 10))

    pygame.display.flip()


def main():
    running = True
    while running:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if buttons["Jouer"].collidepoint(x, y):
                    print("Lancer le jeu !")
                elif buttons["Options"].collidepoint(x, y):
                    print("Afficher les options")
                elif buttons["Quitter"].collidepoint(x, y):
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()











