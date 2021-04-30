import pygame, sys
# Constants:
from pygame.locals import *
SCREEN_XY = (1000, 650)

# Color Constants:
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,150, 50)
RED   = (255,  0,  0)

def displayText(text, xPosition, yPosition, fontName=None, fontSize=12, fontColor=BLACK, backgroundColor=WHITE):
    fontObj = pygame.font.SysFont(fontName, fontSize)
    textSurfaceObject = fontObj.render(text, True, fontColor, backgroundColor)
    textRectObject = textSurfaceObject.get_rect()
    textRectObject.center = (xPosition, yPosition)
    pygame.transform.rotate(textSurfaceObject, 60)
    
pygame.init()

DISPLAYSURF = pygame.display.set_mode(SCREEN_XY)

text_xy = [SCREEN_XY[0]//2, SCREEN_XY[1]//2]

fpsClock = pygame.time.Clock()
FPS = 60

font_color = BLACK
count = 0
while True:
    count += 1
    event_queue = pygame.event.get()
    for event in event_queue:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)
    if 0 <= count < 50:
        font_color = BLACK
    elif 50 <= count < 100:
        font_color = WHITE
    elif 100 <= count < 150:
        font_color = RED
    else:
        font_color = GREEN
    
    if count == 200:
        count = 0 

    textSurfaceObject = displayText('I love programming', text_xy[0], text_xy[1], fontName='sinhalamn', fontSize=80, fontColor=font_color, backgroundColor=RED)
    
    pygame.display.update()
    fpsClock.tick(FPS)
