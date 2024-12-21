from turtle import Turtle
POSITIONS=[(-330,0),(330,0)]
HEADINGS=[0,180]
class Bat():

    def __init__(self):
        self.segments=[]
        self.create_bats()
        self.bat1=self.segments[0]
        self.bat2=self.segments[1]

    def create_bats(self):
        for bat in POSITIONS:
            bat_1=Turtle()
            bat_1.shape("square")
            bat_1.color("white")
            bat_1.penup()
            bat_1.shapesize(stretch_wid=5,stretch_len=1)
            bat_1.goto(bat)
            self.segments.append(bat_1)

    def bat1_up(self):
        y1=self.bat1.ycor()
        if y1 < 280:
            self.bat1.sety(y1+80)
    def bat1_down(self):
        y1= self.bat1.ycor()
        if y1 > -280:
            self.bat1.sety(y1 - 80)

    def bat2_up(self):
        y2= self.bat2.ycor()
        if y2 < 280:
            self.bat2.sety(y2 + 80)
    def bat2_down(self):
        y2= self.bat2.ycor()
        if y2 > -280:
            self.bat2.sety(y2 -80)
