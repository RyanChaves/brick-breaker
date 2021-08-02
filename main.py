from turtle import Screen
from paddle import Paddle
from brick_manager import BrickManager
from score import Score
from ball import Ball
import time



def left():
    user_paddle.left()
    if ball_frozen:
        ball.ball_freeze_left()
def right():
    user_paddle.right()
    if ball_frozen:
        ball.ball_freeze_right()

def game_start():
    global ball_frozen
    ball_frozen=False

    while game_is_on:
        time.sleep(0.08)
        screen.update()
        ball.move()

        #check for wall collision
        if ball.xcor()> 280 or ball.xcor()<-280:
            ball.wall_bounce()
        #check for paddle collision
        if ball.ycor()>-240 and ball.distance(user_paddle)<30:
            ball.y_bounce()

        #loop through bricks and check for contact
        for brick in brick_manager.all_bricks:
            if ball.distance(brick)<25:
                #remove brickk from array and make brick invisible
                brick.hideturtle()
                brick_manager.all_bricks.remove(brick)
                #game_is_on=False
                ball.y_bounce()



screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.tracer(0)

user_paddle = Paddle((0,-240))
ball = Ball()
#ball starts frozen to paddle
ball_frozen = True


screen.listen()

screen.onkeypress(left, "Left")
screen.onkeypress(right,"Right")
screen.onkeypress(game_start, "space")


brick_manager = BrickManager()

score = Score()


#starting values for lpocation of bricks
x_grid=-275
y_grid=190
# create grid for level
#nested for loop rows,columns
for y in range(6):
    #13 columns
    for x in range(13):
        brick_manager.create_brick((x_grid, y_grid))
        x_grid+=45
    y_grid-=25
    #reset x cor
    x_grid=-275

game_is_on = True

while game_is_on:
    screen.update()
    #ball.move()

screen.exitonclick()