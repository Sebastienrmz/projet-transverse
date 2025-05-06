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