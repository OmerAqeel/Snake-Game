from turtle import Turtle
import random

X = random.randint(-270, 270)
Y = random.randint(-270, 270)
class Food(Turtle):         #Inheriting from the Turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(x=X,y=Y)
