from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(x=-130, y=270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score    # The final score becomes the high score if the score was greater than the all time high score
        self.score = 0                  # The score is set back to 0 soon after the game is reset
        self.update_score()

    def update_score(self):
        self.clear()        # clears the previous score from the turtle screen to avoid overlapping
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", font=("Courier", 21, "normal"))

    def giveScore(self):
        self.score += 1     # score will increment by 1
        self.update_score() # after the previous score has been cleared the score is updated
