from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
tim = Turtle()
class Snake:
    def __init__(self):
        self.segments = []
        # Creating the segments of snakes
        self.create()
        self.head = self.segments[0]        #initialising the head of the snake
    def create(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        seg = Turtle(shape="square")
        seg.penup()
        seg.color("green")
        seg.setposition(pos)
        self.segments.append(seg)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position()) #adding the snake segment to the last position (-1)

    # Each segment will move to the position of the segment before/infront it.
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)
        self.head.forward(DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:       #The snake should not move up if its going down (that is how the snake game works)
            self.head.setheading(90)
    def move_down(self):
        if self.head.heading() != 90:        #The snake should not move down if its going up (that is how the snake game works)
            self.head.setheading(270)
    def move_left(self):
        if self.head.heading() != 0:         #The snake should not move left if its going right (that is how the snake game works)
            self.head.setheading(180)
    def move_right(self):
        if self.head.heading() != 180:       #The snake should not move right if its going left (that is how the snake game works)
            self.head.setheading(0)


