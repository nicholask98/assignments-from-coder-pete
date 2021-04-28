## Original code from TheNewBoston.com  ("Under <programming> <Game Development>")

## The images should be in the same folder as the program
bkg_img = "background.jpg"
pizza_img = "pizza_cursor.png"

## Import the pygame and sys libraries
import pygame, sys
from pygame.locals import *

BLACK = (  0,  0,  0)
WHITE = (255,255,255)

def namedisplayText(text, xPosition, yPosition, fontName=None, fontSize=12, fontColor=BLACK, backgroundColor=WHITE):
    screen.blit(text, xPosition, yPosition, fontName, fontSize, fontColor, backgroundColor)

## Initialize PyGame
pygame.init()

## Set the screen size
screen = pygame.display.set_mode((640, 480), 0, 32)

## Load the background and cursor images.
background = pygame.image.load(bkg_img).convert()
mouse_csr = pygame.image.load(pizza_img).convert_alpha()



## Have the pizza start on the upper left corner of the screen.
posX = 0
posY = 0

## Set FPS variable and initialize Clock Object
fpsClock = pygame.time.Clock() ## The clock object is used to have consistent timing on all computers.
FPS = 20
frame_counter = 0

speedX = 100                    ## This makes the speed adjustable
speedY = 300

## Main loop for the program - Includes logic to cleanup when user
##  presses close (red X)
while True:
    pygame.display.set_caption(str(FPS))
    frame_counter += 1
    if frame_counter == 20:
        frame_counter = 0
        FPS += 1


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
    fpsClock.tick(FPS)


    '''
    1.
    - a frame is a single still image in an animation. Many frames that are slightly altered and viewed in rapid succession create the illusion of movement
    - FPS is frames per second. It is a number that corresponds to the amount of [still images](frames) viewed [for each](per) interval of 1 second of time that passes
    - pygame.time.Clock() is an Object in the 'time' module located inside the 'pygame' module. This type of Object can track the amount of time since its initialization and has many methods that can be used to manipulate, alter, and utilize time.
    
    2. There must be an initialized Clock object, an FPS variable, and a regular call to the Object's tick() method including the FPS variable as a parameter. Alternatively one could just include an integer as a tick() argument and not include an FPS variable, but this would prove to be a less flexible option.
    3. tick() method
    4. Hertz
    5. The game runs too slow.
    6. The Clock.tick() method is used to track the amount of time since the last call to .tick() for that instance of the object. This method pauses the program for the amount of time required to achieve the FPS that is included as its parameter.
    '''