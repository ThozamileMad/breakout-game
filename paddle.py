from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle_segments = []
        self.make_paddle(100, 80, 60, 40, 20, 0, -20, -40, -60, -80, -100)
        self.PADDLE_SPEED = 100

    def make_paddle(self, *args):
        for num in range(11):
            square = Turtle(shape="square")
            square.hideturtle()
            square.penup()
            square.color("white")
            square.goto(args[num], -250)
            square.showturtle()
            self.paddle_segments.append(square)

    def move_right(self):
        if self.paddle_segments[-1].xcor() < 260:
            for square in self.paddle_segments:
                square.forward(self.PADDLE_SPEED)

    def move_left(self):
        if self.paddle_segments[0].xcor() > -260:
            for square in self.paddle_segments:
                square.backward(self.PADDLE_SPEED)

