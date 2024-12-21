from turtle import Turtle

POS=[(300,-300),(-300,300)]

class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.pitch()

    def pitch(self):
        pitch=Turtle(shape="square")
        pitch.hideturtle()
        pitch.speed("fastest")
        pitch.color("white")
        pitch.penup()
        pitch.goto(0,310)
        pitch.setheading(270)
        for i in range(30):
            pitch.forward(20)
            pitch.pendown()
            pitch.forward(20)
            pitch.penup()


