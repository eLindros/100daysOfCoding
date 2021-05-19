from snake_game.snake import Snake
from snake_game.scoreboard import Scoreboard
from snake_game.food import Food
from turtle import Screen
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
BG_COLOR = "black"
TITLE = "Snake Game"


class Game:

    def __init__(self):
        self.init_screen()
        self.is_game_on = True
        self.is_game_exited = True
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.define_keys()

    def init_screen(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)

    def set_game_on(self):
        self.is_game_on = True

    def set_game_off(self):
        self.is_game_on = False

    def reset(self):
        self.snake.reset()
        self.food.reset()
        self.scoreboard.reset()
        self.screen.clearscreen()
        self.__init__()
        self.start_game()

    def define_keys(self):
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.snake.up)
        self.screen.onkey(key="Down", fun=self.snake.down)
        self.screen.onkey(key="Left", fun=self.snake.left)
        self.screen.onkey(key="Right", fun=self.snake.right)
        self.screen.onkey(key="c", fun=self.set_game_off)
        self.screen.onkey(key="r", fun=self.reset)
        self.screen.onkey(key="x", fun=self.exit_game)
        self.screen.onkey(key="s", fun=self.start_game)

    def exit_game(self):
        self.screen.bye()

    def is_snake_on_edge(self):
        xcor = self.snake.xcor()
        ycor = self.snake.ycor()
        edge_up = SCREEN_HEIGHT/2 - 10
        edge_down = -SCREEN_HEIGHT/2 - 10
        edge_left = -SCREEN_WIDTH/2 - 10
        edge_right = SCREEN_WIDTH/2 - 10

        if xcor < edge_left or \
                xcor > edge_right or \
                ycor < edge_down or \
                ycor > edge_up:
            self.set_game_off()
            self.scoreboard.game_over()

    def start_game(self):
        self.screen.tracer(0)
        while self.is_game_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            self.is_snake_on_edge()

            if self.snake.snake_head.distance(self.food) < 20:
                self.food.refresh()
                self.snake.grow_snake()
                self.scoreboard.increase_score()

            for segment in self.snake.segments[2:]:
                if self.snake.snake_head.distance(segment) < 10:
                    self.set_game_off()
                    self.scoreboard.game_over()
