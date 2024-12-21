from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()

        self.x_move = 10
        self.y_move = 10




    '''def ball_shape(self):
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.x_move = 10
        self.y_move = 10'''

    def ball_forward(self):
        self.goto(self.x_move+self.xcor(),self.y_move+self.ycor())


