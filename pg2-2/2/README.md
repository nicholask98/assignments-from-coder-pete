https://coderpete.com/class/python/pyGame/assignments/pygame_unit2_exercises.php

- Save pg2-2-1.py as pg2-2-2.py (we want to keep pg2-2-1.py).
- Set the initial frames per second to 20.
- Modify pg2-2-2.py to increment frames per second by one every 20 frames.
- Test your program.

Questions

- At the bottom of the module, answer the following questions using a '''block''' of comments.
1. In your own words, define the following terms:

- frame.
- FPS
- pygame.time.Clock()

2. What PyGame commands must your program contain in order to utilize time based animation?
3. What method of the Clock() object to you call in the game loop to keep animation consistent regardless of the speed of the host computer?
4. Frame rate in games is considered FPS. There is another term used for monitors. What is that term?
5. What happens if your game’s frame rate is too slow?
6. What does the tick() method do?



## 2-3-1:

Create a module named pg2-3-1.py.
Create a function nameddisplayText()that accepts: text, , xPosition, yPosition, fontName, fontSize, fontColor, and backgroundColor, as parameters and blits the text to DISPLAYSURF.
Use the following parameter defaults:

fontName=None

fontSize=12

fontColor=BLACK

BackgroundColor=WHITE


## 2-3-2:

1. Open pg2-3-1.py and save it as pg2-3-2.py.
    1. Use the displayText() function, inside of a loop, to make the message “I love programming” move in a pattern on your screen.The pattern must be more complex than clockwise or counter-clockwise.
    2. Select a different font, font color, font size, and background color then what the textbook uses.
    3. Test anti-aliasing to see if you think anti-aliasing is worth using:
        - You may need to enlarge the text size up to see the difference.

#### Questions

- At the bottom of the module, answer the following questions using comments.
1. What is the first object your program must create in order to display text on the computer screen.
2. (T/F) You can place text directly on the surface object.
3. How do you specify where to display the text on the screen?
4. Name the five steps for displaying text on the screen.
5. List the two functions used to draw anti-aliasedlinesin PyGame.
    - May need to look at the textbook to answer this question.

If you complete this assignment early

1. Create a module named pg2-3-1b.py containing the code from your pg2-3-1.py logic.
2. Make the text rotate or flip
3. Dynamically change the text color.