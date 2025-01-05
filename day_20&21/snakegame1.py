from turtle import Screen
from snake import Snake
from scoreboard import Score
import food
import time

s = Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0) #used to controll the screen images delays

saap = Snake()
khana = food.Food()
score = Score()
score.highScore()

s.listen()
s.onkey(saap.Up,"Up") #Up is used for up arrow key(dont forgate "u" is in upper case)
s.onkey(saap.Down,"Down")
s.onkey(saap.Left,"Left")
s.onkey(saap.Right,"Right")

game_is_on = True
while game_is_on: 
    s.update() #after using it the above loop(from tracer() to update()) will be completed altogethr intirely not piece by piece
    time.sleep(0.1) #delay by 0.1 second 
    saap.move()

    #detect collision with food.
    if saap.head.distance(khana) < 15:
        score.point()
        khana.refresh()
        saap.extend()

    #detect collision with food.
    if saap.head.xcor()>280 or saap.head.xcor()<-280 or saap.head.ycor()>280 or saap.head.ycor()<-280:
        score.game_over()
        game_is_on = False

    # detect collision with tail.
    #we removed first segment using  slicing because head is always in colision with head
    for segment in saap.snk[1:]:
        if saap.head.distance(segment) < 10 :
            game_is_on = False
            score.game_over()

    

s.exitonclick()