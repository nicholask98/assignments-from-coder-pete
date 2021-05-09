# Modified for classroom standards and timing.
# Steve Stoll (3/24/2013)
## This program allows users to move a cat using the keyboard.
## Import the pygame and sys libraries
import pygame
import sys
from pygame.locals import *

## The images are in the same folder as the program
backgroundImg = "background.jpg"
catImg = "cat.png"

## Use the following code if you want to place the images in a 
##    sub-folder named images.
        ##bkg_img = "\images\background.jpg"
        ##mouse_img = "\images\cat.png"

## Set the x, y, directionX, directionY variables
xPos = 0
yPos = 0

# Indicates the x or y direction (+value, -value or zero)
directionX = 0
directionY = 0

# Speed
CAT_VEL = 5

# Set screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

## Initialize PyGame
pygame.init()

## Clock stuff
FPS = 30
fpsClock = pygame.time.Clock()

## Set the screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

## Load the background and cursor images.
background = pygame.image.load(backgroundImg).convert()
cat = pygame.image.load(catImg).convert_alpha()

## Main loop
while True:
    ## Logic to cleanup after user presses close (red X)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        ## event logic to capture when the user presses arrow keys.
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                directionX = -CAT_VEL
            elif event.key == K_RIGHT:
                directionX = +CAT_VEL
            elif event.key == K_UP:    
                directionY = -CAT_VEL
            elif event.key == K_DOWN:
                directionY = +CAT_VEL

        if event.type == KEYUP:
            if event.key == K_LEFT:
                directionX = 0
            elif event.key == K_RIGHT:
                directionX = 0
            elif event.key == K_UP:
                directionY = 0
            elif event.key == K_DOWN:
                 directionY = 0

    catRect = cat.get_rect()
    xPosPlusWidth = catRect.width + xPos
    yPosPlusHeight = catRect.height + yPos

    ## This logic identifies where the object should move
    if (xPos <= 0 and directionX < 0) or (xPosPlusWidth > SCREEN_WIDTH and directionX) > 0:
        directionX =  0
    if (yPos <= 0 and directionY < 0) or (yPosPlusHeight > SCREEN_HEIGHT and directionY) > 0:
        directionY =  0
    if 0 <= xPos and directionX < 0 or xPos <= SCREEN_WIDTH and directionX > 0:
        xPos += directionX
    if 0 <= yPos and directionY < 0 or yPos <= SCREEN_HEIGHT and directionY > 0:
        yPos += directionY
    

    ## Repaint the screen with the objects in the new positions
    screen.blit(background, (0, 0))
    screen.blit(cat, (xPos, yPos))
    pygame.display.flip()
    fpsClock.tick(FPS)


'''
- Describe how the catRect, xPosPlusWidth, and xPosPlusHeight variables are used in the program.
    - catRect variable is used to access the width and height instance variables for the cat image in order to determine the correct place to stop the movement before it crosses the borders of the screen.
    - xPosPlusWidth is a variable used in the same way that the rect.right attribute works. It accesses the x coordinate of the right side of the rect (in this case the right side of the cat image.)
    - yPosPlusHeight has the same purpose as the xPosPlusWidth variable except it tracks the bottom side of the rect.
- In what way are we using the Rect object?
    - We are using the Rect object to calculate the edges of the image to create borders for movement.
- Is there a more efficient way to do this? If yes, please discuss with the instructor or a lab assistant.
    - Yes, by using the catRect.right and catRect.bottom attributes. Or you could use the catRect.bottomright attribute which returns a tuple with format (x, y).
'''