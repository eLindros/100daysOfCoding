from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
       
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(position)
            self.segments.append(snake_part)

        self.snake_head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            prev_num = seg_num - 1
            new_x = self.segments[prev_num].xcor()
            new_y = self.segments[prev_num].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.snake_head.forward(MOVING_DISTANCE)

    def up(self):
        self.snake_head.left(90)

    def down(self):
        self.snake_head.right(90)
