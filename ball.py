import random
from turtle import Turtle


class Ball:
    def __init__(self):
        self.SPEED_LIST = [1, 1.1, 1.2, 1.3, 1.4, 1.5]
        self.BALL_SPEED = 0.5
        self.ball = self.make_ball()
        self.hit_points = 0

    def make_ball(self):
        circle = Turtle(shape="circle")
        circle.color("white")
        circle.setheading(-90)
        circle.penup()

        return circle

    def paddle_impact(self, range_nums, paddle_segments, angle):
        for num in range(range_nums[0], range_nums[1]):
            if paddle_segments[num].distance(self.ball) < 20:
                self.ball.setheading(angle)
                self.BALL_SPEED = random.choice(self.SPEED_LIST)

    def move_and_hit_boundary(self, condition, rand_num):
        if condition:
            random_number = rand_num
            self.ball.setheading(random_number)
            self.BALL_SPEED = random.choice(self.SPEED_LIST)
            self.ball.forward(self.BALL_SPEED)
        else:
            self.ball.forward(self.BALL_SPEED)

    def break_wall(self, wall_segments, condition, rand_num):
        for num in range(len(wall_segments)):
            brick = wall_segments[num]
            if condition and brick.distance(self.ball) < 40:
                random_number = rand_num
                self.ball.setheading(random_number)
                self.BALL_SPEED = random.choice(self.SPEED_LIST)
                self.ball.forward(self.BALL_SPEED)
                brick.hideturtle()
                brick.goto(10000, 10000)
                if brick in wall_segments[:12]:
                    self.hit_points += 12
                elif brick in wall_segments[12:24]:
                    self.hit_points += 8
                else:
                    self.hit_points += 4



