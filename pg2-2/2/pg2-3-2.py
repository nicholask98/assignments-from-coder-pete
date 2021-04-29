import pygame, sys
# Constants:
from pygame.locals import *
SCREEN_XY = (1000, 650)

# Color Constants:
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,150, 50)
RED   = (255,  0,  0)


# WORKING ON THIS FUNCTION CURRENTLY. FOR SOME REASON THE PROGRAM TAKES A WHILE TO LOAD BEFORE CRASHING
def displayText(text, xPosition, yPosition, fontName=None, fontSize=12, fontColor=BLACK, backgroundColor=WHITE):
    fontObj = pygame.font.Font(fontName, fontSize)
    textSurfaceObject = fontObj.render(text, True, fontColor, backgroundColor)
    textRectObject = textSurfaceObject.get_rect()
    textRectObject.topleft = (xPosition, yPosition)
    DISPLAYSURF.blit(textSurfaceObject)

pygame.init()

DISPLAYSURF = pygame.display.set_mode(SCREEN_XY)

text_xy = [SCREEN_XY[0]//2, SCREEN_XY[1]//2]

while True:
    event_queue = pygame.event.get()
    for event in event_queue:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    

    displayText('I love programming', text_xy[0], text_xy[1], fontName=pygame.font.match_font('farisi'), fontSize=36, fontColor=GREEN, backgroundColor=RED)

    pygame.display.update()

