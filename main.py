from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from wall import Wall
from scoreboard import Score
import random


def make_turtle_text(xcor, ycor, text):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(xcor, ycor)
    turtle.color("white")
    turtle.write(text, font=("Bold", 25, ""))
    return turtle


def instructions():
    instruction_text = make_turtle_text(-405, 0, "How to move paddle: 'l' to move right and 'a' to move left.")

    countdown = 5
    countdown_text = make_turtle_text(-405, -80, f"Game Starting In: {countdown}.")
    for num in range(countdown):
        countdown_text.write(f"Game Starting In: {countdown}.", font=("Bold", 25, ""))
        countdown -= 1
        sleep(1)
        countdown_text.clear()

    countdown_text.reset()
    instruction_text.reset()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Wall Breaker!!!")
instructions()
screen.tracer(0, 0)

paddle = Paddle()

screen.onkey(paddle.move_right, "l")
screen.onkey(paddle.move_left, "a")
screen.listen()

ball = Ball()
angles = ([num for num in range(120, 141)], [num for num in range(80, 101)], [num for num in range(40, 61)],
          [num for num in range(220, 241)], [num for num in range(320, 341)], [num for num in range(260, 281)])

wall = Wall()

scoreboard = Score(ball)

play = True

while play:
    sleep(0.01)
    screen.update()

    scoreboard.update_score(screen, ball.hit_points)
    if scoreboard.refresh_end_game(ball.hit_points):
        play = False

    ball.paddle_impact([0, 5], paddle.paddle_segments[::-1], random.choice(angles[0]))
    ball.paddle_impact([5, 6], paddle.paddle_segments, random.choice(angles[1]))
    ball.paddle_impact([0, 5], paddle.paddle_segments, random.choice(angles[2]))

    ball_heading = ball.ball.heading()

    # Left Boundary
    ball.move_and_hit_boundary(ball_heading in angles[0] and ball.ball.xcor() < -490, random.choice(angles[2]))
    ball.move_and_hit_boundary(ball_heading in angles[3] and ball.ball.xcor() < -490, random.choice(angles[4]))

    # Top Boundary
    ball.move_and_hit_boundary(ball_heading in angles[0] and ball.ball.ycor() > 280, random.choice(angles[3]))
    ball.move_and_hit_boundary(ball_heading in angles[1] and ball.ball.ycor() > 280, random.choice(angles[5]))
    ball.move_and_hit_boundary(ball_heading in angles[2] and ball.ball.ycor() > 280, random.choice(angles[4]))

    # Right Boundary
    ball.move_and_hit_boundary(ball_heading in angles[2] and ball.ball.xcor() > 490, random.choice(angles[0]))
    ball.move_and_hit_boundary(ball_heading in angles[4] and ball.ball.xcor() > 490, random.choice(angles[3]))

    # Wall Breaker Code
    # Top, Bottom, Left, Right Impact
    index_nums = [[0, 3], [1, 5], [2, 4], [3, 0], [5, 1], [4, 2]]
    for index_lst in index_nums:
        ball.break_wall(wall.bricks, ball_heading in angles[index_lst[0]], random.choice(angles[index_lst[1]]))

scoreboard.set_high_score()

screen.exitonclick()
