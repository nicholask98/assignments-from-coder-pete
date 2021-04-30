import pygame, sys
# Constants:
from pygame.locals import *
SCREEN_XY = (1000, 650)

# Color Constants:
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,150, 50)
RED   = (255,  0,  0)

vert = "RIGHT"
hori = "TOP"
vel = 5


def move_text(textRectObject):
    global vert
    global hori
    if vert == 'RIGHT':
        text_xy[0] -= vel
        text_xy[1] -= vel
    elif vert == 'LEFT':
        text_xy[0] += vel
        text_xy[1] -= vel // 2
    
    if hori == 'TOP':
        text_xy[0] -= vel
        text_xy[1] += vel
    elif hori == 'BOTTOM':
        text_xy[1] -= vel
        text_xy[0] += vel
        
    
    if textRectObject.right >= SCREEN_XY[0]:
        textRectObject.right = SCREEN_XY[0]
        vert = 'RIGHT'
        
    elif textRectObject.left <= 0:
        textRectObject.left = vel
        vert = 'LEFT'
    if textRectObject.top <= 0:
        textRectObject.top = vel
        hori = 'TOP'
    elif textRectObject.bottom >= SCREEN_XY[1]:
        textRectObject.bottom = SCREEN_XY[1]
        hori = 'BOTTOM'


def displayText(text, xPosition, yPosition, fontName=None, fontSize=12, fontColor=BLACK, backgroundColor=WHITE):
    fontObj = pygame.font.SysFont(fontName, fontSize)
    textSurfaceObject = fontObj.render(text, True, fontColor, backgroundColor)
    textRectObject = textSurfaceObject.get_rect()
    textRectObject.center = (xPosition, yPosition)
    DISPLAYSURF.blit(textSurfaceObject, textRectObject)

    move_text(textRectObject)

    

pygame.init()

DISPLAYSURF = pygame.display.set_mode(SCREEN_XY)

text_xy = [SCREEN_XY[0]//2, SCREEN_XY[1]//2]

fpsClock = pygame.time.Clock()
FPS = 60
while True:
    event_queue = pygame.event.get()
    for event in event_queue:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)

    displayText('I love programming', text_xy[0], text_xy[1], fontName='sinhalamn', fontSize=80, fontColor=GREEN, backgroundColor=RED)

    pygame.display.update()
    fpsClock.tick(FPS)


'''
- At the bottom of the module, answer the following questions using comments.
1. What is the first object your program must create in order to display text on the computer screen.
    Font object

2. (T/F) You can place text directly on the surface object.
    This is a trick question. You must create a new Surface object using the Font.render() method. You cannot place text directly on the DISPLAY surface.
3. How do you specify where to display the text on the screen?
    create a Rect object using the surface object and change one of the Rect object attributes (Rect.topleft, Rect.center, etc.)
4. Name the five steps for displaying text on the screen.
    1. Create a Font object
    2. Create a Surface object using the Font object's .render() method
    3. Create a Rect object using the Surface object's get_rect() method
    4. Adjust the positioning of the Rect object by changing its attributes.
    5. Blit the Surface object to the display surface with the format 'displaysurf.blit(Surface_object, Rect object)'
    (6). pygame.display.update()
5. List the two functions used to draw anti-aliasedlinesin PyGame.
    - May need to look at the textbook to answer this question.
    The pygame.draw.aaline() and pygame.draw.aalines()
'''