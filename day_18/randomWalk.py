from turtle import Turtle,Screen
import random

c=["aquamarine","red","green","blue","orange","brown","burlywood","mintcream"]

t = Turtle()
s = Screen()
t.width(10)
t.speed(0)

x=0
while x<=1:
    color = random.choice(c)
    r=random.randint(0,1)
    t.color(color)
    t.forward(30)
    if r==0:
        t.right(90)
    else:
        t.left(90)
    



s.exitonclick()