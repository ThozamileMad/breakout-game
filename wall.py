from turtle import Turtle


class Wall:
    def __init__(self):
        """
        Initializes the wall by creating three rows of bricks with different colors.
        """
        self.bricks = []  # A list to store all the brick objects.
        # Creates three rows of bricks with different colors at different y coordinates.
        self.make_bricks("red", 190)    # First row with red bricks at y = 190
        self.make_bricks("blue", 145)   # Second row with blue bricks at y = 145
        self.make_bricks("yellow", 100) # Third row with yellow bricks at y = 100

    def make_bricks(self, color, ycor):
        """
        Creates a row of bricks of a specified color at a given y coordinate.
        
        Args:
        - color (str): The color of the bricks.
        - ycor (int): The y-coordinate where the bricks will be placed.
        """
        xcor = -460  # The starting x-coordinate for the first brick in the row.
        for num in range(12):  # Loop to create 12 bricks in each row.
            brick = Turtle()   # Create a new Turtle object for the brick.
            brick.hideturtle()  # Initially hide the brick (it will be shown later).
            brick.penup()      # Lift the pen so it doesn't draw lines.
            brick.shapesize(stretch_wid=2, stretch_len=4)  # Stretch the square shape to make it rectangular.
            brick.color(color)  # Set the color of the brick.
            brick.shape("square")  # Use the square shape for the brick.
            brick.goto(xcor, ycor)  # Position the brick at the given x and y coordinates.
            brick.showturtle()  # Show the brick after positioning.
            xcor += 85  # Increment the x-coordinate for the next brick in the row.
            self.bricks.append(brick)  # Add the brick to the list of bricks.
