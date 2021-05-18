from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 270)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
