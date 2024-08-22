from turtle import Turtle, Screen


def create_turtles(x, y, color, shape="turtle"):
    t = Turtle(shape)
    t.color(color)
    t.penup()
    t.goto(x, y)


create_turtles(-300, -120, "green")
create_turtles(-300, -70, "yellow")
create_turtles(-300, -20, "purple")
create_turtles(-300, 30, "orange")
create_turtles(-300, 80, "red")
create_turtles(-300, 130, "blue")

screen = Screen()
user_guess = screen.textinput(title="Make your bet!", prompt="Which turtle is going to win? Enter color name: ")
colors = ["red", "blue", "green", "orange", "purple", "yellow"]

screen.exitonclick()
