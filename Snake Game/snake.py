import turtle as t
positions = [(0, 0), (-20, 0), (-40, 0)]
SCREEN = t.Screen()
class Snake:
    def __init__(self):
        self.snake = []
        self.create()
        self.head = self.snake[0]

    def create(self):
        for i in positions:
            self.add_segment(i)

    def add_segment(self, i):
        tim = t.Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.snake.append(tim)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        SCREEN.listen()
        SCREEN.onkey(self.up, "Up")
        SCREEN.onkey(self.down, "Down")
        SCREEN.onkey(self.left, "Left")
        SCREEN.onkey(self.right, "Right")
        for segments in range(len(self.snake) - 1, 0, -1):
            last_x = self.snake[segments - 1].xcor()
            last_y = self.snake[segments - 1].ycor()
            self.snake[segments].goto(last_x, last_y)
        self.head.forward(20)
