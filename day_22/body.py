from turtle import Turtle
players = []

class Body(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.shapesize(stretch_len=5)

    def player1(self):
        self.up()
        self.goto(350,0)

    def player2(self):
        self.up()
        self.goto(-350,0)

    def moveup(self):
        self.forward(40)
    def movedown(self):
        self.back(40)



