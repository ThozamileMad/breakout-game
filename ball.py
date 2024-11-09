import random
from turtle import Turtle


class Ball:
    def __init__(self):
        # Define possible speeds for the ball in a list.
        self.SPEED_LIST = [1, 1.1, 1.2, 1.3, 1.4, 1.5]
        # Initial speed of the ball.
        self.BALL_SPEED = 0.5
        # Create the ball using the make_ball function.
        self.ball = self.make_ball()
        # Initialize hit points to track the player's score.
        self.hit_points = 0

    def make_ball(self):
        # Create a circle turtle object that will act as the ball.
        circle = Turtle(shape="circle")
        # Set the ball's color to white.
        circle.color("white")
        # Set the initial heading of the ball to -90 (downwards).
        circle.setheading(-90)
        # Prevent the ball from drawing lines by lifting the pen.
        circle.penup()

        return circle

    def paddle_impact(self, range_nums, paddle_segments, angle):
        """
        Handles the impact between the ball and the paddle.
        
        Args:
        - range_nums: The range of paddle segments to check for collision.
        - paddle_segments: The list of paddle segments.
        - angle: The new angle to set the ball to after impact.
        """
        for num in range(range_nums[0], range_nums[1]):
            # Check if the ball is close enough to a paddle segment (distance < 20).
            if paddle_segments[num].distance(self.ball) < 20:
                # If collision occurs, set the ball's heading to the given angle.
                self.ball.setheading(angle)
                # Change the ball's speed randomly.
                self.BALL_SPEED = random.choice(self.SPEED_LIST)

    def move_and_hit_boundary(self, condition, rand_num):
        """
        Moves the ball and checks if it hits any boundary conditions (e.g., walls).
        
        Args:
        - condition: Condition to check if the boundary is hit.
        - rand_num: Random angle to change the ball's heading when boundary is hit.
        """
        if condition:
            # If the condition is true, change the ball's heading and speed randomly.
            random_number = rand_num
            self.ball.setheading(random_number)
            self.BALL_SPEED = random.choice(self.SPEED_LIST)
            # Move the ball forward with the new speed.
            self.ball.forward(self.BALL_SPEED)
        else:
            # If no boundary is hit, move the ball forward with the current speed.
            self.ball.forward(self.BALL_SPEED)

    def break_wall(self, wall_segments, condition, rand_num):
        """
        Handles the impact of the ball with the wall segments (bricks).
        
        Args:
        - wall_segments: The list of wall segments (bricks).
        - condition: Whether the ball hits a brick.
        - rand_num: Random angle to set the ball to after wall impact.
        """
        for num in range(len(wall_segments)):
            brick = wall_segments[num]
            # Check if the ball collides with the brick (distance < 40).
            if condition and brick.distance(self.ball) < 40:
                # If collision occurs, change the ball's heading and speed randomly.
                random_number = rand_num
                self.ball.setheading(random_number)
                self.BALL_SPEED = random.choice(self.SPEED_LIST)
                # Move the ball forward after the hit.
                self.ball.forward(self.BALL_SPEED)
                # Hide the brick after it is hit.
                brick.hideturtle()
                # Move the brick off-screen to prevent it from being visible.
                brick.goto(10000, 10000)
                # Increment the hit points based on the brick's position in the wall.
                if brick in wall_segments[:12]:
                    self.hit_points += 12  # Add 12 points for bricks in the first group.
                elif brick in wall_segments[12:24]:
                    self.hit_points += 8   # Add 8 points for bricks in the second group.
                else:
                    self.hit_points += 4   # Add 4 points for bricks in the last group.
