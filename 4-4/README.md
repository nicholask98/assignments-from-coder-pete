# Assignment
## 4-4-1

1. Edit pg4-3-1.py and save it as pg4-4-1.py

2. Add a sprite group variable just after the import statements named allSpriteGroup:
    - You will use this group to position all of the sprites on the screen..
    - When you create a circle object (instance of Circle class), add it to the allSpriteGroup.

3. Circle's Class Constructor:
    - The constructor must receive three parameters when creating an instance of the class:
        1. color
        2. xPos
        3. yPos
    - Calculate and store the random position of the class instance as: self.x and self.y

4. Use a loop to create twenty circle objects on the screen in somewhat random positions.

5. Calculate the random (x, y) coordinates and pass them as parameters when creating instances of the Circle class.
    - Ten RED circles across the top of the screen.
        1. Random x: Between 10 and the (width of the screen -10)
        2. Random y: Between 10 and 150
    - Ten BLUE circles toward the bottom of the screen (bottom 20% of the screen).
        1. Random x: Between 10 and the (width of the screen -10)
        2. Random y: Between 250 and the (height of the screen - 10)

    * Do not forget to add each circle object to the allSpriteGroup after you create it.

6. Immediately after you fill the screen with the background color, call the draw() method of the allSpriteGroup to place the sprites on the screen.


## 4-4-2

1. Edit pg4-4-1.py and save it as pg4-4-2.py

2. Add an update(self) method to your Circle class. This method moves red circle objects down five pixels per frame and blue Circle objects up five pixels per frame.

3. Don't forget to call the update() method using allSpriteGroup before executing the pygame.display.flip() command.

## 4-4-3

1. Edit pg4-4-2.py and save it as pg4-4-3.py

2. Add two new sprite groups to your program:
    - blueSpriteGroup- Add each blue sprite to this group immediately after you create it.
    - redSpriteGroup- Add each red sprite to this group immediately after you create it.
3. When the circles touch (collide), remove both of them from the screen. The syntax should be similar to this:
    - pygame.sprite.groupcollide(group1???, group2???, True, True)

* Note: group1 and group2 are Sprite groups. True means destroy the colliding sprite from the related group. Therefore, the first True means destroy the colliding sprite from group1 and the second True means destroy the colliding sprite from group2.


### Advanced Programmers: 
#### (if you complete your assignment early, you count as advanced)

1. Replace the circle with an image you found on the Internet.