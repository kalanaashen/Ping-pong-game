from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score=0
        self.goto(pos)
        self.update_scoreborad()

    def update_scoreborad(self):
        self.write(f"SCORE:{self.score}", False, "center", font=("arial", 20, "bold"))

    def marks_up(self):
        self.score+=1
        self.clear()
        self.write(f"SCORE:{self.score}", False, "center", font=("arial", 20, "bold"))






