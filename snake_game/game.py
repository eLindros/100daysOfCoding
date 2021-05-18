from snake_game.snake import Snake
from snake_game.scoreboard import Scoreboard
from snake_game.food import Food

class Game:
  
  def __init__(self):
    self.is_game_on = False
    self.is_game_exited = False
    self.snake = Snake()
    self.food = Food()
    self.scoreboard = Scoreboard()

  def set_game_on(self):
    self.is_game_on = True

  def set_game_off(self):
    self.is_game_on = False

  def reset(self):
    self.snake.clear()
    self.food.refresh()
    self.scoreboard.reset()
    self.snake = Snake()
    self.scoreboard = Scoreboard()
