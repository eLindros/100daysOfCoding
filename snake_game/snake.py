from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_segment(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)

    
    def create_snake(self):
        for position in STARTING_POSITIONS:
          self.create_segment(position)
    
    def grow_snake(self):
      snake_tail = self.segments[-1]
      tail_position = snake_tail.position()
      self.create_segment(tail_position)

    def clear(self):
      for segment in self.segments:
        segment.reset()
      
      self.__init__()

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            prev_num = seg_num - 1
            new_x = self.segments[prev_num].xcor()
            new_y = self.segments[prev_num].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.snake_head.forward(MOVING_DISTANCE)

    def xcor(self):
      return self.snake_head.xcor()
        
    def ycor(self):
      return self.snake_head.ycor()

    def up(self):
        if self.snake_head.heading() != DOWN:
          self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
          self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
          self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
          self.snake_head.setheading(RIGHT)
