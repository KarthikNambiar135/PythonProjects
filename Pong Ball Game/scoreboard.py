from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.show()


    def show(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.score2, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score1, align="center", font=("Arial", 80, "normal"))

    def increase1(self):
        self.score1 += 1
        self.clear()
        self.show()

    def increase2(self):
        self.score2 += 1
        self.clear()
        self.show()
