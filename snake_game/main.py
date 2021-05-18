from turtle import Screen
import time
from game import Game

SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


def start_game():
    game = Game()
    game.set_game_on()
    return game


def is_snake_on_edge(game, screen_width, screen_height):
    xcor = game.snake.xcor()
    ycor = game.snake.ycor()
    edge_up = screen_height/2 - 10
    edge_down = -screen_height/2 - 10
    edge_left = -screen_width/2 - 10
    edge_right = screen_width/2 - 10

    if xcor < edge_left or \
       xcor > edge_right or \
       ycor < edge_down or \
       ycor > edge_up:
        game.set_game_off()
        game.scoreboard.game_over()


game = start_game()


def reset_game():
    game.reset()

def exit_game():
    game.is_game_exited = True

screen.onkey(key="Up", fun=game.snake.up)
screen.onkey(key="Down", fun=game.snake.down)
screen.onkey(key="Left", fun=game.snake.left)
screen.onkey(key="Right", fun=game.snake.right)
screen.onkey(key="c", fun=game.set_game_off)
screen.onkey(key="r", fun=reset_game)
screen.onkey(key="x", fun=exit_game)

is_game_exited = False

while not game.is_game_exited:
    while game.is_game_on:
        screen.update()
        time.sleep(0.1)
        game.snake.move()
        is_snake_on_edge(game, SCREEN_WIDTH, SCREEN_HEIGHT)

        if game.snake.snake_head.distance(game.food) < 20:
            game.food.refresh()
            game.snake.grow_snake()
            game.scoreboard.increase_score()

        for segment in game.snake.segments[2:]:
            if game.snake.snake_head.distance(segment) < 10:
                game.set_game_off()
                game.scoreboard.game_over()

screen.exitonclick()
