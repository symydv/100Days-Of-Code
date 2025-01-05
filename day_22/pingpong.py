from turtle import Screen
from centerLine import Line
from body import Body
from ball import Ball
from score import Score
import time

s=Screen()

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("PING PONG")
s.tracer(0)

#draw center line
l = Line()
l.drawLine()

#create players
p1= Body()
p1.player1()

p2= Body()
p2.player2()

#create ball
b= Ball()
scoreboard = Score()

s.listen()
s.onkeypress(p1.moveup,"Up")
s.onkeypress(p1.movedown, "Down")

s.onkeypress(p2.moveup,"w")
s.onkeypress(p2.movedown, "s")


game_is_on = True
x=0.1
while game_is_on:
    s.update() 
    time.sleep(x)
    b.move()
    if b.ycor()<-280 or b.ycor()>280 :
        b.bounce_y()

    #detect collision with right paddle
    if b.distance(p1) < 50 and b.xcor() > 320:
        x *= 0.95
        b.bounce_x()

    #detect collision with left paddle
    if b.distance(p2) < 50 and b.xcor() < -320:
        x *= 0.95
        b.bounce_x()
    
    if b.xcor() > 380 :
        scoreboard.lpoint()
        x = 0.1
        b.reset()

    if b.xcor() < -380:
        scoreboard.rpoint()
        x = 0.1
        b.reset()







s.exitonclick()
