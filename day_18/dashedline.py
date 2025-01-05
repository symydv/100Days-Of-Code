from turtle import Turtle,Screen

l=Turtle()

x=0
while x<=10:
    l.forward(10)
    l.up()   #(or can use penup)
    l.forward(10)
    l.down()
    x+=1



s=Screen()
s.exitonclick()