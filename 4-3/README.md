## 4-3-1
### Assignment:
1. Create a module named pg4-3-1.py.
2. Within your new module:
    1. Create a Circle class similar to the Block class found in the textbook. Of course, you want to display colored circles instead of blocks.
    2. Your new class must inherit from the pygame.sprite.Sprite class.
    3. Create one instance of the class and display it in random a place on the screen.


#### Sample code to create an ellipse in the circle's constructor:

* self.image = pygame.Surface([40,50]) 
* pygame.draw.ellipse(self.image,BLUE,[0,0,40,50])
* self.rect = self.image.get_rect()



#### Sample Code to blit the object's image to the screen:

* \# Clear the SCREEN
* SCREEN.fill(WHITE)

* \# Blit the circleObj object instance.
* SCREEN.blit(circleObj.image, (xPos, yPos))