from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        # Creating the segments of snakes
        self.create()
    def create(self):
        for pos in positions:
            seg = Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.setposition(pos)
            self.segments.append(seg)

    # Each segment will move to the position of the segment before/infront it.
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)

