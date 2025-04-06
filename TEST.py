import pygame
import sys
import time
import random

# Initialisation de Pygame
pygame.init()

# Charger la musique du menu
pygame.mixer.init()
pygame.mixer.music.load("welcome-to-arena-sport-hip-hop-207257.mp3")  # Mets ton fichier audio ici
pygame.mixer.music.set_volume(0.5)

# Charger l’image de fond et autres images
background = pygame.image.load("cartoon-background-of-street-basketball-vector-22899763.jpg")
background = pygame.transform.scale(background, (800, 600))

basket_img = pygame.image.load("basket.png")  # Image du panier
basket_img = pygame.transform.scale(basket_img, (200, 200))

ball_img = pygame.image.load("ball.png")  # Image du ballon
ball_img = pygame.transform.scale(ball_img, (50, 50))

explosion_img = pygame.image.load("explosion.png")  # Image d'explosion
explosion_img = pygame.transform.scale(explosion_img, (250, 250))

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERT = (0, 255, 0)
GRAY = (100, 100, 100)
LIGHT_GREEN = (144, 238, 144)  # Couleur plus claire pour le survol

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket Game - Menu")

# Charger une police personnalisée (assurez-toi que le fichier .ttf est dans le dossier 'fonts/')
font_path = "StreetartDemoItalic.ttf"  # Remplace par ton chemin de police .ttf
font = pygame.font.Font(font_path, 50)  # Police personnalisée pour le menu

# Définition des boutons
buttons = {
    "Jouer": pygame.Rect(50, 280, 200, 50),
    "Options": pygame.Rect(300, 280, 200, 50),
    "Quitter": pygame.Rect(550, 280, 200, 50),
}


def enter_names():
    """Permet aux joueurs d'entrer leur nom."""
    font_small = pygame.font.Font(font_path, 30)  # Police plus petite pour l'entrée du nom

    # Créer un champ de texte pour les joueurs
    player1_name = ""
    player2_name = ""
    active_input = 1  # Variable pour savoir quel joueur entre son nom (1 pour joueur 1, 2 pour joueur 2)

    input_box1 = pygame.Rect(150, 200, 500, 50)
    input_box2 = pygame.Rect(150, 300, 500, 50)
    color_inactive = (100, 100, 100)
    color_active = (0, 255, 0)
    color1 = color_inactive
    color2 = color_inactive
    active = False  # Pour savoir si le champ de texte est actif

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        # Affichage des champs de texte
        text_surface1 = font_small.render(f"Joueur 1 : {player1_name}", True, BLACK)
        text_surface2 = font_small.render(f"Joueur 2 : {player2_name}", True, BLACK)
        screen.blit(text_surface1, (input_box1.x + 10, input_box1.y + 10))
        screen.blit(text_surface2, (input_box2.x + 10, input_box2.y + 10))

        # Affichage des boîtes de saisie
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active_input = 1
                    color1 = color_active
                    color2 = color_inactive
                elif input_box2.collidepoint(event.pos):
                    active_input = 2
                    color1 = color_inactive
                    color2 = color_active
                else:
                    color1 = color_inactive
                    color2 = color_inactive

            if event.type == pygame.KEYDOWN:
                if active_input == 1:
                    if event.key == pygame.K_BACKSPACE:
                        player1_name = player1_name[:-1]
                    else:
                        player1_name += event.unicode
                elif active_input == 2:
                    if event.key == pygame.K_BACKSPACE:
                        player2_name = player2_name[:-1]
                    else:
                        player2_name += event.unicode

        # Vérifier si les deux joueurs ont saisi leur nom
        if len(player1_name) > 0 and len(player2_name) > 0:
            # Afficher un bouton "Démarrer" une fois les noms saisis
            pygame.draw.rect(screen, GRAY, buttons["Jouer"])
            label = font.render("Démarrer", True, BLACK)
            screen.blit(label, (buttons["Jouer"].x + 50, buttons["Jouer"].y + 10))

        pygame.display.flip()
        clock.tick(30)

        # Attendre la validation du bouton "Démarrer"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if buttons["Jouer"].collidepoint(x, y) and len(player1_name) > 0 and len(player2_name) > 0:
                    return player1_name, player2_name



def animation_titre_progressif():
    """Affiche le titre lettre par lettre avec effet zoom et couleur sur écran noir"""
    title_text = "Green Ball"
    displayed = ""
    clock = pygame.time.Clock()

    # Afficher l'écran noir
    screen.fill(BLACK)
    pygame.display.flip()

    # Animation du titre lettre par lettre
    for i, char in enumerate(title_text):
        displayed += char
        color = VERT if i % 2 == 0 else WHITE  # Alterne les couleurs
        zoom_factor = 1 + (i * 0.1)  # Zoom progressif (commence petit et grandit)

        # Crée l'effet de zoom pour chaque lettre
        title_surface = font.render(displayed, True, color)
        scaled_surface = pygame.transform.scale(title_surface, (
            int(title_surface.get_width() * zoom_factor), int(title_surface.get_height() * zoom_factor)))

        # Calculer la position pour centrer le titre
        x_pos = WIDTH // 2 - scaled_surface.get_width() // 2
        y_pos = HEIGHT // 2 - scaled_surface.get_height() // 2

        screen.fill(BLACK)  # L'écran noir
        screen.blit(scaled_surface, (x_pos, y_pos))  # Afficher le titre avec le zoom
        pygame.display.flip()

        pygame.time.delay(200)  # Délai entre l'apparition des lettres
        clock.tick(60)

    # Petite pause finale avant d'entrer dans le menu
    pygame.time.delay(1000)

    # Transition : écran noir se divise en carrés
    transition()

    pygame.mixer.music.play(-1)


def transition():
    """Transition où l'écran noir se divise en petits carrés"""
    square_size = 50
    num_squares_x = WIDTH // square_size
    num_squares_y = HEIGHT // square_size
    squares = []

    # Créer une liste de carrés
    for x in range(num_squares_x):
        for y in range(num_squares_y):
            square_rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            squares.append(square_rect)

    random.shuffle(squares)  # Mélanger l'ordre pour un effet plus fluide

    # Transition des carrés
    for square in squares:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, square)  # Dessiner chaque carré en blanc
        pygame.display.flip()
        pygame.time.delay(10)  # Lente transition
        pygame.time.delay(10)  # Remplacé pygame.time.wait par pygame.time.delay


def draw_button(text, rect, is_hovered):
    """Dessiner un bouton avec survol et texte."""
    button_color = LIGHT_GREEN if is_hovered else VERT
    border_color = WHITE

    pygame.draw.rect(screen, button_color, rect, border_radius=15)
    pygame.draw.rect(screen, border_color, rect, 5, border_radius=15)

    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


def draw_menu():
    """Affichage du menu principal avec des boutons personnalisés"""
    screen.blit(background, (0, 0))  # Afficher l’image de fond

    # Titre du jeu
    title = font.render("Green Ball", True, VERT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    # Dessin des boutons
    for text, rect in buttons.items():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hovered = rect.collidepoint(mouse_x, mouse_y)
        draw_button(text, rect, is_hovered)

    pygame.display.flip()


def main():
    """Lancement du jeu avec animation puis menu"""
    animation_titre_progressif()  # Nouvelle animation à la place de l’ancienne
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if buttons["Jouer"].collidepoint(x, y):
                    player1_name, player2_name = enter_names()  # Attendre que les joueurs saisissent leurs noms
                    print(f"Joueur 1 : {player1_name}")
                    print(f"Joueur 2 : {player2_name}")

                    # Lancer une fonction de jeu après la saisie des noms (par exemple, démarrer un niveau)
                    start_game(player1_name, player2_name)
                elif buttons["Options"].collidepoint(x, y):
                    print("Afficher les options")
                elif buttons["Quitter"].collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        draw_menu()  # Dessine le menu
        pygame.time.delay(30)



def start_game(player1_name, player2_name):
    """Démarre le jeu avec les noms des joueurs"""
    print(f"Le jeu commence avec {player1_name} et {player2_name}")

if __name__ == "__main__":
    main()