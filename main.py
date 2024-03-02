import pygame

def main():
    # pygame initializer
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets resolution
    clock = pygame.time.Clock() 
    running = True
    dt = 0
    
    # Home Screen
    pygame.display.set_caption("Main Menu")
    
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    
    player_speed = 5
    player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.2)

    while running:
        screen.fill((52, 78, 91))
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Left and Right Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_position.x -= player_speed
        if keys[pygame.K_d]:
            player_position.x += player_speed

        screen.fill("white") # Makes background white
        pygame.draw.circle(screen, "red", player_position, 40) # Creates player

        # Shows game elements and limits frame time to 60 fps
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    # Quits game
    pygame.quit()

if __name__ == '__main__': 
    main()
