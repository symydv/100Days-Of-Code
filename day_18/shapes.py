from turtle import Turtle,Screen
import random
t=Turtle()
s=Screen()

c=["red","green","blue","sea green","orange","pink","black","purple"]
y=3
r=0
z=0

while y<=10:
    x=360/y
    t.color(random.choice(c))

    for r in range(y):
        t.forward(100)
        t.left(x)

    y+=1
    z+=1

s.exitonclick()