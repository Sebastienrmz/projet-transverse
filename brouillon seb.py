import pygame
import sys

# Initialisation
pygame.init()
pygame.mixer.init()

# Taille écran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket Game - Menu")
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)
GRAY = (100, 100, 100)
VERT = (0, 255, 0)

# Chargement des polices
try:
    orbitron_big = pygame.font.Font("Orbitron.ttf", 72)
    orbitron_small = pygame.font.Font("Orbitron.ttf", 30)
except Exception as e:
    print("Erreur de chargement de la police Orbitron :", e)
    pygame.quit()
    sys.exit()

font_path = "StreetartDemoItalic.ttf"
font_small = pygame.font.Font(font_path, 28)
font_medium = pygame.font.Font(font_path, 40)
font_large = pygame.font.Font(font_path, 60)
FONT = pygame.font.SysFont("Arial", 30)

# Chargement images
background_menu = pygame.image.load("cartoon-background-of-street-basketball-vector-22899763.jpg")
background_menu = pygame.transform.scale(background_menu, (WIDTH, HEIGHT))

background_game = pygame.image.load("background_projet-transversre-Copie.jpg")
background_game = pygame.transform.scale(background_game, (WIDTH, HEIGHT))

ball_image = pygame.image.load("0pw3xgm2-modified.jpg").convert_alpha()
basket_image = pygame.image.load("79qqv6dt.jpg").convert_alpha()
ball_image = pygame.transform.scale(ball_image, (40, 40))
basket_image = pygame.transform.scale(basket_image, (80, 60))

# Musique
pygame.mixer.music.load("welcome-to-arena-sport-hip-hop-207257.mp3")
pygame.mixer.music.set_volume(0.5)

# Boutons menu
buttons = {
    "Jouer": pygame.Rect(50, 280, 200, 50),
    "Options": pygame.Rect(300, 280, 200, 50),
    "Quitter": pygame.Rect(550, 280, 200, 50),
}


def draw_button(text, rect, hovered, font):
    color = LIGHT_GREEN if hovered else GRAY
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, BLACK)
    screen.blit(text_surf, (rect.x + rect.width // 2 - text_surf.get_width() // 2,
                            rect.y + rect.height // 2 - text_surf.get_height() // 2))


def enter_names():
    player1_name = ""
    player2_name = ""
    active_input = 1

    input_box1 = pygame.Rect(150, 200, 500, 50)
    input_box2 = pygame.Rect(150, 300, 500, 50)
    color1 = VERT
    color2 = GRAY

    start_button = pygame.Rect(300, 400, 200, 50)

    while True:
        screen.blit(background_menu, (0, 0))

        text_surface1 = font_medium.render(f"Joueur 1 : {player1_name}", True, BLACK)
        text_surface2 = font_medium.render(f"Joueur 2 : {player2_name}", True, BLACK)
        screen.blit(text_surface1, (input_box1.x + 10, input_box1.y + 10))
        screen.blit(text_surface2, (input_box2.x + 10, input_box2.y + 10))

        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active_input = 1
                    color1, color2 = VERT, GRAY
                elif input_box2.collidepoint(event.pos):
                    active_input = 2
                    color1, color2 = GRAY, VERT
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

        if player1_name and player2_name:
            hovered = start_button.collidepoint(pygame.mouse.get_pos())
            draw_button("Démarrer", start_button, hovered, font_medium)

        pygame.display.flip()
        clock.tick(30)




def enter_names():
    player1_name = ""
    player2_name = ""
    active_input = 1

    input_box1 = pygame.Rect(150, 200, 500, 50)
    input_box2 = pygame.Rect(150, 300, 500, 50)
    color1 = VERT
    color2 = GRAY

    start_button = pygame.Rect(300, 400, 200, 50)

    while True:
        screen.blit(background_menu, (0, 0))

        #affiche les noms tapés
        text_surface1 = font_medium.render(f"Joueur 1 : {player1_name}", True, BLACK)
        text_surface2 = font_medium.render(f"Joueur 2 : {player2_name}", True, BLACK)
        screen.blit(text_surface1, (input_box1.x + 10, input_box1.y + 10))
        screen.blit(text_surface2, (input_box2.x + 10, input_box2.y + 10))

        #dessine les cadres pour écrire
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #change de champ actif si clic sur un des deux
                if input_box1.collidepoint(event.pos):
                    active_input = 1
                    color1, color2 = VERT, GRAY
                elif input_box2.collidepoint(event.pos):
                    active_input = 2
                    color1, color2 = GRAY, VERT
                #si on clique sur démarrer et que les deux noms sont remplis
                elif start_button.collidepoint(event.pos) and player1_name and player2_name:
                    return player1_name, player2_name

            elif event.type == pygame.KEYDOWN:
                #gestion du texte tapé pour le champ actif
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

        #affiche le bouton "Démarrer" si les deux noms sont remplis
        if player1_name and player2_name:
            hovered = start_button.collidepoint(pygame.mouse.get_pos())
            draw_button("Démarrer", start_button, hovered, font_medium)

        pygame.display.flip()
        clock.tick(30)
