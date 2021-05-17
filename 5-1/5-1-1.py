#  This program is part 2 of the Space Shooter project.  It contains code for both the 
#       player and enemy classes.

import pygame
import random
import sys

# ***   Enemy Class   ***
# ***   Enemy Class   ***
class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(ENEMY_SHIP_1).convert()
		self.rect = self.image.get_rect()

	def update(self):
		if self.rect.y > SCREEN_HEIGHT:
			self.kill()
			#print('Enemy ship object should be deleted.')
		else:
			self.rect.y += ENEMY_SHIP_SPEED

# ***   Player Class   ***
# ***   Player Class   ***
class Player(pygame.sprite.Sprite):

	def __init__(self):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(PLAYER_SHIP).convert()

		self.rect = self.image.get_rect()

# **********	 CONSTANTS	 **********
# **********	 CONSTANTS	 **********
# Define colors
BLACK	= (0, 0, 0)
WHITE	= (255, 255, 255)
RED	  = (255, 0, 0)
BLUE	 = (0, 0, 255)

FPS = 30  # Game Speed (Frames Per Second)

# Set the height and width of the screen
SCREEN_HEIGHT = 650
SCREEN_WIDTH = 1000

# Image Locations
PLAYER_SHIP = 'images/Galaga_player_ship.png'
ENEMY_SHIP_1 = 'images/Galaga_Dragonfly.png'
#ENEMY_SHIP_1 = 'images/GLX_Flagship.png'

# Other constants
ENEMY_SHIP_COUNT = 10	   # The number of enemy ships to create initially.
ENEMY_SHIP_SPEED = 3		# The number of pixels the enemy ship moves per frame.
PLAYER_SHIP_SPEED = 12		# The number of pixels the player ship moves per frame.

# CODE EXECUTION BEGINS HERE
# CODE EXECUTION BEGINS HERE

# Initialize Pygame
pygame.init()

# Create the window (primary surface)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# **********	 SPRITE LISTS (For animation and collision detection)	 **********
allSpritesGroup = pygame.sprite.Group()  # List of all sprites (enemies, bullets, and playerShip)
enemyGroup = pygame.sprite.Group()  		# List of each enemy in the game

# **********	 CREATE ENEMY SHIPS	 **********
for i in range(ENEMY_SHIP_COUNT):
	# This represents an Enemy
	enemyObj = Enemy()

	# Set a random location for the enemy
	enemyObj.rect.x = random.randrange(SCREEN_WIDTH - 50)
	enemyObj.rect.y = random.randrange(SCREEN_HEIGHT - 450)

	# Add the enemy to the group of objects
	enemyGroup.add(enemyObj)
	allSpritesGroup.add(enemyObj)

# Create the player's ship
playerObj = Player()
allSpritesGroup.add(playerObj)

# Used to manage how fast the SCREEN updates
fpsClock = pygame.time.Clock()

playerObj.rect.y = SCREEN_HEIGHT - 50	# Position the player ship.
playerShipMove = 0	  # used to move the player ship when the arrow keys are pressed.

# **********	 MAIN PROGRAM LOOP	 **********
while True:
	# **********	 EVENT PROCESSING	 **********
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			# Move the ship left?
			if event.key == pygame.K_LEFT:
					playerShipMove = -PLAYER_SHIP_SPEED
			# Move the ship right?
			if event.key == pygame.K_RIGHT:
				playerShipMove = PLAYER_SHIP_SPEED

		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_LEFT and playerShipMove < 0 or
				event.key == pygame.K_RIGHT and playerShipMove > 0):
				#print('Keyup should stop movement in: ' + str(event.key) + ' direction')
				playerShipMove = 0


	# Move the player ship.
	playerObj.rect.x += playerShipMove

	# Update enemyGroup to move enemy ships.
	enemyGroup.update()

	# **********	 DRAW SCREEN	 **********
	# Clear the SCREEN
	screen.fill(WHITE)

	# Draw all the spites
	allSpritesGroup.draw(screen)

	# Make the game slow down to value set in FPS constant.
	fpsClock.tick(FPS)
	
	# Update the screen with what we've drawn.
	pygame.display.flip()