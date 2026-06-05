# Project 9: Snake Game
I built a Snake game using the **Jack** programming language.

## Overview
The goal of this project was to write a real application, where I used object-oriented programming to create an interactive game that runs on the Hack Computer.

## Key Features
- **Snake Movement:** I used an array to keep track of the snake's body parts and their positions.
- **Game Logic:** The game includes rules for moving, eating food to grow, and checking if the snake hits a wall or itself.
- **Controls:** The game listens to the keyboard. You use the arrow keys to change the snake's direction.
- **Graphics:** I used the `Screen` library to draw rectangles for the snake and the food on the screen.

## How to Play
1. Compile the code using the Nand2Tetris `JackCompiler`.
2. Load the files into the **CPU Emulator**.
3. Run the `Main` class.
4. Use the **Arrow Keys** to move.
5. Press **'Q'** if you want to quit the game.

## My Classes
- **Main:** Starts the game.
- **SnakeGame:** Manages the game loop, user input, and the scoreboard.
- **Snake:** Handles the movement, growth, and collision rules.
- **Food:** Creates the food in a new place every time the snake eats it.

## Lessons Learned
- I learned how to organize code into different classes.
- I practiced using the `Screen` and `Keyboard` libraries.
- I learned how to manage memory by using `dispose()` to clean up objects when they are not needed anymore.