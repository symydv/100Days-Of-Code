import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

t =Player()
car_manager = CarManager()
score =Scoreboard()



screen.listen()
screen.onkeypress(t.move , "Up")

cars = []
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    #detect collition with car
    for car in car_manager.all_cars:
        if car.distance(t) < 20:
            score.crash( )
            game_is_on = False

    #detect succesfull crossing
    if t.is_at_finish_line():
        t.gotoStart()
        car_manager.levelUp()
        score.levl_up()



screen.exitonclick()
    