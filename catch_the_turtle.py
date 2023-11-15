import turtle
import random

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")


def make_score():
    make_score=turtle.Turtle()
    make_score.penup()
    make_score.setpos(0, 250)
    make_score.write("Score: 0", False, "center", ["normal", 30])


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
def make_turtle():
    make_turtle=turtle.Turtle()
    make_turtle.shape("turtle")
    make_turtle.turtlesize(3)
    make_turtle.penup()




def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)



make_turtle()
setup_turtles()
make_score()
turtle.mainloop()