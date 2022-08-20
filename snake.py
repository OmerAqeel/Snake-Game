from turtle import Turtle
class Snake:
    def __init__(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        global segments
        segments = []
        # Creating the segments of snakes
        for pos in positions:
            seg = Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.setposition(pos)
            segments.append(seg)

    # Each segment will move to the position of the segment before/infront it.
    def move(self):
        for seg in range(len(segments) - 1, 0, -1):
            new_x = segments[seg - 1].xcor()
            new_y = segments[seg - 1].ycor()
            segments[seg].goto(x=new_x, y=new_y)
        segments[0].forward(20)
