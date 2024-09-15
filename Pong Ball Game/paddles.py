from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.create(positions)

    def create(self, positions):
            self.shape("square")
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()
            self.goto(positions)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
