from turtle import Screen
from pong.paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Pong"
BG_COLOR = "black"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(TITLE)
screen.tracer(0)
screen.listen()

paddle = Paddle()

screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)
screen.onkey(key="c", fun=screen.bye)

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()
