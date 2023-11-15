import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("gray")
drawing_board.title("Talha Turtle")
turtle_instance= turtle.Turtle()


def dondurma():
    turtle_instance.left(10)

def ileri():
    turtle_instance.forward(100)
def ekran_silme():
    turtle_instance.clear()

def eve_don():
    turtle_instance.home()

def kalem_kaldir():
    turtle_instance.penup()

def kalem_indir():
    turtle_instance.pendown()

drawing_board.listen()

drawing_board.onkey(fun=dondurma, key="space")
drawing_board.onkey(fun=ileri, key="a")
drawing_board.onkey(fun=eve_don, key="e")
drawing_board.onkey(fun=ekran_silme, key="c")
drawing_board.onkey(fun=kalem_kaldir, key="k")
drawing_board.onkey(fun=kalem_indir, key="i")

turtle.mainloop()