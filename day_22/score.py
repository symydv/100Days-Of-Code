from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.show_score()

    def show_score(self):
        self.goto(-100,245)
        self.write(self.lscore, align="center",font=("Courier", 40 , "normal"))
        self.goto(100,245)
        self.write(self.rscore, align="center",font=("Courier", 40 , "normal"))

    def lpoint(self):
        self.clear()
        self.lscore+=1
        self.show_score()

    def rpoint(self):
        self.clear()
        self.rscore+=1
        self.show_score()