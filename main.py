from turtle import Turtle, Screen
from random import randint

colours = ['red', 'green', 'yellow', 'orange', 'blue', 'purple']

FULL_HEIGHT = 200

FINISH_LINE_X_COORDINATE = 230

screen = Screen()

turtles = []

for colour in colours:
    turtle = Turtle(shape='turtle')
    turtle.color(colour)
    turtle.penup()
    gradient = FULL_HEIGHT * 2 / len(colours)
    y_coordinate = -1 * FULL_HEIGHT + colours.index(colour) * gradient
    turtle.goto(x=-230, y=y_coordinate)
    turtles.append(turtle)

turtle_won = None

while not turtle_won:
    for turtle in turtles:
        distance = randint(1, 10)
        turtle.forward(distance)
        print(turtle.xcor())
        if turtle.xcor() >= FINISH_LINE_X_COORDINATE:
            turtle_won = turtle

screen.exitonclick()