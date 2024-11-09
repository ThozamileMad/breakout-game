from time import sleep
from turtle import Turtle


class Score:
    def __init__(self, ball):
        """
        Initializes the score tracking system.

        Args:
        - ball: The ball object whose hit points are tracked for scoring.
        """
        # Assign the ball object passed as an argument to the ball_obj attribute.
        self.ball_obj = ball
        # Extract the ball turtle from the ball object.
        self.ball = self.ball_obj.ball
        # Set the initial number of attempts the player has (starting with 3).
        self.attempts = 3
        # A flag indicating if the ball has gone below the screen.
        self.ball_gone = False
        # A flag indicating if the game is over.
        self.game_over = False

    def update_score(self, screen, score):
        """
        Updates the score displayed on the screen.

        Args:
        - screen: The turtle screen object where the score is displayed.
        - score: The current score to be displayed.
        """
        try:
            # Try to read the high score from a file.
            with open("high_score.txt") as file:
                high_score = file.read()
                # Update the screen title to show the high score, current score, and remaining attempts.
                screen.title(f"Highest Score: {high_score}     Current Score: {score}     Attempts: {self.attempts}")
        except FileNotFoundError:
            # If the high score file does not exist, default the high score to 0.
            screen.title(f"Highest Score: 0     Current Score: {score}     Attempts: {self.attempts}")

    def refresh_end_game(self, score):
        """
        Checks if the game should end, either because the player has lost all attempts or completed the game.

        Args:
        - score: The current score to check if the game has ended.

        Returns:
        - A boolean indicating whether the game is over.
        """
        # Check if the ball has gone below the bottom of the screen and the player still has attempts.
        if self.ball_obj.ball.ycor() < -280 and self.attempts != 0:
            self.ball_gone = True
            if self.ball_gone:
                # Pause for 2 seconds before respawning the ball.
                sleep(2)
                self.ball.hideturtle()
                self.ball.goto(0, 0)
                self.ball.setheading(-90)  # Reset ball's direction.
                self.ball_obj.BALL_SPEED = 0.5  # Reset the ball's speed.
                self.ball.showturtle()  # Show the ball again.
                self.attempts -= 1  # Decrease the number of attempts.
                self.ball_gone = False
        # End the game if attempts are zero or if the score reaches 288 (winning condition).
        elif self.attempts == 0 or score == 288:
            game_over_text = Turtle()
            game_over_text.hideturtle()
            game_over_text.penup()
            game_over_text.goto(-165, 0)
            game_over_text.color("white")
            game_over_text.write("Game Over", font=("Bold", 50, ""))  # Display game over message.
            game_over_text.showturtle()
            self.game_over = True

        return self.game_over

    def set_high_score(self):
        """
        Updates the high score if the current score is higher.

        Checks if the current score exceeds the previously stored high score and updates it.
        """
        is_higher = False
        try:
            # Read the existing high score from the file.
            with open("high_score.txt") as file:
                high_score = int(file.read())
                # If the current score is higher than the high score, set the flag to True.
                if high_score < self.ball_obj.hit_points:
                    is_higher = True

            if is_higher:
                # If the current score is higher, update the high score in the file.
                with open("high_score.txt", "w") as file:
                    file.write(f"{self.ball_obj.hit_points}")
        except FileNotFoundError:
            # If no high score file exists, create one and write the current score as the high score.
            with open("high_score.txt", "w") as file:
                file.write(f"{self.ball_obj.hit_points}")
