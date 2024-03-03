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
    background_image = pygame.image.load("Images/cell_background.png")
    background_rect = background_image.get_rect()
    
    # Load the character image
    character_image = pygame.image.load("Images/player.png")
    character_rect = character_image.get_rect()

    # Load the enemy image
    enemy_image = pygame.image.load("Images/nucleus.png")
    enemy_object = enemy_image.get_rect()

    # Entity initialization
    player = Player([SCREEN_WIDTH / 2.5, SCREEN_HEIGHT / 1.3])
    enemy = Enemy([40, player.position[1] -100])

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
            enemy_object.y = player.position[1] - 100


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
    main_background_image = pygame.image.load("Images/home_screen.png")
    main_background_rect = main_background_image.get_rect()
    screen.blit(main_background_image, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 100))
    screen.blit(text, text_rect)



    pygame.display.flip()


def draw_battle_screen(screen, player: Player, enemy: Enemy):
    screen.fill((0, 0, 0))  # Black background
    
    # Load the battle background image
    battle_background_image = pygame.image.load("Images/battle.png")
    battle_background_rect = battle_background_image.get_rect()

    screen.blit(battle_background_image, (0, 0))

    # Draw the battle scene elements
    font = pygame.font.Font(None, 36)
    text = font.render("", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

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