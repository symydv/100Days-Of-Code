from turtle import Turtle
FONT = ("Courier", 15, "normal")
FONT2 = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-240,270)
        self.write(f"LEVEL : {self.level}" , align="center", font = FONT)

    def levl_up(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL : {self.level}" , align="center", font = FONT)

    def crash(self):
        self.goto(-100,0)
        self.write("GAME OVER" , font= FONT2)
