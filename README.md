# Brick-Breaker Game

This is a simple brick-breaking game created using the `turtle` module in Python. The game consists of three main components: the ball, the paddle, and the wall of bricks. The player controls the paddle to prevent the ball from falling off the screen while breaking bricks arranged in rows.

## Features
- **Ball Movement**: The ball moves across the screen and bounces off walls and the paddle.
- **Paddle Control**: The paddle is controlled using the left and right arrow keys to prevent the ball from falling off the screen.
- **Bricks Wall**: The game features three rows of bricks in different colors: red, blue, and yellow. Each row contains 12 bricks, totaling 36 bricks on the screen.
- **Scoring**: The game keeps track of the score, with each brick hit contributing to the score.
- **Game Over Condition**: The game ends when the player runs out of attempts or when all bricks are destroyed.

## Classes

### Ball Class
The `Ball` class handles the movement of the ball, including interactions with the paddle and bricks. It also controls the ball's speed and the change of direction upon hitting boundaries or the paddle.

#### Key Methods:
- `make_ball()`: Initializes the ball object.
- `paddle_impact()`: Detects when the ball hits the paddle and changes direction.
- `move_and_hit_boundary()`: Moves the ball and checks for boundary collisions.
- `break_wall()`: Detects collisions with bricks and hides the broken bricks.

### Paddle Class
The `Paddle` class creates and controls the paddle. The paddle consists of 11 segments arranged horizontally. The paddle moves left and right based on user input.

#### Key Methods:
- `make_paddle()`: Initializes the paddle with 11 segments.
- `move_right()`: Moves the paddle to the right.
- `move_left()`: Moves the paddle to the left.

### Score Class
The `Score` class manages the scoring and game over conditions. It tracks the player's attempts and score, updating the screen with the current score and high score. If the ball falls off the screen, the player loses an attempt.

#### Key Methods:
- `update_score()`: Updates the score on the screen.
- `refresh_end_game()`: Checks if the game is over and displays the appropriate message.
- `set_high_score()`: Saves the high score to a file if the player achieves a higher score than the previous record.

### Wall Class
The `Wall` class creates the wall of bricks. The bricks are placed in three rows, each with a different color. The bricks are represented as Turtle objects, and they are hidden when broken.

#### Key Methods:
- `make_bricks()`: Creates the bricks with a specified color and position.

## How to Play
1. Use the left and right arrow keys to move the paddle.
2. The ball will bounce off the paddle and break bricks.
3. When all bricks are destroyed or if you run out of attempts, the game ends.
4. The highest score is saved and displayed each time you play.

## Installation

1. Ensure that Python is installed on your computer. You can download it from [here](https://www.python.org/downloads/).
2. This game requires the `turtle` module, which comes pre-installed with Python. No additional installations are required.

## Running the Game

1. Clone or download the repository to your local machine.
2. Run the main game script:

```bash
python game.py
