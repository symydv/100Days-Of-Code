from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        pass
    def drawLine(self):
        self.up()
        self.color("white")
        self.goto(0,-300)
        self.left(90)
        x=0
        while x < 20:
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)
            x+=1