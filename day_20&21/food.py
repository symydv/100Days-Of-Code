from turtle import Turtle
import random

class Food(Turtle):  #inherit from Turtle class

    def __init__(self):
        super().__init__() #now we can use all methods of Turtle directly
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)  #it will make it 10*10 pixel from 20*20 pixels
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

        

