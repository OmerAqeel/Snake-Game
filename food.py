from turtle import Turtle
import random

X = random.randint(-270, 270)       #random X axis point on the screen
Y = random.randint(-270, 270)       #random Y axis point on the screen

#Inheriting from the Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(x=X,y=Y)      #The food will move to random points on the screen

    #As soon as the snake will eat the food the food will move to new position on the screen
    def move(self):
        new_posX = random.randint(-270, 270) 
        new_posY = random.randint(-270, 270)
        self.goto(x = new_posX, y = new_posY)
