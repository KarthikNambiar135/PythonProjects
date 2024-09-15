import time
import turtle as t
from paddles import Paddle
from balls import Ball
from scoreboard import Score

screen = t.Screen()
tim = t.Turtle()
tim.hideturtle()
def mid_boundary():
    tim.color("white")
    tim.pensize(10)
    tim.penup()
    tim.goto(0, 390)
    tim.pendown()
    tim.goto(0, -390)
mid_boundary()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

on = True
while on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if (ball.distance(paddle1) < 50 and ball.xcor() > 340) or (ball.distance(paddle2) < 50 and ball.xcor() < -340):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.recreate()
        score.increase2()
        if score.score2 == 10:
            on = False
            tim.color("green")
            tim.penup()
            tim.home()
            tim.write("LEFT WON!", align="center", font=("Arial", 30, "normal"))
    if ball.xcor() < -380:
        ball.recreate()
        score.increase1()
        if score.score1 == 10:
            on = False
            tim.color("green")
            tim.penup()
            tim.home()
            tim.write("RIGHT WON!", align="center", font=("Arial", 30, "normal"))

screen.exitonclick()
