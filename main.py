import pygame, sys
SCREEN_SIZE = (800,800)
FILL_COLOR = (144,100,10)

def drawSnake(snake, color = (0,0,0)):
    for piece in snake:
        pygame.draw.rect(main_sf, color, square)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
main_sf = pygame.Surface((50,50))
main_sf.fill((255,255,255))
clock = pygame.time.Clock()

# Variables
square = pygame.Rect(2,2,1,1)
snake = [square]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(FILL_COLOR)

    drawSnake(snake)
    screen.blit(pygame.transform.scale(main_sf, SCREEN_SIZE), (0,0))

    pygame.display.update()
    clock.tick(120)