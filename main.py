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
    background_image = pygame.image.load("Images/cell_background.png")
    background_rect = background_image.get_rect()

    # Player starting values
    player_speed = 5
    player_position = [SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 1.3]

    # Load the character image
    character_image = pygame.image.load("Images/player.png")
    character_rect = character_image.get_rect()

    # Load the object image
    object_image = pygame.image.load("Images/nucleus.png")
    enemy_object = object_image.get_rect()
    enemy_object.x = 50
    enemy_object.y = player_position[1]

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
                    if 240 <= x <= 850 and 400 <= y <= 500:  # Start button area
                        start_screen_displayed = False
                    elif 1150 <= x <= 1320 and 20 <= y <= 80:                        # Exit button area
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and battle_screen_displayed:
                if event.button == 1:  # Left mouse button
                    battle_screen_displayed = False

        if not start_screen_displayed and not battle_screen_displayed:
            # Clear the screen
            screen.blit(background_image, background_rect)

            # Using the Blit method to put the character image onto the screen
            screen.blit(character_image, player_position)

            # Using the Blit method to put the object image onto the screen
            screen.blit(object_image, enemy_object)

            # Left and Right Player Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_position[0] -= player_speed
            if keys[pygame.K_d]:
                player_position[0] += player_speed

            # Update the object's position
            enemy_object.y = player_position[1] - 100

            # Check for collision with object
            if enemy_object.colliderect(
                    pygame.Rect(player_position[0], player_position[1], character_rect.width, character_rect.height)):
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
    main_background_image = pygame.image.load("Images/home_screen.png")
    main_background_rect = main_background_image.get_rect()
    screen.blit(main_background_image, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 100))
    screen.blit(text, text_rect)



    pygame.display.flip()


def draw_battle_screen(screen):
    # Load the battle background image
    battle_background_image = pygame.image.load("Images/testing_battle.png")
    battle_background_rect = battle_background_image.get_rect()

    screen.blit(battle_background_image, (0, 0))

    # Draw the battle scene elements
    font = pygame.font.Font(None, 36)
    text = font.render("Battle Screen", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

    # You can add additional elements here, such as UI components, health bars, etc.

    pygame.display.flip()



if __name__ == '__main__':
    main()