from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class BrickManager(Turtle):
    def __init__(self):
        self.all_bricks = []

    def create_brick(self, position):
        new_brick = Turtle("square")
        new_brick.shapesize(stretch_wid=1,stretch_len=2)
        new_brick.penup()
        new_brick.color(random.choice(COLORS))
        new_brick.goto(position)
        self.all_bricks.append(new_brick)