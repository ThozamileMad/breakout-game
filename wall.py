from turtle import Turtle


class Wall:
    def __init__(self):
        self.bricks = []
        self.make_bricks("red", 190)
        self.make_bricks("blue", 145)
        self.make_bricks("yellow", 100)

    def make_bricks(self, color, ycor):
        xcor = -460
        for num in range(12):
            brick = Turtle()
            brick.hideturtle()
            brick.penup()
            brick.shapesize(stretch_wid=2, stretch_len=4)
            brick.color(color)
            brick.shape("square")
            brick.goto(xcor, ycor)
            brick.showturtle()
            xcor += 85
            self.bricks.append(brick)
