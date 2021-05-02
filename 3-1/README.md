https://coderpete.com/class/python/pyGame/assignments/pygame_unit3_exercises.php
3-1-1
Open the sample program keyboard_example_move_cat.txt and save it as pg3-1-1.py
Add timing to your program. Following are the three things to add to your program:
FPS = ???? # Define with constant
fpsClock = ?????? # Before game loop
fpsClock.???????(??????) # Inside of the loop

3-1-2
Start with program pg3-1-1.py and save it as pg3-1-2.py.
pg3-1-1 must remain in tact. Make the changes to pg3-1-2.
Do not change FPS as part of this exercise.
Create a constant variable:
CAT_SPEED = 5 (or whatever speed you like)
Use CAT_SPEED to determine how many pixels the cat should move when the player presses an arrow key.

Advanced Programmers:

Add CAT_TURBO to the program and apply additional speed when the user presses the spacebar. Test your program using different turbo speeds.

3-1-3
NOTE: The cat should stop beyond the right and bottom borders. It should stop at the top and left borders (not beyond).

Start with sample program pg3-1-2.pyand save it as pg3-1-3.py.
pg3-1-2 must remain in tact. Make the changes to pg3-1-3.
Allow the cat image to stop just beyond the borders of the screen.
The cat should stop going left at pixel 0 (on the x axis (Not Beyond).
The cat should stop going right at the value stored in constant SCREEN_WIDTH
The cat should stop going up at pixel 0 (on the y axis) (Not Beyond)
The cat should stop going down at the value stored in constant SCREEN_HEIGHT
It is OK for the cat to go just off the right and bottom edges
