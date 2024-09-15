import random
import colorgram
import turtle as t

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(280)
tim.pendown()
tim.setheading(0)
colors = colorgram.extract("image.jpg", 30)
c = []
for color in colors:
    color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    c.append(color_tuple)
for i in range(1, 101):
    tim.dot(20, random.choice(c))
    tim.penup()
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()
