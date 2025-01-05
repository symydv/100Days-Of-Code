from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1: 
            new_car = Turtle()   
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=1.8)
            new_car.color(random.choice(COLORS))
            position_y = random.randint(-250,250)
            new_car.goto(280,position_y)

            self.all_cars.append(new_car)
        

    def move(self):
        for car in self.all_cars:
            car.back(self.carSpeed)

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT



    
        
        
        


            


