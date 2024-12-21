import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.discrip()

    def discrip(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.left(45)
        self.speed("slow")
        self.x_move=10
        self.y_move=10

    def bounce(self):
            self.y_move*=-1



    def ball_forward(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)


