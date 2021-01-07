import pygame, sys
SCREEN_SIZE = (800,800)
FILL_COLOR = (144,100,10)

def drawSnake():
    for i in range(len(snake)):
        if i == len(snake) - 1:
            pygame.draw.rect(main_sf, (200, 0, 0), snake[i])
        else:
            pygame.draw.rect(main_sf, (0, 0, 0), snake[i])


def moveSnake(dir):
    dirX = 0
    dirY = 0
    lastX = 0
    lastY = 0
    auxLastX = 0
    auxLastY = 0

    if dir == 'right':
        dirX = 1
    elif dir == 'left':
        dirX = -1
    if dir == 'down':
        dirY = 1
    elif dir == 'up':
        dirY = -1
        
    for i in reversed(range(len(snake))):
        if i == len(snake) - 1:
            lastX = snake[i].x
            lastY = snake[i].y
            snake[i].x += dirX
            snake[i].y += dirY
        else:
            auxLastX = snake[i].x
            auxLastY = snake[i].y
            snake[i].x = lastX
            snake[i].y = lastY
            lastX = auxLastX
            lastY = auxLastY


def growSnake():
    snake.insert(0, square.copy())

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
main_sf = pygame.Surface((50,50))
main_sf.fill((255,255,255))
clock = pygame.time.Clock()

# Variables
square = pygame.Rect(5,5,1,1)
snake = [square.copy()]
snakeSpeed = 100
direction = 'right'

MOVE_SNAKE = pygame.USEREVENT
pygame.time.set_timer(MOVE_SNAKE, snakeSpeed)
TEST = pygame.USEREVENT + 1
pygame.time.set_timer(TEST, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            if event.key == pygame.K_DOWN:
                direction = 'down'
            if event.key == pygame.K_UP:
                direction = 'up'
        if event.type == MOVE_SNAKE:
            moveSnake(direction)
        if event.type == TEST:
            growSnake()

    screen.fill(FILL_COLOR)
    main_sf.fill((255,255,255))

    drawSnake()

    screen.blit(pygame.transform.scale(main_sf, SCREEN_SIZE), (0,0))
    pygame.display.update()
    clock.tick(120)