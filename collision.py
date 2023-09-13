import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

# Initialize game state variables.
gameOver = False
gameStarted = False
gameOverDelay = 60  # Number of frames before game over can occur (adjust as needed)
frameCount = 0

# Define MOVESPEED here.
MOVESPEED = 6

while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if not gameOver:
        if frameCount < gameOverDelay:
            frameCount += 1
        else:
            if not gameStarted:
                # Initialize game by adding initial food squares
                for i in range(20):
                    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                                             random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
                gameStarted = True

            # Handle player input and game logic
            keys = pygame.key.get_pressed()
            if keys[K_LEFT] or keys[K_a]:
                player.left -= MOVESPEED
            if keys[K_RIGHT] or keys[K_d]:
                player.left += MOVESPEED
            if keys[K_UP] or keys[K_w]:
                player.top -= MOVESPEED
            if keys[K_DOWN] or keys[K_s]:
                player.top += MOVESPEED

            foodCounter += 1
            if foodCounter >= NEWFOOD:
                # Add new food.
                foodCounter = 0
                foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
                                         random.randint(0, WINDOWHEIGHT - FOODSIZE),
                                         FOODSIZE, FOODSIZE))

            # Move the player within the screen boundaries.
            player.left = max(0, min(player.left, WINDOWWIDTH - player.width))
            player.top = max(0, min(player.top, WINDOWHEIGHT - player.height))

            # Check whether the player has intersected with any food squares.
            for food in foods[:]:
                if player.colliderect(food):
                    gameOver = True
                    break  # Exit the loop immediately on game over
                    foods.remove(food)  # Remove this line

            # Draw the white background onto the surface.
            windowSurface.fill(WHITE)

            # Draw the player onto the surface.
            pygame.draw.rect(windowSurface, BLACK, player)

            # Draw the food.
            for i in range(len(foods)):
                pygame.draw.rect(windowSurface, GREEN, foods[i])

    if gameOver:
        # Game over logic goes here.
        gameOverFont = pygame.font.Font(None, 72)
        gameOverText = gameOverFont.render('Game Over', True, BLACK)
        gameOverRect = gameOverText.get_rect()
        gameOverRect.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)
        windowSurface.blit(gameOverText, gameOverRect)

    pygame.display.update()
    mainClock.tick(40)









