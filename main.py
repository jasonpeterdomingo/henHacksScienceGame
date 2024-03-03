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
    background_image = pygame.image.load("Images/testing_bg.png")
    background_rect = background_image.get_rect()

    # Player class
    class Player(object):
        def __init__(self, position):
            self.position = position
            self.vel = 5
            
    # Player initialization
    player = Player([SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 1.6])

    # Load the character image
    character_image = pygame.image.load("Images/test_player.png")
    character_rect = character_image.get_rect()

    # Load the object image
    object_image = pygame.image.load("Images/nucleus.png")
    enemy_object = object_image.get_rect()
    enemy_object.x = 40
    enemy_object.y = player.position[1]

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
            screen.blit(character_image, player.position)

            # Blit the object image onto the screen
            screen.blit(object_image, enemy_object)

            # Left and Right Player Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.position[0] -= player.vel
            if keys[pygame.K_d]:
                player.position[0] += player.vel

            # Update the object's position
            enemy_object.y = player.position[1]

            # Check for collision with object
            if enemy_object.colliderect(
                    pygame.Rect(player.position[0], player.position[1], character_rect.width, character_rect.height)):
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

    # Draw the battle scene elements
    font = pygame.font.Font(None, 36)
    text = font.render("Battle Screen", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

    # You can add additional elements here, such as UI components, health bars, etc.

    pygame.display.flip()


if __name__ == '__main__':
    main()
