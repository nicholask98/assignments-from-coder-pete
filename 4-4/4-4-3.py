import pygame
import sys
import random

allSpriteGroup = pygame.sprite.Group()
blueSpriteGroup = pygame.sprite.Group()
redSpriteGroup = pygame.sprite.Group()

# Color Constants:
BLUE  = (  0,  0,255)
WHITE = (255,255,255)
RED   = (255,  0,  0)

class Circle(pygame.sprite.Sprite):
    vel = 1
    def __init__(self, color, xPos, yPos):
        pygame.sprite.Sprite.__init__(self) # Initializes sprite

        self.color = color

        # FIXME: Advanced Programmers challenge
        self.image = turtle
        # self.image = pygame.Surface([40,50])
        # pygame.draw.ellipse(self.image,color,[0,0,40,50])
        
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
        pygame.Surface.set_colorkey(self.image, WHITE)
    
    def update(self):
        if self.color == RED:
            self.rect.y += self.vel
        elif self.color == BLUE:
            self.rect.y -= self.vel
    
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

turtle = pygame.image.load('turtle.jpg').convert_alpha()

fpsClock = pygame.time.Clock()
FPS = 90

done = False

# Circle generation
for i in range(10):
    xPos = random.randint(10, SCREEN_WIDTH - 10)
    if i <= 4:
        yPos = random.randint(10, 150)
        circleObj = Circle(RED, xPos, yPos)
        redSpriteGroup.add(circleObj)
    elif i > 4:
        yPos = random.randint(SCREEN_HEIGHT * 3 // 4, SCREEN_HEIGHT - 10)
        circleObj = Circle(BLUE, xPos, yPos)
        blueSpriteGroup.add(circleObj)
    allSpriteGroup.add(circleObj)

# Game loop
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.sprite.groupcollide(redSpriteGroup, blueSpriteGroup, True, True)

    SCREEN.fill(WHITE)
    allSpriteGroup.draw(SCREEN)
    allSpriteGroup.update()
    pygame.display.flip()
    fpsClock.tick(FPS)
