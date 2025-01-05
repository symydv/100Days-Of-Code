from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen() #this func enable screen to listwn to keyboard
screen.onkey(key="space", fun=move_forward) # used to bind a key to a function
#in above case we are using a function move_forward inot another function onkey so onkey is called higher order function

screen.exitonclick()