import pygame
import sys
import time
import random
import math
# Initialisation de Pygame
pygame.init()




# Charger la musique du menu
pygame.mixer.init()
pygame.mixer.music.load("welcome-to-arena-sport-hip-hop-207257.mp3")  # Mets ton fichier audio ici
pygame.mixer.music.set_volume(0.5)

# Charger l’image de fond et autres images
# Images d’arrière-plan
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
ecran_hauteur = 800
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



def draw_button(text, rect, is_hovered, font):
    """Dessiner un bouton avec survol et texte."""
    button_color = LIGHT_GREEN if is_hovered else VERT
    border_color = WHITE

    pygame.draw.rect(screen, button_color, rect, border_radius=15)
    pygame.draw.rect(screen, border_color, rect, 5, border_radius=15)

    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)



def draw_ball(x, y):
    pygame.draw.circle(WIN, ORANGE, (int(x), int(y)), BALL_RADIUS)
    pygame.draw.circle(WIN, BLACK, (int(x), int(y)), BALL_RADIUS, 2)

def draw_hoop():
    pygame.draw.rect(screen, (255, 0, 0), (HOOP_X, HOOP_Y, HOOP_WIDTH, HOOP_HEIGHT))



def adjust_hoop_size():
    global HOOP_WIDTH, HOOP_X

    if difficulty == "Facile":
        HOOP_WIDTH = 100  # Largeur normale
    elif difficulty == "Moyen":
        HOOP_WIDTH = 80 # Panier plus petit
    elif difficulty == "Difficile":
        HOOP_WIDTH = 100  # Normal, mais on fera déplacer le panier


def move_hoop():
    global HOOP_X, HOOP_SPEED

    if difficulty == "Difficile":
        # Déplacer le panier de gauche à droite
        HOOP_X += HOOP_SPEED
        if HOOP_X < 0 or HOOP_X + HOOP_WIDTH > WIDTH:
            HOOP_SPEED = -HOOP_SPEED  # Inverser la direction si le panier touche les bords

background_options = pygame.image.load("background_option_menu_projet_transverse.png").convert()
background_options = pygame.transform.scale(background_options, (WIDTH, HEIGHT))

def options_menu():
    global difficulty
    running = True

    back_button = pygame.Rect(600, 500, 150, 50)
    volume_slider = pygame.Rect(500, 145, 150, 50)
    dragging = False

    while running:
        screen.blit(background_options, (0, 0))

        # Titre "Options"
        title = orbitron_big.render("Options", True, VERT)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        # Volume
        music_text = orbitron_small.render("Volume Musique :", True, WHITE)
        screen.blit(music_text, (100, 150))

        pygame.draw.rect(screen, WHITE, volume_slider)
        volume = pygame.mixer.music.get_volume()
        pygame.draw.rect(screen, VERT, (volume_slider.x, volume_slider.y, int(volume * volume_slider.width), volume_slider.height))
        handle_x = volume_slider.x + int(volume * volume_slider.width)
        pygame.draw.circle(screen, BLACK, (handle_x, volume_slider.y + volume_slider.height // 2), 10)

        # Difficulté
        draw_text("Difficulté :", orbitron_medium, WHITE, screen, 100, 200)

        easy_button = pygame.Rect(115, 265, 110, 50)
        medium_button = pygame.Rect(225, 265, 110, 50)
        hard_button = pygame.Rect(335, 265, 155, 50)

        pygame.draw.rect(screen, (0, 200, 0), easy_button)
        pygame.draw.rect(screen, (255, 165, 0), medium_button)
        pygame.draw.rect(screen, (200, 0, 0), hard_button)

        draw_text("Facile", orbitron_small, BLACK, screen, 115, 265)
        draw_text("Moyen", orbitron_small, BLACK, screen, 225, 265)
        draw_text("Difficile", orbitron_small, BLACK, screen, 335, 265)

        draw_text(f"Difficulté actuelle : {difficulty}", orbitron_small, WHITE, screen, 100, 320)

        draw_button("Retour", back_button, back_button.collidepoint(*pygame.mouse.get_pos()), orbitron_small)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False
                elif volume_slider.collidepoint(event.pos):
                    dragging = True
                elif easy_button.collidepoint(event.pos):
                    difficulty = "Facile"
                elif medium_button.collidepoint(event.pos):
                    difficulty = "Moyen"
                elif hard_button.collidepoint(event.pos):
                    difficulty = "Difficile"

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            elif event.type == pygame.MOUSEMOTION and dragging:
                rel_x = event.pos[0] - volume_slider.x
                rel_x = max(0, min(rel_x, volume_slider.width))
                new_volume = rel_x / volume_slider.width
                pygame.mixer.music.set_volume(new_volume)

        pygame.display.flip()
        pygame.time.delay(30)





def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def start_game(player1_name, player2_name):
    level = 1  # Tu peux ajouter un menu de difficulté plus tard
    score1_total = 0
    score2_total = 0

    for round_number in range(1, 4):  # 3 manches
        print(f"Manche {round_number} : {player1_name} joue")
        score1, _ = play_round(level, player1_name, player2_name, round_number)

        print(f"Manche {round_number} : {player2_name} joue")
        score2, _ = play_round(level, player2_name, player1_name, round_number)

        score1_total += score1
        score2_total += score2

        print(f"Résultat de la manche {round_number} :")
        print(f"{player1_name} : {score1} points | {player2_name} : {score2} points")

    # Résultat final
    if score1_total > score2_total:
        winner = player1_name
    elif score2_total > score1_total:
        winner = player2_name
    else:
        winner = "Égalité"

    print("Fin du jeu !")
    print(f"{player1_name} : {score1_total} points")
    print(f"{player2_name} : {score2_total} points")
    print(f"Gagnant : {winner}")


def draw_centered_text(text, font, color, y):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH // 2, y))
    screen.blit(rendered, rect)



def show_round(round_number, player_name):
    # Charger la police Orbitron
    orbitron_big = pygame.font.Font("Orbitron.ttf", 72)
    orbitron_countdown = pygame.font.Font("Orbitron.ttf", 100)

    background = pygame.image.load("image_manche.jpg")  # Remplace par ton image
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Afficher la manche avec fondu
    message = f"Manche {round_number} - {player_name}"
    text = orbitron_big.render(message, True, (255, 215, 0))  # Doré
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))

    for alpha in range(0, 256, 10):
        screen.blit(background, (0, 0))
        text.set_alpha(alpha)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(30)

    # Compte à rebours : 3, 2, 1, GO!
    for count in ["3", "2", "1", "GO!"]:
        countdown_text = orbitron_countdown.render(count, True, (255, 215, 0))
        countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        for alpha in range(0, 256, 20):
            screen.blit(background, (0, 0))
            screen.blit(text, text_rect)  # Re-affiche le titre de manche
            countdown_text.set_alpha(alpha)
            screen.blit(countdown_text, countdown_rect)
            pygame.display.flip()
            pygame.time.delay(20)

        pygame.time.delay(300)  # Pause entre les nombres

    pygame.time.delay(300)  # Pause après GO!





def show_end_screen(player1, player2, score1, score2):
    # Charger l'image de fond
    background_img = pygame.image.load("image_victoire.jpg").convert()
    background_img = pygame.transform.scale(background_img, (ecran_hauteur, ecran_largeur))

    # Afficher l'image de fond
    screen.blit(background_img, (0, 0))

    # Afficher les textes par-dessus l'image
    draw_centered_text("Fin du Jeu", orbitron_big, WHITE, 80)
    draw_centered_text(f"{player1}: {score1} pts", orbitron_medium, VERT, 200)
    draw_centered_text(f"{player2}: {score2} pts", orbitron_medium, VERT, 260)

    if score1 > score2:
        winner = f"Gagnant: {player1}"
    elif score2 > score1:
        winner = f"Gagnant: {player2}"
    else:
        winner = "Match nul !"

    draw_centered_text(winner, orbitron_medium, ROUGE, 350)
    draw_centered_text("Cliquez pour retourner au menu", orbitron_small, WHITE, 500)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False




def get_difficulty_margin():
    if difficulty == "easy":
        return 40
    elif difficulty == "medium":
        return 25
    elif difficulty == "hard":
        return 10

difficulty= "facile" #par défaut
orbitron_font_small = pygame.font.Font("Orbitron.ttf", 30)
orbitron_font_large = pygame.font.Font("Orbitron.ttf", 72)



def play_round(player_name, round_number, difficulty):
    # Animation de la manche avec texte grandissant
    show_round(round_number, player_name)

    # Pause avant le début de la manche
    time.sleep(1)

    # Paramètres physiques
    gravity = 0.4
    launched = False
    velocity = [0, 0]
    aiming = False
    aim_start = (0, 0)

    # Initialisation de la balle
    if difficulty == "Difficile":
        ball = pygame.Rect(random.randint(300, 450), 500, 50, 50)
    else:
        ball = pygame.Rect(370, 500, 50, 50)

    # Initialisation du panier
    if difficulty == "Facile":
        hoop_zone = pygame.Rect(350, 100, 100, 20)
    elif difficulty == "Moyen":
        hoop_zone = pygame.Rect(370, 100, 60, 20)
    elif difficulty == "Difficile":
        hoop_zone = pygame.Rect(350, 100, 100, 20)
        direction = 1
        speed = 3
    else:
        hoop_zone = pygame.Rect(350, 100, 100, 20)

    paused = False
    pause_start = 0
    total_pause_duration = 0
    start_time = time.time()
    score = 0  # Initialisation du score

    # Boucle de la manche
    while time.time() - start_time - total_pause_duration < 30:
        screen.blit(background_game, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        pause_start = time.time()
                    else:
                        total_pause_duration += time.time() - pause_start
            if not paused:
                if event.type == pygame.MOUSEBUTTONDOWN and not launched:
                    aiming = True
                    aim_start = event.pos
                elif event.type == pygame.MOUSEBUTTONUP and aiming:
                    aim_end = event.pos
                    dx = (aim_start[0] - aim_end[0]) / 10
                    dy = (aim_start[1] - aim_end[1]) / 10
                    velocity = [dx, dy]
                    launched = True
                    aiming = False

        if not paused:
            if launched:
                ball.x += int(velocity[0])
                ball.y += int(velocity[1])
                velocity[1] += gravity

                if hoop_zone.colliderect(ball):
                    score += 1
                    launched = False
                    ball.topleft = (random.randint(300, 450), 500) if difficulty == "Difficile" else (370, 500)
                    velocity = [0, 0]
                elif ball.top > HEIGHT or ball.right < 0 or ball.left > WIDTH:
                    launched = False
                    ball.topleft = (random.randint(300, 450), 500) if difficulty == "Difficile" else (370, 500)
                    velocity = [0, 0]

            if difficulty == "Difficile":
                hoop_zone.x += direction * speed
                if hoop_zone.left <= 0 or hoop_zone.right >= WIDTH:
                    direction *= -1

            # Affichage des éléments de jeu
            screen.blit(basket_image, (hoop_zone.x, hoop_zone.y))
            screen.blit(ball_image, (ball.x, ball.y))

            elapsed = time.time() - start_time - total_pause_duration
            remaining = max(0, int(30 - elapsed))

            # Affichage du score et timer avec Orbitron
            timer_text = orbitron_font_small.render(f"Temps: {remaining}s", True, WHITE)
            score_text = orbitron_font_small.render(f"{player_name} Score: {score}", True, VERT)
            screen.blit(timer_text, (10, 10))
            screen.blit(score_text, (10, 50))

        else:
            pause_text = orbitron_font_large.render("PAUSE", True, WHITE)
            screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(60)

    return score


def start_game(player1, player2, difficulty):
    total1 = 0
    total2 = 0

    for i in range(1, 4):
        total1 += play_round(player1, i, difficulty)
        total2 += play_round(player2, i, difficulty)

    show_end_screen(player1, player2, total1, total2)



def show_score_graph(scores1, scores2, player1_name, player2_name):
    bar_width = 100
    spacing = 60
    max_score = max(max(scores1), max(scores2), 1)  # éviter division par 0
    screen.fill((0, 0, 0))

    # Titre
    title = orbitron_big.render("Résumé des scores", True, VERT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    for i in range(3):
        # Barre joueur 1
        h1 = int((scores1[i] / max_score) * 200)
        bar1 = pygame.Rect(150 + i * (bar_width + spacing), 400 - h1, bar_width, h1)
        pygame.draw.rect(screen, VERT, bar1)

        # Barre joueur 2
        h2 = int((scores2[i] / max_score) * 200)
        bar2 = pygame.Rect(150 + i * (bar_width + spacing) + bar_width // 2, 400 - h2, bar_width, h2)
        pygame.draw.rect(screen, (255, 100, 100), bar2)

        # N° de manche
        label = orbitron_small.render(f"Manche {i + 1}", True, WHITE)
        screen.blit(label, (bar1.x + 10, 420))

    # Légendes
    legend1 = orbitron_small.render(player1_name, True, VERT)
    legend2 = orbitron_small.render(player2_name, True, (255, 100, 100))
    screen.blit(legend1, (WIDTH // 2 - 150, 500))
    screen.blit(legend2, (WIDTH // 2 + 50, 500))

    pygame.display.flip()
    pygame.time.delay(5000)




# Déclaration globale de la difficulté
difficulty = "Facile"



def draw_menu():
    screen.blit(background_menu, (0, 0))  # Affiche l’image de fond

    # Titre du jeu avec Orbitron
    title = orbitron_big.render("Green Ball", True, VERT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    # Dessin des boutons
    for text, rect in buttons.items():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hovered = rect.collidepoint(mouse_x, mouse_y)
        draw_button(text, rect, is_hovered, orbitron_medium)

    pygame.display.flip()


def main():
    global difficulty
    difficulty = "facile"  # difficulté par défaut

    animation_titre_progressif()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if buttons["Jouer"].collidepoint(x, y):
                    player1_name, player2_name = enter_names()
                    print(f"Joueur 1 : {player1_name}")
                    print(f"Joueur 2 : {player2_name}")
                    start_game(player1_name, player2_name, difficulty)

                elif buttons["Options"].collidepoint(x, y):
                    options_menu()

                elif buttons["Quitter"].collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        draw_menu()
        pygame.time.delay(30)







if __name__ == "__main__":
    main()








