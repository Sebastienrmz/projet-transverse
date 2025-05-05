
import pygame
import sys

# Initialisation de Pygame
pygame.init()

try:
    orbitron_big = pygame.font.Font("Orbitron.ttf", 72)
    orbitron_small = pygame.font.Font("Orbitron.ttf", 30)
except Exception as e:
    print("Erreur de chargement de la police Orbitron :", e)
    pygame.quit()
    sys.exit()



# Charger la musique du menu
pygame.mixer.init()
pygame.mixer.music.load("welcome-to-arena-sport-hip-hop-207257.mp3")  # Mets ton fichier audio ici
pygame.mixer.music.set_volume(0.5)

#Charger l’image de fond et autres images
#Images d’arrière-plann
background_menu = pygame.image.load("cartoon-background-of-street-basketball-vector-22899763.jpg")
background_menu = pygame.transform.scale(background_menu, (800, 600))

background_game = pygame.image.load("background_projet-transversre-Copie.jpg")  # Ton image pour le jeu
background_game = pygame.transform.scale(background_game, (800, 600))



orbitron_big = pygame.font.Font("Orbitron.ttf", 70)
orbitron_medium = pygame.font.Font("Orbitron.ttf", 40)
orbitron_small = pygame.font.Font("Orbitron.ttf", 30)


difficulty="Facile"

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Chargement des images
ball_image = pygame.image.load("0pw3xgm2-modified.jpg").convert_alpha()
basket_image = pygame.image.load("79qqv6dt.jpg").convert_alpha()

# Redimensionner les images si nécessaire
ball_image = pygame.transform.scale(ball_image, (40, 40))
basket_image = pygame.transform.scale(basket_image, (80, 60))

# Couleurs
ecran_largeur = 800
ecran_hauteur = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERT = (0, 255, 0)
GRAY = (100, 100, 100)
LIGHT_GREEN = (144, 238, 144)  # Couleur plus claire pour le survol
ROUGE = (255, 0, 0)
ORANGE = (255, 165, 0)
BLEU = (0, 0, 255)
FONT_SIZE = 50
FPS = 60


# Polices
font_large = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)
font_small = pygame.font.SysFont("Arial", 30)

# Variables
clock = pygame.time.Clock()

BALL_RADIUS = 10
HOOP_X = WIDTH // 2  # Position initiale du panier (au centre)
HOOP_Y = 100         # Position verticale du panier
HOOP_WIDTH = 100      # Largeur du panier
HOOP_HEIGHT = 20      # Hauteur du panier
HOOP_SPEED = 5


# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket Game - Menu")



# Charger une police personnalisée (assurez-toi que le fichier .ttf est dans le dossier 'fonts/')
font_path = "StreetartDemoItalic.ttf"  # Remplace par ton chemin de police .ttf
font = pygame.font.Font(font_path, 50)  # Police personnalisée pour le menu
font_large = pygame.font.Font(font_path, 60)
font_medium = pygame.font.Font(font_path, 40)
font_small = pygame.font.Font(font_path, 28)
font = pygame.font.SysFont(None, 48)
FONT = pygame.font.SysFont("Arial", 30)
# Définition des boutons
buttons = {
    "Jouer": pygame.Rect(50, 280, 200, 50),
    "Options": pygame.Rect(300, 280, 200, 50),
    "Quitter": pygame.Rect(550, 280, 200, 50),
}


def enter_names():
    """Permet aux joueurs d'entrer leur nom."""
    font_small = pygame.font.Font(font_path, 30)
    player1_name = ""
    player2_name = ""
    active_input = 1

    input_box1 = pygame.Rect(150, 200, 500, 50)
    input_box2 = pygame.Rect(150, 300, 500, 50)
    color_inactive = (100, 100, 100)
    color_active = (0, 255, 0)
    color1 = color_active
    color2 = color_inactive

    # Nouveau bouton de démarrage
    start_button = pygame.Rect(300, 400, 200, 50)

    clock = pygame.time.Clock()
    done = False

    while not done:
        screen.fill(WHITE)
        screen.blit(background_menu, (0, 0))

        # Affichage des champs
        text_surface1 = font_small.render(f"Joueur 1 : {player1_name}", True, BLACK)
        text_surface2 = font_small.render(f"Joueur 2 : {player2_name}", True, BLACK)
        screen.blit(text_surface1, (input_box1.x + 10, input_box1.y + 10))
        screen.blit(text_surface2, (input_box2.x + 10, input_box2.y + 10))

        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active_input = 1
                    color1 = color_active
                    color2 = color_inactive
                elif input_box2.collidepoint(event.pos):
                    active_input = 2
                    color1 = color_inactive
                    color2 = color_active
                elif start_button.collidepoint(event.pos) and player1_name and player2_name:
                    return player1_name, player2_name

            elif event.type == pygame.KEYDOWN:
                if active_input == 1:
                    if event.key == pygame.K_BACKSPACE:
                        player1_name = player1_name[:-1]
                    elif len(player1_name) < 20:
                        player1_name += event.unicode
                elif active_input == 2:
                    if event.key == pygame.K_BACKSPACE:
                        player2_name = player2_name[:-1]
                    elif len(player2_name) < 20:
                        player2_name += event.unicode

        # Affichage du bouton démarrer uniquement si les 2 noms sont saisis
        if player1_name and player2_name:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            hovered = start_button.collidepoint(mouse_x, mouse_y)
            draw_button("Démarrer", start_button, hovered, font )

        pygame.display.flip()
        clock.tick(30)

