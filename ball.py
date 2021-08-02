from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.75)
        self.penup()
        self.speed("fast")
        self.setheading(90)
        self.x_move=10
        self.y_move=10
        self.move_speed = 0.1
        self.goto((0,-220))

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def ball_freeze_right(self):
        #10 because that is speed of paddle
        new_x = self.xcor()+15
        self.goto(new_x, self.ycor())
    def ball_freeze_left(self):
        #10 because that is speed of paddle
        new_x = self.xcor()-15
        self.goto(new_x, self.ycor())

    def wall_bounce(self):
        #reverse x direction
        self.x_move *= -1

    def y_bounce(self):
        #we hit roof
        self.y_move *= -1