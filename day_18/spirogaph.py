import turtle
import random
from turtle import Turtle , Screen

t= Turtle()
s = Screen()
t.speed(0)

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

x=0
while x<=359:
    t.color(random_color())
    t.circle(100)
    t.left(1)
    x+=1

s.exitonclick()