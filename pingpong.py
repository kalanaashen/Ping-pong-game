from turtle import Screen
from bat import Bat
from map import Map
from ball2 import Ball
from scoreborad import Scoreboard
import time

positions=[(-70,280),(70,280)]
screen=Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title("pakaya")
screen.tracer(0)
ball=Ball()
bat=Bat()
pitch=Map()

score1=Scoreboard(positions[0])
score2=Scoreboard(positions[1])



screen.listen()
screen.onkey(bat.bat1_up,"Up")
screen.onkey(bat.bat1_down,"Down")
screen.onkey(bat.bat2_up,"w")
screen.onkey(bat.bat2_down,"s")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_forward()

    if bat.bat1.distance(ball)<50 and ball.ycor()>-300:
        ball.x_move*=-1
        score1.marks_up()

    if bat.bat2.distance(ball)<50 and ball.ycor()<300:

        ball.x_move*=1
        score2.marks_up()

    if ball.ycor()<-280 or ball.ycor()>280:
        ball.bounce()













screen.exitonclick()