ffrom turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x = -30, y = 280)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font=("Algerian", 17, "normal"))

    def giveScore(self):
        self.score += 1     # score will increment by 1
        self.clear()        # clears the previous score from the turtle screen to avoid overlapping
        self.update_score() # after the previous score has been cleared the score is updated

