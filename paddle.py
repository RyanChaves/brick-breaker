from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def left(self):
        self.setx(self.xcor()-15)

    def right(self):
        self.setx(self.xcor()+15)