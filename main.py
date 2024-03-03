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

    # Load the background image
    background_image = pygame.image.load("testing_bg.png")
    background_rect = background_image.get_rect()

    # Player starting values
    player_speed = 5
    player_position = [SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 1.6]
    player_health = 3

    # Load the character image
    character_image = pygame.image.load("test_player.png")
    character_rect = character_image.get_rect()

    # Load the object image
    object_image = pygame.image.load("nucleus.png")
    enemy_object = object_image.get_rect()
    enemy_object.x = 40
    enemy_object.y = player_position[1]
    enemy_health = 3

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
            screen.blit(background_image, background_rect)

            # Blit the character image onto the screen
            screen.blit(character_image, player_position)

            # Blit the object image onto the screen
            screen.blit(object_image, enemy_object)

            # Left and Right Player Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_position[0] -= player_speed
            if keys[pygame.K_d]:
                player_position[0] += player_speed

            # Update the object's position
            enemy_object.y = player_position[1]

            # Check for collision with object
            if enemy_object.colliderect(
                    pygame.Rect(player_position[0], player_position[1], character_rect.width, character_rect.height)):
                battle_screen_displayed = True
                draw_battle_screen(screen, player_health, enemy_health)

            # Update the display
            pygame.display.update()

            # Limit frame time to 60 fps
            dt = clock.tick(60) / 1000

        elif battle_screen_displayed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    battle_screen_displayed = False

            draw_battle_screen(screen, player_health, enemy_health)
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


def draw_battle_screen(screen, player_health, enemy_health):
    screen.fill((0, 0, 0))  # Black background

    # Draw the battle scene elements
    font = pygame.font.Font(None, 36)
    text = font.render("Battle Screen", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

    # You can add additional elements here, such as UI components, health bars, etc.
    draw_player_hearts(screen, player_health)
    draw_enemy_hearts(screen, enemy_health)

    pygame.display.flip()


def draw_player_hearts(screen, health):
    player_heart_position = 10
    for i in range(health):
        pygame.draw.rect(screen, (255, 0, 0), (player_heart_position, 10, 50, 50), 2)
        player_heart_position += 60


def draw_enemy_hearts(screen, health):
    enemy_heart_position = screen.get_width() - 180
    for i in range(health):
        pygame.draw.rect(screen, (255, 0, 0), (enemy_heart_position, 10, 50, 50), 2)
        enemy_heart_position += 60


if __name__ == '__main__':
    main()
