from turtle import Turtle, Screen
import time

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)
positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for pos in positions:
    seg = Turtle(shape="square")
    seg.penup()
    seg.color("white")
    seg.setposition(pos)
    segments.append(seg)

in_the_Game = True

while in_the_Game:
    distance = 10
    game_screen.update()
    time.sleep(0.1)

    for seg in range(start= len(segments) -1, stop=0, step=-1):























game_screen.exitonclick()