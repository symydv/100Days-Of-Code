from turtle import Turtle,Screen #( (*) imported every thing from turtle but it is confusing as we dont know where Turtle and Screen came from )

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
x=0
while x<=3:
    timmy.forward(100)
    timmy.left(90) 
    x+=1

screen = Screen()
screen.exitonclick()

