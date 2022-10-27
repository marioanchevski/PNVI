import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
# frames per second setting
fpsClock = pygame.time.Clock()


#background music
pygame.mixer.music.load('media/background-music.mp3')
pygame.mixer.music.play(-1, 3)
#to stop the music
#pygame.mixer.music.stop()
soundObj = pygame.mixer.Sound('media/BerserkerCaster.wav')
soundObj.play()


# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)
catImg = pygame.image.load('media/cat.png')
catx = 10
caty = 10
direction = 'right'

DISPLAYSURF.fill(WHITE)
while True: # the main game loop

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
            DISPLAYSURF.fill(YELLOW)
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            DISPLAYSURF.fill(YELLOW)
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
            DISPLAYSURF.fill(YELLOW)
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            DISPLAYSURF.fill(YELLOW)

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
