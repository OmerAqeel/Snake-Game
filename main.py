from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

#Game Screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)

# Game objects
snake = Snake()
food = Food()
score = ScoreBoard()
game_Over = Turtle()


#Moves
game_screen.listen()
game_screen.onkey(key="Up", fun=snake.move_up)
game_screen.onkey(key="Down", fun=snake.move_down)
game_screen.onkey(key="Right", fun=snake.move_right)
game_screen.onkey(key="Left", fun= snake.move_left)

in_the_Game = True


def game_over():
    game_Over.color("white")
    game_Over.penup()
    game_Over.goto(x=-49, y=0)
    game_Over.write("GAME OVER.", font=("Courier", 21, "normal"))
    game_Over.hideturtle()


while in_the_Game:
    distance = 10
    game_screen.update()
    time.sleep(0.1)

#Detecting the collision between the food and snake
    if snake.head.distance(food) < 15:
        food.move()
        score.giveScore()
#Detecting the collision between the wall and the snake
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over()
        in_the_Game = False

    snake.move()























game_screen.exitonclick()
