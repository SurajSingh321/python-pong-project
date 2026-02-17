from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time      
from scoreboard import Scoreboard 

#SCREEN SETUP
screen = Screen()
screen.title("PING PONG GAME")
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

#RIGHT PADDLE CONTROL
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

#LEFT PADDLE CONTROL
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:

    time.sleep(ball.move_spped)
    screen.update()
    ball.move()

    #DETECT COLLISION WITH WALL
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #DETECT COLLISION WITH LEFT AND RIGHT PADDLE
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()

    #DETECT RIGHT PADDLE MISS
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    
    #DETECT LEFT PADDLE MISS
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

    
    



















screen.exitonclick()