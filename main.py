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
