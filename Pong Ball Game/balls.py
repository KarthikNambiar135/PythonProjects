from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.01
        self.create()

    def create(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
       x = self.xcor() + self.x_move
       y = self.ycor() + self.y_move
       self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.83

    def recreate(self):
        self.home()
        self.move_speed = 0.01
        self.bounce_x()
