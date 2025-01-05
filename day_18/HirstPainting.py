import turtle
import random

t=turtle.Turtle()
s=turtle.Screen()

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

t.width(20)
t.up()
t.setposition(-300,-300) #(to take our unitial point at given position)
t.down()
y=0
while y<=8:
    x=0
    while x<=8:
        t.color(random_color())
        t.forward(0)
        t.up()
        t.forward(50)
        t.down()
        t.forward(0)
        x+=1
    t.up()
    t.left(90)
    t.left(90)
    t.forward(450)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.down()
    y+=1
s.exitonclick()