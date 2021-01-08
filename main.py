import pygame, sys, random, os

# Put the window on the center of the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

""" ...Constants... """
SCREEN_SIZE = (800,850)
GAME_SIZE = (800,800)
LEMON = (255, 234, 167)
GREEN = (76, 209, 55)
NIGHT = (53, 59, 72)
BLACK = (61, 61, 61)
WHITE = (245, 246, 250)
BARARED = (237, 76, 103)

"""< When the snake do not exist, this add the first square(1 or more) >"""
def createSnake(snk, xPos, yPos, size = 1):
    for i in range(size):
        snk.insert(0, square.copy())
    snk[len(snk) - 1].x = xPos
    snk[len(snk) - 1].y = yPos

"""< Draw the snake but the head will be of a different color than the body >"""
def drawSnake(bodyColor, headColor):
    for i in range(len(snake)):
        # If that is the head
        if i == len(snake) - 1:
            pygame.draw.rect(gameSf, headColor, snake[i])
        else:
            pygame.draw.rect(gameSf, bodyColor, snake[i])

"""< The logic of the snake movement >"""
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


def growSnake(ammount = 0):
    if ammount == 0:
        size = random.randint(1,5)
        for i in range(size):
            snake.insert(0, square.copy())
    else:
        for i in range(ammount):
            snake.insert(0, square.copy())


def createFood():
    # Get a random position on the screen
    x = random.randint(2, gameSf.get_width()-2)
    y = random.randint(2, gameSf.get_height()-2)
    # Check if there is not other food in the random position that we get
    for f in food:
        if f.x == x and f.y == y:
            createFood()
            print("a")
            return
    # Check if the snake is in the position that we generate
    for piece in snake:
        if piece.x == x and piece.y == y:
            createFood()
            print("b")
            return
    # Add the food on the list
    fd = square.copy()
    fd.x = x
    fd.y = y
    food.append(fd)


def drawFood(color = BARARED):
    for f in food:
        pygame.draw.rect(gameSf, color, f)


def checkCollisions():
    global score, gameOver, highScore
    for i in range(len(snake)):
        if i != len(snake) - 1:
            if snake[len(snake) - 1].x == snake[i].x and snake[len(snake) - 1].y == snake[i].y:
                gameOver = True
                deathSound.play()
                pygame.mixer.music.set_volume(gameOverVolume)
                if score > highScore:
                    highScore = score
    
    for i in range(len(food)):
        if food[i].colliderect(snake[len(snake) - 1]):
            score += 1
            random.choice(pointSound).play()
            food.pop(i)
            createFood()
            growSnake()
    
    if (snake[len(snake) - 1].x < 0) or (snake[len(snake) - 1].x > gameSf.get_width() - 1) or (snake[len(snake) - 1].y < 0) or (snake[len(snake) - 1].y > gameSf.get_height() - 1):
        gameOver = True
        deathSound.play()
        pygame.mixer.music.set_volume(gameOverVolume)
        if score > highScore:
            highScore = score


def drawShadows(shadowColor = (LEMON[0] - 20, LEMON[1] - 20, LEMON[2] - 20)):
    shadow = 0
    for f in food:
        shadow = f.copy()
        shadow.x += 1
        shadow.y += 1
        pygame.draw.rect(gameSf, shadowColor, shadow)
    
    for piece in snake:
        shadow = piece.copy()
        shadow.x += 1
        shadow.y += 1
        pygame.draw.rect(gameSf, shadowColor, shadow)


def text(txt, font, xPos, yPos, color = WHITE):
    txtSf = font.render(txt, 1, color).convert_alpha()
    rect = txtSf.get_rect(center = (xPos, yPos))
    return txtSf, rect


def resetValues():
    global score
    global direction

    direction = 'right'
    score = 0
    snake.clear()
    createSnake(snake, initialSnakePos[0], initialSnakePos[1], initialSnakeSize)
    food.clear()
    createFood()

pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 1024)
pygame.init()
# Window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TOM THE SNAKE")
pygame.display.set_icon(pygame.image.load("icon.png"))
# Main surface where we draw the game and later we scale it up
gameSf = pygame.Surface((50,50))
# To control FPS
clock = pygame.time.Clock()
gameFont = pygame.font.Font('Pixeled.ttf', 30)
gameOverFont = pygame.font.Font('Pixeled.ttf', 20)

""" ... Sounds ..."""
pygame.mixer.music.load("sounds/backgroundSound.mp3")
gameOverVolume = 0.2
playingVolume = 1.0
pointSound1 = pygame.mixer.Sound("sounds/pointSound1.wav")
pointSound2 = pygame.mixer.Sound("sounds/pointSound2.wav")
pointSound = [pointSound1, pointSound2]
deathSound = pygame.mixer.Sound("sounds/deathSound.wav")

""" ...Variables... """
square = pygame.Rect(-20,-20,1,1)
# Time(miliseconds) between each snake movement (less mean faster) 
snakeSpeed = 100
direction = 'right'
# This list will contain squares to make the snake
snake = []
initialSnakePos = [5, 5]
initialSnakeSize = 2
# Food list
food = []
score = 0
highScore = 0
gameOver = True

""" ...User events... """
MOVE_SNAKE = pygame.USEREVENT
pygame.time.set_timer(MOVE_SNAKE, snakeSpeed)
TEST = pygame.USEREVENT + 1
pygame.time.set_timer(TEST, 500)

# Start game
createSnake(snake, initialSnakePos[0], initialSnakePos[1], initialSnakeSize)
createFood()
pygame.mixer.music.set_volume(gameOverVolume)
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if gameOver:
                gameOver = False
                resetValues()
                pygame.mixer.music.set_volume(playingVolume)
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_LEFT and not gameOver:
                direction = 'left'
            if event.key == pygame.K_RIGHT and not gameOver:
                direction = 'right'
            if event.key == pygame.K_DOWN and not gameOver:
                direction = 'down'
            if event.key == pygame.K_UP and not gameOver:
                direction = 'up'
            # To quit the game pressing ESC
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOVE_SNAKE and not gameOver:
            moveSnake(direction)

    screen.fill(BLACK)
    gameSf.fill(LEMON)

    if(gameOver):
        # Draw a scaled surface where we draw the snake
        screen.blit(pygame.transform.scale(gameSf, GAME_SIZE).convert_alpha(), (0,SCREEN_SIZE[1] - GAME_SIZE[1]))
        # |PRESS ANY KEY| text
        anyKeyText, anyKeyRect = text("-PRESS ANY KEY TO START-", gameOverFont, int(SCREEN_SIZE[0]/2), 20)
        screen.blit(anyKeyText, anyKeyRect)
        # |HIGH SCORE| text
        highScoreText, highScoreRect = text("HIGH SCORE", gameFont, int(SCREEN_SIZE[0]/2), 300, NIGHT)
        screen.blit(highScoreText, highScoreRect)
        # High score text (the number)
        hSText, hSRect = text(str(highScore), gameFont, int(SCREEN_SIZE[0]/2), 350, GREEN)
        screen.blit(hSText, hSRect)
        # |LAST SCORE| text
        lScoreText, lScoreRect = text("Last Score", gameOverFont, int(SCREEN_SIZE[0]/2), 450, NIGHT)
        screen.blit(lScoreText, lScoreRect)
        # Last score text (the number)
        lSText, lSRect = text(str(score), gameOverFont, int(SCREEN_SIZE[0]/2), 500, GREEN)
        screen.blit(lSText, lSRect)
    else:
        checkCollisions()
        drawShadows()
        drawFood()
        drawSnake(NIGHT, GREEN)
        # Score text
        scoreText, scoreRect = text(str(score), gameFont, int(SCREEN_SIZE[0]/2), 20)
        screen.blit(scoreText, scoreRect)
        # Draw a scaled surface where we draw the snake
        screen.blit(pygame.transform.scale(gameSf, GAME_SIZE).convert_alpha(), (0,SCREEN_SIZE[1] - GAME_SIZE[1]))

    pygame.display.update()
    clock.tick(120)