from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="c", fun=lambda: screen.bye)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
