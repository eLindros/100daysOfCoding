from turtle import Turtle

POSITION_Y = 270
ALIGNMENT = "center"
FONT = ("Courier", "24", "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.goto(0,POSITION_Y)
    self.penup()
    self.score = 0
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.update_score()
  
