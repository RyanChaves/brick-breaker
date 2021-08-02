from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0,220)
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(f"Score: {self.score}" )