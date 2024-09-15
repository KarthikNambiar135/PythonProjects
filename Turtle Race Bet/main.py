import turtle as t
import random

colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
screen = t.Screen()
screen.setup(width=800,height=500)
on = False
user_bet = screen.textinput(title="Place your Bet",prompt="Which turtle will win the race? "
                                               "Enter the colour(from rainbow): ")
tom = t.Turtle()
tom.hideturtle()
tom.penup()
tom.goto(x=360, y=200)
tom.right(90)
tom.pendown()
tom.forward(410)
tom.penup()
tom.goto(x=-300, y=0)
turtles = []
for i in range(0, 7):
    tim = t.Turtle(shape="turtle")
    tim.color(colours[i])
    tim.penup()
    tim.goto(x=-300, y=-200 + i*66)
    turtles.append(tim)
if user_bet:
    on = True
while on:
    for j in turtles:
        if j.xcor() > 360:
            winner = j.pencolor()
            on = False
            if winner == user_bet:
                print(f"You WON! The {winner} turtle has finished the race first.")
                tom.write(f"You WON!\nThe {winner} turtle has finished the race first."
                          f"\nClick to Exit.",
                        font=("Arial", 26, "normal"), align="left")
            else:
                print(f"You LOST! The {winner} turtle finished the race first.")
                tom.write(f"You LOST!\nThe {winner} turtle finished the race first."
                          f"\nClick to Exit.",
                        font=("Arial", 26, "normal"), align="left")
        distance = random.randint(0,10)
        j.forward(distance)

screen.exitonclick()
