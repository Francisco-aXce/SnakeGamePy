import pygame, sys
SCREEN_SIZE = (800,800)
FILL_COLOR = (144,100,10)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# Variables

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(FILL_COLOR)

    pygame.display.update()