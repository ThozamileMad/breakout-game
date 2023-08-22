from time import sleep
from turtle import Turtle


class Score:
    def __init__(self, ball):
        self.ball_obj = ball
        self.ball = self.ball_obj.ball
        self.attempts = 3
        self.ball_gone = False
        self.game_over = False

    def update_score(self, screen, score):
        try:
            with open("high_score.txt") as file:
                high_score = file.read()
                screen.title(f"Highest Score: {high_score}     Current Score: {score}     Attempts: {self.attempts}")
        except FileNotFoundError:
            screen.title(f"Highest Score: 0     Current Score: {score}     Attempts: {self.attempts}")

    def refresh_end_game(self, score):
        if self.ball_obj.ball.ycor() < -280 and self.attempts != 0:
            self.ball_gone = True
            if self.ball_gone:
                sleep(2)
                self.ball.hideturtle()
                self.ball.goto(0, 0)
                self.ball.setheading(-90)
                self.ball_obj.BALL_SPEED = 0.5
                self.ball.showturtle()
                self.attempts -= 1
                self.ball_gone = False
        elif self.attempts == 0 or score == 288:
            game_over_text = Turtle()
            game_over_text.hideturtle()
            game_over_text.penup()
            game_over_text.goto(-165, 0)
            game_over_text.color("white")
            game_over_text.write("Game Over", font=("Bold", 50, ""))
            game_over_text.showturtle()
            self.game_over = True

        return self.game_over

    def set_high_score(self):
        is_higher = False
        try:
            with open("high_score.txt") as file:
                high_score = int(file.read())
                if high_score < self.ball_obj.hit_points:
                    is_higher = True

            if is_higher:
                with open("high_score.txt", "w") as file:
                    file.write(f"{self.ball_obj.hit_points}")
        except FileNotFoundError:
            with open("high_score.txt", "w") as file:
                file.write(f"{self.ball_obj.hit_points}")
