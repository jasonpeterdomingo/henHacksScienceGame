import pygame
import sys


def main():
    # pygame initializer
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Sets resolution
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Player starting values
    player_speed = 5
    player_radius = 40
    player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.2)

    # Interactive object
    object_rect = pygame.Rect(400, player_position.y - player_radius, 100, 100)

    # Display Start Screen
    draw_start_screen(screen)

    start_screen_displayed = True
    battle_screen_displayed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and start_screen_displayed:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    if 540 <= x <= 740 and 320 <= y <= 380:  # Start button area
                        start_screen_displayed = False
                    elif 540 <= x <= 740 and 420 <= y <= 480:  # Exit button area
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and battle_screen_displayed:
                if event.button == 1:  # Left mouse button
                    battle_screen_displayed = False

        if not start_screen_displayed and not battle_screen_displayed:
            # Clear the screen
            screen.fill((52, 78, 91))

            # Draw interactive object
            pygame.draw.rect(screen, (0, 255, 0), object_rect)  # Interactive object

            # Draw player
            pygame.draw.circle(screen, (255, 0, 0), (int(player_position.x), int(player_position.y)), player_radius)

            # Left and Right Player Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_position.x -= player_speed
            if keys[pygame.K_d]:
                player_position.x += player_speed

            # Update the interactive object's position
            object_rect.y = player_position.y - player_radius

            # Check for collision with interactive object
            if object_rect.colliderect(
                    pygame.Rect(player_position.x - player_radius, player_position.y - player_radius, player_radius * 2,
                                player_radius * 2)):
                battle_screen_displayed = True
                draw_battle_screen(screen)

            # Update the display
            pygame.display.update()

            # Limit frame time to 60 fps
            dt = clock.tick(60) / 1000

        elif battle_screen_displayed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    battle_screen_displayed = False

            draw_battle_screen(screen)
            pygame.display.update()

    # Quits game
    pygame.quit()


def draw_start_screen(screen):
    screen.fill((0, 0, 0))  # Black background
    font = pygame.font.Font(None, 36)
    text = font.render("Click to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 100))
    screen.blit(text, text_rect)

    # Start Button
    pygame.draw.rect(screen, (255, 255, 255), (540, 320, 200, 60), 2)  # Draw clickable area
    text_start = font.render("Start", True, (255, 255, 255))
    text_start_rect = text_start.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text_start, text_start_rect)

    # Exit Button
    pygame.draw.rect(screen, (255, 255, 255), (540, 420, 200, 60), 2)  # Draw clickable area
    text_exit = font.render("Exit", True, (255, 255, 255))
    text_exit_rect = text_exit.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
    screen.blit(text_exit, text_exit_rect)

    pygame.display.flip()


def draw_battle_screen(screen):
    screen.fill((0, 0, 0))  # Black background
    font = pygame.font.Font(None, 36)
    text = font.render("Battle Screen", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()


if __name__ == '__main__':
    main()
