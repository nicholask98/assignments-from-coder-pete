# Steve Stoll (4/2/2013)
# This program is a simple PyGame template.
# Import the pygame and sys libraries
import pygame
import sys
from pygame.locals import *

xPos = 0
yPos = 0

# Set screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Frames per second
FPS = 8

# Color constants
GREEN = (  0,255,  0)

# Initialize PyGame
pygame.init()
fpsClock = pygame.time.Clock()

# Set the screen size
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Fill the screen with green.
SCREEN.fill(GREEN)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# Mouse events or mouse logic may go here...
    xPos, yPos = pygame.mouse.get_pos()
    print('[', xPos, yPos, ']')
    pygame.display.flip()
    fpsClock.tick(FPS)