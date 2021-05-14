import pygame
import sys
import random

from pygame.draw import circle

allSpriteGroup = pygame.sprite.Group()

# Color Constants:
BLUE  = (  0,  0,255)
WHITE = (255,255,255)
RED   = (255,  0,  0)

class Circle(pygame.sprite.Sprite):
    def __init__(self, color, xPos, yPos):
        pygame.sprite.Sprite.__init__(self) # Initializes sprite

        self.image = pygame.Surface([40,50])
        pygame.draw.ellipse(self.image,color,[0,0,40,50])
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
        pygame.Surface.set_colorkey(self.image, [0,0,0])
    
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fpsClock = pygame.time.Clock()
FPS = 30

done = False

# Circle generation
for i in range(20):
    xPos = random.randint(10, SCREEN_WIDTH - 10)
    if i <= 9:
        yPos = random.randint(10, 150)
        circleObj = Circle(RED, xPos, yPos)
    elif i > 9:
        yPos = random.randint(SCREEN_HEIGHT * 3 // 4, SCREEN_HEIGHT - 10)
        circleObj = Circle(BLUE, xPos, yPos)
    allSpriteGroup.add(circleObj)

# Game loop
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.fill(WHITE)
    allSpriteGroup.draw(SCREEN)
    pygame.display.flip()
    fpsClock.tick(FPS)
