import pygame

def main():
    # pygame initializer
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets resolution
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Player starting values
    player_speed = 5
    player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.2)

    # Display Start Screen
    draw_start_screen(screen)
    start_screen_displayed = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if start_screen_displayed:
                    start_screen_displayed = False
                else:
                    running = False

        if not start_screen_displayed:
            # Clear the screen
            screen.fill((52, 78, 91))

            # Draw player
            pygame.draw.circle(screen, (255, 0, 0), (int(player_position.x), int(player_position.y)), 40)

            # Left and Right Player Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_position.x -= player_speed
            if keys[pygame.K_d]:
                player_position.x += player_speed

            # Update the display
            pygame.display.update()

            # Limit frame time to 60 fps
            dt = clock.tick(60) / 1000

    # Quits game
    pygame.quit()

def draw_start_screen(screen):
    screen.fill((0, 0, 0)) # Black background
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

if __name__ == '__main__':
    main()
