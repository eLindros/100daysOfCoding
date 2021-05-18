from turtle import Turtle


HEIGHT = 100
WIDTH = 20
X_POS = 350
Y_POS = 0
COLOR = "white"



class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.penup()
        self.color(COLOR)
        self.goto(X_POS, Y_POS)
        self.setheading(90)
        self.showturtle()

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
