import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

on = True
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 270 or snake.head.ycor() < -295:
        on = False
        score.game_over()
    if snake.head.distance(food) < 15:
        food.new_location()
        score.increase()
        snake.extend()
    for segment in snake.snake[1:len(snake.snake)]:
        if snake.head.distance(segment) < 10:
            on = False
            score.game_over()

screen.exitonclick()
