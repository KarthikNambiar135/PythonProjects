import turtle as t

tim = t.Turtle()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def pen_up():
    tim.penup()
def pen_down():
    tim.pendown()
def clear():
    tim.clear()
def home():
    tim.penup()
    tim.home()
    tim.pendown()
screen = t.Screen()
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="p", fun=pen_up)
screen.onkey(key="l", fun=pen_down)
screen.onkey(key="space", fun=clear)
screen.onkey(key="h", fun=home)
screen.exitonclick()
