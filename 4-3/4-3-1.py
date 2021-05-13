import pygame
import sys
import random

# Color Constants:
BLUE  = (  0,  0,255)
WHITE = (255,255,255)

class Circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # Initializes sprite

        self.image = pygame.Surface([40,50])
        pygame.draw.ellipse(self.image,BLUE,[0,0,40,50])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
    
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fpsClock = pygame.time.Clock()
FPS = 30

done = False

circleObj = Circle()

# Game loop
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.fill(WHITE) # FIXME: WHY TF IS THIS NOT WORKING
    SCREEN.blit(circleObj.image, (circleObj.rect.x, circleObj.rect.y))
    fpsClock.tick(FPS)
