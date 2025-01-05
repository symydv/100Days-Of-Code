#tuples are like lists but they cannot be edited or changed

t = (1,3,8)  # a tuple

print(t[0])

#We can use R G B concept to generate random colors in our walk

import turtle
from turtle import Turtle,Screen
import random


t = Turtle()
s = Screen()
t.width(10)
t.speed(0)

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
x=0
while x<=1:
    t.color(random_color())
    r=random.randint(0,1)
    
    t.forward(30)
    if r==0:
        t.right(90)
    else:
        t.left(90)
    


s.exitonclick()