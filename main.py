from turtle import Turtle, Screen
import time
from snake import Snake

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)

snake = Snake()

#Moves


game_screen.listen()
game_screen.onkey(key="Up", fun=snake.move_up)
game_screen.onkey(key="Down", fun=snake.move_down)
game_screen.onkey(key="Right", fun=snake.move_right)
game_screen.onkey(key="Left", fun= snake.move_left)

in_the_Game = True

while in_the_Game:
    distance = 10
    game_screen.update()
    time.sleep(0.1)
#Each segment will move to the position of the segment before/infront it.

    snake.move()























game_screen.exitonclick()
