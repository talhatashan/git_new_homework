import turtle
from random import randint

points = turtle.Turtle()
points.hideturtle()
points.color('black')
points.penup()
points.goto(-280, 250)
points.write(f"Points: {points}")
def show_score():
    player.clear()
    player.goto(randint(-280, 0), randint(0, 280))
    player.write(f"Score: {score}")
    player.penup()



def add_score(x, y):
    global score
    score += 1
    show_score()
    turtle.update()


score = 0
turtle.tracer(0)
player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.turtlesize(3)
player.onclick(add_score)
show_score()
turtle.update()
turtle.mainloop()