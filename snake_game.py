from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(-40,0), (-20,0), (0,0)]

snake = []

for position in starting_positions:
  snake_part = Turtle(shape="square")
  snake_part.color("white")
  snake_part.penup()
  snake_part.goto(position)
  snake.append(snake_part)

is_game_on = True

while is_game_on:
  screen.update()
  time.sleep(0.1)
  for snake_part in snake:
    snake_part.forward(20)


screen.exitonclick()