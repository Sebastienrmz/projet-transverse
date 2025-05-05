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