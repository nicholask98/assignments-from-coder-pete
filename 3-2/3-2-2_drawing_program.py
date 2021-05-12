# Steve Stoll (4/2/2013)
# This program is a simple PyGame template.
# Import the pygame and sys libraries
import pygame
import sys
from pygame.locals import *
import math

xPos = 0
yPos = 0

# Set screen width and height
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Frames per second
FPS = 90

# Color constants
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)

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

        # Mouse logic
        if event.type == MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            xPos_1, yPos_1 = pygame.mouse.get_pos()
        if event.type == MOUSEMOTION:
            mouse_pressed = pygame.mouse.get_pressed()
            xPos_1, yPos_1 = pygame.mouse.get_pos()
            if mouse_pressed[0]:
                pygame.draw.rect(SCREEN, RED, (xPos_1, yPos_1, 10, 10))
            # Draw shapes
        # if event.type == MOUSEBUTTONUP:
        #     xPos_2, yPos_2 = pygame.mouse.get_pos()
        #     if mouse_pressed[0]:
        #         pygame.draw.rect(SCREEN, RED, (xPos_1, yPos_1, abs(xPos_1 - xPos_2), abs(yPos_1 - yPos_2)))
        #     if mouse_pressed[2]:
        #         pygame.draw.rect(SCREEN, BLUE, (xPos_1, yPos_1, abs(xPos_1 - xPos_2), abs(yPos_1 - yPos_2)))

    
    pygame.display.flip()
    fpsClock.tick(FPS)