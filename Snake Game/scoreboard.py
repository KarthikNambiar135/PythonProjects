from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.show()

    def show(self):
        self.penup()
        self.goto(-300, 270)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align="center", font=("Arial", 30, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.show()
