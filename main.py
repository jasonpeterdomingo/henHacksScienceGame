import pygame
import sys

# Player class
class Player(object):
    def __init__(self, position):
        self.position = position
        self.vel = 5
        self.health = 3

# Enemy class
class Enemy(object):
    def __init__(self, position):
        self.position = position
        self.health = 3

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

    # Load the character image
    character_image = pygame.image.load("Images/test_player.png")
    character_rect = character_image.get_rect()

    # Load the object image
    enemy_image = pygame.image.load("Images/nucleus.png")
    enemy_object = enemy_image.get_rect()

    # Entity initialization
    player = Player([SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 1.6])
    enemy = Enemy([40, player.position[1]])
    
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
            screen.blit(enemy_image, enemy.position)

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
                draw_battle_screen(screen, player, enemy)

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

            draw_battle_screen(screen, player, enemy)
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


def draw_battle_screen(screen, player: Player, enemy: Enemy):
    screen.fill((0, 0, 0))  # Black background

    # Draw the battle scene elements
    font = pygame.font.Font(None, 36)
    text = font.render("Battle Screen", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    font2 = pygame.font.Font(None, 30)
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 13.25, screen.get_height() / 1.3, 450, 100), 2)
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 1.68, screen.get_height() / 1.365, 180, 60), 2)
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 1.68, screen.get_height() / 1.15, 180, 60), 2)
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 1.252, screen.get_height() / 1.365, 180, 60), 2)
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 1.252, screen.get_height() / 1.15, 180, 60), 2)
    text2_1 = font2.render("Question: The cell's genetic material is", True, (255, 255, 255))
    text2_2 = font2.render("stored in structures called what?", True, (255, 255, 255))
    text2_3 = font2.render("a) Cytoplasms", True, (255, 255, 255))
    text2_4 = font2.render("b) Nuclear Pores", True, (255, 255, 255))
    text2_5 = font2.render("c) mRNA", True, (255, 255, 255))
    text2_6 = font2.render("d) Chromosomes", True, (255, 255, 255))
    text2_1_rect = text2_1.get_rect(center=(screen.get_width() / 4, screen.get_height() / 1.225))
    text2_2_rect = text2_2.get_rect(center=(screen.get_width() / 4, screen.get_height() / 1.175))
    text2_3_rect = text2_3.get_rect(center=(screen.get_width() / 1.5, screen.get_height() / 1.3))
    text2_4_rect = text2_4.get_rect(center=(screen.get_width() / 1.15, screen.get_height() / 1.3))
    text2_5_rect = text2_5.get_rect(center=(screen.get_width() / 1.554, screen.get_height() / 1.1))
    text2_6_rect = text2_6.get_rect(center=(screen.get_width() / 1.15, screen.get_height() / 1.1))
    screen.blit(text2_1, text2_1_rect)
    screen.blit(text2_2, text2_2_rect)
    screen.blit(text2_3, text2_3_rect)
    screen.blit(text2_4, text2_4_rect)
    screen.blit(text2_5, text2_5_rect)
    screen.blit(text2_6, text2_6_rect)

    # Health
    draw_player_hearts(screen, player.health)
    draw_enemy_hearts(screen, enemy.health)

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