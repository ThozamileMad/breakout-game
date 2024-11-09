from turtle import Turtle


class Paddle:
    def __init__(self):
        # Initialize the list to store all the paddle segments (blocks).
        self.paddle_segments = []
        # Create the paddle using the make_paddle method, passing in specific x-coordinates for each segment.
        self.make_paddle(100, 80, 60, 40, 20, 0, -20, -40, -60, -80, -100)
        # Set the speed at which the paddle moves (in pixels).
        self.PADDLE_SPEED = 100

    def make_paddle(self, *args):
        """
        Creates a paddle consisting of multiple segments (blocks).
        
        Args:
        - *args: x-coordinates for each of the 11 paddle segments.
        """
        for num in range(11):
            # Create a square turtle object for each segment of the paddle.
            square = Turtle(shape="square")
            # Hide the square initially to position it first.
            square.hideturtle()
            # Lift the pen to prevent drawing lines.
            square.penup()
            # Set the square's color to white.
            square.color("white")
            # Set the x-coordinate based on the args passed and a fixed y-coordinate (-250).
            square.goto(args[num], -250)
            # Show the square once it is correctly positioned.
            square.showturtle()
            # Add the square to the paddle segments list.
            self.paddle_segments.append(square)

    def move_right(self):
        """
        Moves the paddle to the right by moving each segment forward.
        Ensures the paddle doesn't exceed the right boundary (x-coordinate < 260).
        """
        # Check if the rightmost segment is within the allowed x-coordinate.
        if self.paddle_segments[-1].xcor() < 260:
            # Move each segment of the paddle to the right.
            for square in self.paddle_segments:
                square.forward(self.PADDLE_SPEED)

    def move_left(self):
        """
        Moves the paddle to the left by moving each segment backward.
        Ensures the paddle doesn't exceed the left boundary (x-coordinate > -260).
        """
        # Check if the leftmost segment is within the allowed x-coordinate.
        if self.paddle_segments[0].xcor() > -260:
            # Move each segment of the paddle to the left.
            for square in self.paddle_segments:
                square.backward(self.PADDLE_SPEED)
