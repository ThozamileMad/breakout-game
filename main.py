# Import necessary modules for the game
from turtle import Turtle, Screen  # For drawing on the screen using turtle graphics
from paddle import Paddle  # Import the Paddle class for controlling the player's paddle
from ball import Ball  # Import the Ball class for controlling the ball
from time import sleep  # For adding pauses during gameplay
from wall import Wall  # Import the Wall class for handling the game wall and bricks
from scoreboard import Score  # Import the Score class for handling the score
import random  # For generating random values

# Function to create text using turtle graphics
def make_turtle_text(xcor, ycor, text):
    turtle = Turtle()
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.penup()  # Lift the pen so it doesn't draw lines
    turtle.goto(xcor, ycor)  # Move turtle to the specified coordinates
    turtle.color("white")  # Set text color to white
    turtle.write(text, font=("Bold", 25, ""))  # Write the provided text with specified font
    return turtle  # Return the turtle object

# Function to display game instructions and countdown before the game starts
def instructions():
    # Create instruction text using the make_turtle_text function
    instruction_text = make_turtle_text(-405, 0, "How to move paddle: 'l' to move right and 'a' to move left.")

    countdown = 5  # Set the countdown starting value
    # Display countdown text
    countdown_text = make_turtle_text(-405, -80, f"Game Starting In: {countdown}.")
    for num in range(countdown):
        countdown_text.write(f"Game Starting In: {countdown}.", font=("Bold", 25, ""))
        countdown -= 1  # Decrease countdown
        sleep(1)  # Pause for 1 second
        countdown_text.clear()  # Clear the countdown text

    countdown_text.reset()  # Reset the countdown turtle
    instruction_text.reset()  # Reset the instruction turtle

# Set up the game screen
screen = Screen()
screen.bgcolor("black")  # Set background color to black
screen.setup(width=1000, height=600)  # Set screen dimensions
screen.title("Wall Breaker!!!")  # Set the window title
instructions()  # Call instructions to display how to play and countdown
screen.tracer(0, 0)  # Turn off automatic screen updates for better control

# Create paddle and set up keybindings for moving the paddle
paddle = Paddle()
screen.onkey(paddle.move_right, "l")  # Press 'l' to move the paddle right
screen.onkey(paddle.move_left, "a")  # Press 'a' to move the paddle left
screen.listen()  # Start listening for key presses

# Create the ball object
ball = Ball()

# Define ball bounce angles for randomizing direction after collisions
angles = ([num for num in range(120, 141)], [num for num in range(80, 101)], [num for num in range(40, 61)],
          [num for num in range(220, 241)], [num for num in range(320, 341)], [num for num in range(260, 281)])

# Create wall with bricks
wall = Wall()

# Create scoreboard for displaying points and handling scoring
scoreboard = Score(ball)

# Game loop flag
play = True

# Main game loop
while play:
    sleep(0.01)  # Short sleep to control game speed
    screen.update()  # Update the screen

    # Update the score based on the ball's hit points
    scoreboard.update_score(screen, ball.hit_points)
    
    # Check if game should end (if hit points are below a certain threshold)
    if scoreboard.refresh_end_game(ball.hit_points):
        play = False

    # Check for collisions with the paddle and walls, and make the ball bounce accordingly
    ball.paddle_impact([0, 5], paddle.paddle_segments[::-1], random.choice(angles[0]))
    ball.paddle_impact([5, 6], paddle.paddle_segments, random.choice(angles[1]))
    ball.paddle_impact([0, 5], paddle.paddle_segments, random.choice(angles[2]))

    ball_heading = ball.ball.heading()  # Get the current heading of the ball

    # Collision handling with boundaries (Left, Top, Right boundaries)
    ball.move_and_hit_boundary(ball_heading in angles[0] and ball.ball.xcor() < -490, random.choice(angles[2]))
    ball.move_and_hit_boundary(ball_heading in angles[3] and ball.ball.xcor() < -490, random.choice(angles[4]))
    ball.move_and_hit_boundary(ball_heading in angles[0] and ball.ball.ycor() > 280, random.choice(angles[3]))
    ball.move_and_hit_boundary(ball_heading in angles[1] and ball.ball.ycor() > 280, random.choice(angles[5]))
    ball.move_and_hit_boundary(ball_heading in angles[2] and ball.ball.ycor() > 280, random.choice(angles[4]))
    ball.move_and_hit_boundary(ball_heading in angles[2] and ball.ball.xcor() > 490, random.choice(angles[0]))
    ball.move_and_hit_boundary(ball_heading in angles[4] and ball.ball.xcor() > 490, random.choice(angles[3]))

    # Wall brick collision detection
    index_nums = [[0, 3], [1, 5], [2, 4], [3, 0], [5, 1], [4, 2]]
    for index_lst in index_nums:
        # Check for brick collisions in different directions and handle bounce
        ball.break_wall(wall.bricks, ball_heading in angles[index_lst[0]], random.choice(angles[index_lst[1]]))

# Save high score after the game ends
scoreboard.set_high_score()

# Exit the game when the screen is clicked
screen.exitonclick()
