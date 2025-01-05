from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def backward():
    tim.back(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")
screen.onkey(clear,"c")

screen.exitonclick()
