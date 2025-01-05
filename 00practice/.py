from turtle import Turtle,Screen

self = Turtle()
s=Screen()

def moveup():
    self.forward(20)

self.shape("square")
self.up()
self.left(90)

self.shapesize(stretch_len=4)
s.listen()
s.onkey(self.forward(20),"Up")


s.exitonclick()
 
