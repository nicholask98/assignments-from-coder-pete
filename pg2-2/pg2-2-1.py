## Original code from TheNewBoston.com  ("Under <programming> <Game Development>")

## The images should be in the same folder as the program
bkg_img = "background.jpg"
pizza_img = "pizza_cursor.png"

## Import the pygame and sys libraries
import pygame, sys
from pygame.locals import *

## Initialize PyGame
pygame.init()

## Set the screen size
screen = pygame.display.set_mode((640, 480), 0, 32)

## Load the background and cursor images.
background = pygame.image.load(bkg_img).convert()
mouse_csr = pygame.image.load(pizza_img).convert_alpha()

## Set FPS variable and initialize Clock Object
fpsClock = pygame.time.Clock()
FPS = 40

## Have the pizza start on the upper left corner of the screen.
posX = 0
posY = 0

clock = pygame.time.Clock()     ## The clock object is used to have consistent timing on all computers.
speedX = 100                    ## This makes the speed adjustable
speedY = 300

## Main loop for the program - Includes logic to cleanup when user
##  presses close (red X)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ## Place the background image on the screen.
    screen.blit(background, (0, 0))
    screen.blit(mouse_csr, (posX, posY))

    posX += 1
    posY += 1

    if posX > 640:
        posX = 0

    if posY > 480:

        posY = 0

    ## Update the screen
    pygame.display.update()
    fpsClock.tick(2000)