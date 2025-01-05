from turtle import Turtle

UP = 90
DOWN= 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
            self.t1=Turtle("square")
            self.t2=Turtle("square")
            self.t3=Turtle("square")
            self.snk = [self.t1,self.t2,self.t3]
            self.head = self.snk[0]
            x=0
            y=0
            for t in self.snk:
                t.color("white")
                t.penup()
                t.goto(x,y)
                x-=20
    def add_segment(self, position):
          new_segment = Turtle("square")
          new_segment.color("white")
          new_segment.penup()
          new_segment.goto(position)
          self.snk.append(new_segment)

    def extend(self):
          #add new segment to snake
          self.add_segment(self.snk[-1].position()) # to add at last position of the list

    def move(self):
            snk = self.snk
            for r in range(len(snk)-1 , 0, -1): #first one is starting point(here last square of our snake) 
                                          #second is end point and last is how many points we are moving in each step
                new_x = snk[r-1].xcor()
                new_y = snk[r-1].ycor()
                snk[r].goto(new_x,new_y)

            '''the above for loop ensures that all the 
            square follows first square of our snake'''

            snk[0].forward(20)
            


    def Up(self):
            snk = self.snk
            if snk[0].heading() != DOWN:
                snk[0].setheading(UP)
    def Down(self):
            snk = self.snk
            if snk[0].heading() != UP:
                snk[0].setheading(DOWN)
    def Left(self):
            snk = self.snk
            if snk[0].heading() != RIGHT:
                snk[0].setheading(LEFT)
    def Right(self):
            snk = self.snk
            if snk[0].heading() != LEFT:
                snk[0].setheading(RIGHT)
            

            




