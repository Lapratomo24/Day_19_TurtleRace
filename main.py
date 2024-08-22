from turtle import Turtle, Screen
import random

screen = Screen()
user_guess = screen.textinput(title="Make your bet!", prompt="Which turtle is going to win? Enter color name: ")
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
positions = [-120, -70, -20, 30, 80, 130]
racing_turtles = []
race_is_on = False

for turtle in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle])
    t.penup()
    t.goto(x=-300, y=positions[turtle])
    racing_turtles.append(t)


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
