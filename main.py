from turtle import Screen
import time
from snake import Snake
from game import Game
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

def start_game():
  snake = Snake()
  game = Game()
  game.set_game_on()
  return (snake, game)



def is_snake_on_edge(snake, game, screen_width, screen_height):
  xcor = snake.xcor()
  ycor = snake.ycor()
  edge_up = screen_height/2
  edge_down = -screen_height/2
  edge_left = -screen_width/2
  edge_right = screen_width/2

  if xcor < edge_left or \
     xcor > edge_right or \
     ycor < edge_down or \
     ycor > edge_up:
    game.set_game_off()


new_game = start_game()

snake = new_game[0]
game = new_game[1]
food = Food()
scoreboard = Scoreboard()

def reset_game():
  snake.clear()
  food.refresh()
  scoreboard.reset()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="c", fun=game.set_game_off)
screen.onkey(key="r", fun=reset_game)


while game.is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    is_snake_on_edge(snake, game, SCREEN_WIDTH, SCREEN_HEIGHT)

    if snake.snake_head.distance(food) < 20:
      food.refresh()
      snake.grow_snake()
      scoreboard.increase_score()


screen.exitonclick()
