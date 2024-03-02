import pygame

pygame.init()

#creates the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

def draw_text(text, font, text_coL, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# run game
run = True
while run:
    screen.fill((52, 78, 91))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
    pygame.display.update()

pygame.quit()
