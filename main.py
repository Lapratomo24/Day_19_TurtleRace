from turtle import Turtle, Screen
import random

racing_turtles = []
race_is_on = False


def create_turtles(x, y, color, shape="turtle"):
    t = Turtle(shape)
    t.color(color)
    t.penup()
    t.goto(x, y)
    racing_turtles.append(t)


create_turtles(-300, -120, "green")
create_turtles(-300, -70, "yellow")
create_turtles(-300, -20, "purple")
create_turtles(-300, 30, "orange")
create_turtles(-300, 80, "red")
create_turtles(-300, 130, "blue")

screen = Screen()
user_guess = screen.textinput(title="Make your bet!", prompt="Which turtle is going to win? Enter color name: ")
colors = ["red", "blue", "green", "orange", "purple", "yellow"]

if user_guess:
    race_is_on = True

while race_is_on:
    for turtle in racing_turtles:
        race_gaps = random.randint(0, 10)
        turtle.forward(race_gaps)

        if turtle.xcor() > 320:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print("You won!")
            else:
                print("You lost!")

screen.exitonclick()
