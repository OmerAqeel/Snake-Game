from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x = -30, y = 280)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", font=("Algerian", 17, "normal"))

